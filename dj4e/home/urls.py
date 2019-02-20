from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('hello/', TemplateView.as_view(template_name='home.html'), name = 'home'),
    # path('helloworld', views.helloworld) ,
    path('', TemplateView.as_view(template_name='main.html')),
]
