from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^signin/', views.signin),
    url(r'^about/', include('about.urls')),
    url(r'^signout/', include('member.urls')),
    url(r'^member/', include('member.urls')),

    url(r'^blog/', include('blog.urls')),
    url(r'^product/', include('product.urls')),
    # url(r'^signup/', views.signup),
    # url(r'^signout/', views.signout),
    # url(r'^about/', include('about.urls')),
]
