"""ITProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from Ambrosia_Project import views

urlpatterns = [
    path('admin/', admin.site.urls, name="adminPannel"),
    # path('' , include('Ambrosia.urls'))

    path('', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('Home/', include('Ambrosia_Project.urls')),

    path('emp_fund_view/', views.emp_fund_view, name="emp_fund_view"),
    path('emp_funds_add/', views.emp_funds_add, name="emp_funds_add"),
    path('emp_funds_delete<int:id>/', views.emp_funds_delete),
    path('emp_allowance/', views.emp_allowance, name="emp_allowance")


]
