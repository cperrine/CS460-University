"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student/', views.student),
    path('instructor/', views.instructor),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('administrator_view/administrator_f2/', views.administrator_f2),
    path('administrator_view/administrator_f1/', views.administrator_f1),
    path('administrator_view/administrator_f1/name/', views.f1name),
    path('administrator_view/administrator_f1/department/', views.f1department),
    path('administrator_view/administrator_f1/salary/', views.f1salary),
    path('administrator_view/administrator_f3/', views.administrator_f3),
    path('administrator_view/', views.administrator_view),
    path('instructor/section', views.section),
]
