from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('ViewAllUsers', views.view_AllUsers, name="view_all_users"),


    path('AddUser', views.registration, name='register'),
    path('Factory', views.factoryHomepage, name='factory_home'),
    path('Shop', views.teashopHomepage, name='teashop_home'),

    #Employee Management-------------------------------------------------------------------
    path('Factory/EmployeeHome/', include('Ambrosia_Project.url_mappings.employeeManagementUrls')),

    # employee_funds_VUP---------------------------------------------------------------------------------------------------------------
    path('Factory/EmployeeHome/', include('Ambrosia_Project.url_mappings.salary_management_urls')),

]

