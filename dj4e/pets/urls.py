from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.PetList.as_view(), name='pets'),
    path('main/create/', views.PetCreate.as_view(), name='pets_create'),
    path('main/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
    path('main/<int:pk>/delete/', views.PetDelete.as_view(), name='pets_delete'),
    path('lookup/', views.KindView.as_view(), name='kind_list'),
    path('lookup/create/', views.KindCreate.as_view(), name='kind_create'),
    path('lookup/<int:pk>/update/', views.KindUpdate.as_view(), name='kind_update'),
    path('lookup/<int:pk>/delete/', views.KindDelete.as_view(), name='kind_delete'),
]
