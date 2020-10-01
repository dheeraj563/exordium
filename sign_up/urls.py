from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'form',views.adddata),
    url(r'^$', views.index, name='index'),

]
