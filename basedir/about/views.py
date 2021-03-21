from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'About',
        'kontributor' : 'ini halaman about',
        'banner' : 'about/img/banner_about.jpg', 
        'nav':
            [
                ['/','Home'],
            ]
    }
    return render(request, 'about/index.html' , context)