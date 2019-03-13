from django.urls import path
from challengica_app import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.index, name='index'),
    #path('set/<int:set_no>/ques/welcome', views.welcome, name='welcome'),
    path('set/<int:set_no>/ques/<slug:ans>', views.generateques, name='question'),
]
