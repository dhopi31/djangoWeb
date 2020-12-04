from django.shortcuts import render
from .models import Post, PostImage

# Create your views here.
def index(request):
    paket = Post.objects.all()
    print(paket)
    context = {
        'judul' : 'Blog Page',
        'banner' : 'blog/img/banner2.jpg', 
        'kontributor' : 'Blog Page aja',
        'subjudul' : 'Halaman Blog ',
        'list_paket' : paket,
        'nav':
            [
                ['/','Home'],
                ['/blog/cerita','Cerita'],
                ['/blog/news','News'],
            ],
        'member' : '/member',
        'signout' : '/member/signout'
        
    }
    return render(request, 'blog/index.html', context)

def news(request):
    context = {
        'judul' : 'News Blog Page',
        'banner' : 'blog/img/banner2.jpg',
        'kontributor' : 'Blog Page aja',
        'nav':
            [
                ['/','Home'],
                ['/blog/cerita','Cerita'],
                ['/blog/news','News'],
            ]
    }
    return render(request, 'blog/index.html', context)

def cerita(request):
    context = {
        'judul' : 'Cerita Blog Page ',
        'kontributor' : 'Blog Page aja',
        'banner' : 'blog/img/banner2.jpg', 
        'nav':
            [
                ['/','Home'],
                ['/blog/cerita','Cerita'],
                ['/blog/news','News'],
            ]
    }
    return render(request, 'blog/index.html', context)

def detail(request, slugInput):

    slugImage = Post.objects.get(slug=slugInput)
    list_img = PostImage.objects.filter(post_id=slugImage)
    print(slugImage)
    print(list_img)

    context = {
        'judul' : 'Product Detail',
        'kontributor' : 'Blog Page aja',
        'list_img' : list_img,
        'slugImage' : slugImage,
        'nav':
            [
                ['/','Home'],
                ['/blog/cerita','Cerita'],
                ['/blog/news','News'],
            ],
        'member' : '/member',
        'signout' : '/member/signout'
    }
    return render(request, 'blog/detail.html', context)