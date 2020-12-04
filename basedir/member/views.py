from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.views import View

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from .utils import token_generator

from .forms import LoginForm, SignUpForm1, SignUpForm2
# Create your views here.
def index(request):
    login_form   = LoginForm()
    signup_form1 = SignUpForm1()    
    signup_form2 = SignUpForm2()    
    context = {
        'judul' : 'Member',
        'banner' : 'img/banner.jpg',
        'nav' : 
        [
            ['/', 'Home'],
            ['/blog', 'Produk'],
            ['/about', 'Parcel'],
        ],
        'member' : '/member/',
        'login' : '/member/signin',
        'login_form': login_form,
        'signup_form1':signup_form1,
        'signup_form2':signup_form2,
    }
    if request.method=="POST":

        first_name      = request.POST['first_name']
        last_name       = request.POST['last_name']
        email_signup    = request.POST['email']
        username_signup = request.POST['username']
        password_signup = request.POST['password']

        # if username_signup not value and first_name == '' and last_name == '' and email_signup== '' and password_signup=='':
        #     messages.error(request, "Ada field yang kosong")

        if User.objects.filter(username=username_signup):
            messages.error(request, "Maaf, Username sudah pernah digunakan.")

        elif User.objects.filter(email=email_signup):
            messages.error(request, "Maaf, Email sudah pernah digunakan.")

        elif len(password_signup) < 6:
                messages.error(request, "Maaf, Password terlalu pendek, minimal 6 digit")
        
        else:
            user_signup = User.objects.create_user(
            username     = username_signup,
            first_name   = first_name,
            last_name    = last_name,
            email        = email_signup, 
            password     = password_signup
            )
            user_signup.is_active = False
            user_signup.save()

            # send email
            uidb64  = urlsafe_base64_encode(force_bytes(user_signup.pk))
        
            domain = get_current_site(request).domain
            print(domain)
            link = reverse('activate', kwargs={
                                        'uidb64'    : uidb64, 
                                        'token'     : token_generator.make_token(user_signup),})
            
            active_url = 'http://'+domain+link
            email_body = 'Hi '+first_name+' '+last_name+','+'\nsilahkan untuk aktivasi akun anda terlebih dahulu\n' + active_url

            email_subject = 'Activate Your Account'
            send_mail(
                email_subject,
                email_body, 
                'sandhopi@gmail.com',
                [email_signup], 
                fail_silently=False
            )
            messages.info(request, 'Pembuatan akun berhasil. Silahkan melakukan verifikasi email pada link yang dikirimkan')
            return redirect('/member/signin')


    if request.method=="GET":
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return render(request, 'member/index.html' , context)
    
    return render(request, 'member/index.html' , context)

def signin(request):

    signup_form1 = SignUpForm1()    
    signup_form2 = SignUpForm2()  
    login_form = LoginForm()
    context = {
        'judul' : 'Member',
        'banner' : 'img/banner.jpg',
        'nav' : 
        [
            ['/', 'Home'],
            ['/blog', 'Produk'],
            ['/about', 'Parcel'],
        ],
        'member' : '/member/',
        'login_form': login_form,
        'signup_form1':signup_form1,
        'signup_form2':signup_form2,
    }

    if request.method=="POST":
        
        username_login = request.POST['username']
        password_login = request.POST['password']
        user_auth = authenticate(request, username=username_login, password=password_login)
        print(user_auth)

        user = User.objects.get(username=username_login)
        print(user.is_active)

        if user.is_active==False:
            messages.error(request, "Akun anda belum diaktivasi, silahkan melakukan aktivasi melalui link di email.")
            return redirect('/member/signin', context)

        if user_auth is not None:
            login(request, user_auth)
            messages.info(request, "Anda berhasil Login.")
            return redirect ('/',context)
            
        else:
            messages.error(request, "Username dan Password tidak cocok.")
            return redirect('/member/signin', context)
            
    if request.method=="GET":
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return render(request, 'member/login.html' , context)

@login_required
def signout(request):
    context={
        'judul':'Logout',
    }
    print('proses logout')
    logout(request)
    return render(request, 'member/logout.html', context)

class VerificationEmail(View):

    def get(self, request, uidb64, token):
        
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            print(id)
            print(user)
            print(token_generator.check_token(user, token))
            print(user.is_active)
            if not token_generator.check_token(user, token):
                return redirect('/member/signin'+'?message='+'user siap diaktivasi')

            if user.is_active:
                return redirect('/member/signin')
            user.is_active = True
            user.save()

            messages.success(request,'Akun anda sukses diaktivasi')
            return redirect('/member/signin')

        except Expression as ex:
            pass
        
        # return redirect('/member/signin')
        
        
