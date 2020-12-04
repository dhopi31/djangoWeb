from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^member/', views.index),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.VerificationEmail.as_view(), name='activate'),
    url(r'^signin/', views.signin),
    url(r'^signout/', views.signout),
]