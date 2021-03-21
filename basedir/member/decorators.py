from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwarg):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args, **kwarg)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwarg):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwarg)
            else:
                return HttpResponse('Kamu tidak berhak melihat halaman ini')
        return wrapper_func
    return decorator
