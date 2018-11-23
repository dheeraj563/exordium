from . import views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login

app_name = 'home'
urlpatterns = [

    url(r'^search/serpro', views.serpro, name='serpro'),
    url(r'^search/', views.search, name='search'),
    # url(r'^registration/sign_up/form', include('sign_up.urls')),
    #url(r'^registration/sign_up/', include('sign_up.urls'), name = 'reg'),
    url(r'^registration/success/', views.success, name = 'success'),
    url(r'^registration/', views.registration, name = 'registration'),
    url(r'^login/form', views.finddata, name= 'loginform'),
    url(r'^login/', login, {'template_name':'home/login.html'},name='login'),
    url(r'^$', views.index, name='index'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
