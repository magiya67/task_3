from django.contrib import admin
from django.urls import path
from app3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('contents/', views.contents),
    path('contents/<int:content_id>', views.contents),
]