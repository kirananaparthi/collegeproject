"""facultyreg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from profileapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',views.f1),
    path('register1/',views.f2),
    path('signin/',views.f3),
    path('show/',views.f4),
    path('student/',views.f5),
    path('sreg/',views.f6),
    path('sign1/',views.f7),
    path('show1/',views.f8),
    path('details/',views.f9),
    path('display/',views.f10),
    path('demo/',views.f11),
    path('event/',views.f12),
    path('event1/',views.f13),
    path('faculty/',views.f14),
    path('facul1/',views.f15),
    path('dep1/',views.f16),
    path('dep/',views.f17),
    path('student12/',views.f18),
    path('studen23/',views.f19)
    
]
