from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.StarList.as_view(), name='stars'),
    path('main/create/', views.StarCreate.as_view(), name='stars_create'),
    path('main/<int:pk>/update/', views.StarUpdate.as_view(), name='stars_update'),
    path('main/<int:pk>/delete/', views.StarDelete.as_view(), name='stars_delete'),
    path('lookup/', views.ConstellationView.as_view(), name='constellation_list'),
    path('lookup/create/', views.ConstellationCreate.as_view(), name='constellation_create'),
    path('lookup/<int:pk>/update/', views.ConstellationUpdate.as_view(), name='constellation_update'),
    path('lookup/<int:pk>/delete/', views.ConstellationDelete.as_view(), name='constellation_delete'),
]
