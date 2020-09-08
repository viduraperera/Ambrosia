from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('ViewAllUsers', views.view_AllUsers, name="view_all_users"),
    path('ViewAllUsers/EditUser', views.ShowUser, name="update_user"),
    path('ViewAllUsers/UpdateUserdetails', views.UpdateUser, name="update_user_details"),
    path('ViewAllUsers/', views.DeleteUser, name="delete_user"),


    path('AddUser', views.registration, name='register'),
    path('Factory', views.factoryHomepage, name='factory_home'),
    path('Shop', views.teashopHomepage, name='teashop_home'),

    path('Factory/EmployeeHome', views.EmployeeHome, name="EmployeeHome"),

    path('Factory/Transport', views.VehicleRecords, name="Transport"),
    path('Factory/Transport/RetrieveVehicleTable', views.RetrieveVehicleTable, name="RetrieveVehicleTable"),
    path('Factory/Transport/RetrieveVehicleTable/EditVehicleRecords', views.EditVehicleRecords, name="EditVehicleRecords"),
    path('Factory/Transport/VehicleRecords/VehicleRepairs', views.VehicleRepairs, name="VehicleRepairs"),
    path('Factory/Transport/VehicleRepairs/FuelLog', views.FuelLog, name="FuelLog"),









]

