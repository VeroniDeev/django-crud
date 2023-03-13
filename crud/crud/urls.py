from django.contrib import admin
from django.urls import path
from interface import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('read/<int:id>/', views.read, name='read-user'),
    path('update/', views.update, name='update'),
    path('update/<int:id>/', views.update_user, name='update-user'),
]
