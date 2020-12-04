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
                ['/about/kontak','Kontak'],
            ]
    }
    return render(request, 'about/index.html' , context)

def kontak(request):
    context = {
        'judul' : 'Halaman Kontak',
        'banner' : 'about/img/banner_about.jpg', 
        'kontributor' : 'ini halaman kontak',
        'nav':
            [
                ['/','Home'],
                ['/about/kontak','Kontak'],
            ]
    }
    return render(request, 'index.html', context)