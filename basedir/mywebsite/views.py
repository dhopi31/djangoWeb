from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from product.models import PostProduct, PostImageProduct

from member.decorators import allowed_users
#menampilkan index
# def index2(request):
#     judul = "home"
#     konten = "konten adalah ...."
#     isi = judul + konten
#     return HttpResponse(isi)

# @allowed_users(allowed_roles=['customer'])
def index(request):

    list_promo = PostProduct.objects.all()[:10]
    print(list_promo)
    context = {
        'judul' : 'Home',
        'banner' : 'img/banner.jpg', 
        'subjudul' : 'Lengkapi Kebutuhan Alat Tulis Anda',
        'list_promo':list_promo,
        'nav' : 
        [
            ['/', 'Home'],
            ['/product', 'Produk'],
            ['/about', 'Kami'],
            
        ],
        'member' : '/member',
        'signout': '/member/signout'
    }
    return render(request, 'index.html' , context)

def signup(request):
    context = {
        'judul' : 'Member',
        'nav' : 
        [
            ['/', 'Home'],
            ['/blog', 'Produk'],
            ['/about', 'Parcel'],
        ],
        'login' : '/signin',
    }
    if request.method=="GET":
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return render(request, 'signup.html' , context)

def signin(request):
    user = None
    context = {
        'judul' : 'Login',
        'nav' : 
        [
            ['/', 'Home'],
            ['/blog', 'Produk'],
            ['/about', 'Parcel'],
        ],
        'member' : '/signup',
    }
    if request.method=="POST":
        username_login = request.POST['username']
        password_login = request.POST['password']
        # print(username)
        # print(password)
        user = authenticate(request, username=username_login, password=password_login)
        print(user)

        if user is not None:
            login(request, user)
            return redirect ('/')
        else:
            return redirect('/signin', context)
        
    if request.method=="GET":
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return render(request, 'login.html' , context)

@login_required
def signout(request):
    context={
        'judul':'Logout',
    }
    print('proses logout')
    logout(request)
    return render( request, 'logout.html', context)

def about(request):
    return render(request, 'about.html')

#permission check untuk 1 fungsi
#hrus import lib
