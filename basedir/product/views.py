from django.shortcuts import render
from django.shortcuts import render
from .models import PostProduct, PostImageProduct

def detail(request, slugInput):

    slugImage = PostProduct.objects.get(slug=slugInput)
    list_img = PostImageProduct.objects.filter(post_id=slugImage)
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
            ],
        'member' : '/member',
        'signout' : '/member/signout'
    }
    return render(request, 'product/detail.html', context)