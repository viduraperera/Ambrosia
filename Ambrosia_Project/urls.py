from django.urls import path
from . import views
from . views import *

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


    # transport management

    # Driver
    path('Factory/Transport', views.driver_records, name="Transport"),
    path('Factory/Transport/UpdateDriver', views.DisplayDriverRecord, name="ShowDriver"),
    path('Factory/Transport/DeleteDriverRecords', views.deleteDriverRecord, name="delete_Driver_record"),
    path('Factory/Transport/Records', views.UpdateDriverRecord, name="update_Driver_record"),

    # Vehicle
    path('Factory/Transport/AddVehicle', views.Vehicle_Records, name="addVehicle"),
    path('Factory/Transport/DeleteVehicleRecords', views.deleteVehicleRecord, name="delete_record"),

    #Driving records
    path('Factory/Transport/DrivingRecords', views.DrivingRecords, name="vehicle_records"),
    path('Factory/Transport/ShowRecords', views.ShowDrivingRecords, name="RecordTable"),
    path('Factory/Transport/DeleteRecords', views.deleteRecords, name="delete_driving_records"),


    #vehicle repairs
    path('Factory/Transport/VehicleRepairs', views.AddVehicleRepairs, name="VehicleRepairs"),
    path('Factory/Transport/ShowVehicleRepairs', views.ShowVehicleRepairs, name="RepairTable"),
    path('Factory/Transport/EditVehicleRepairs', views.DisplayUpdateRepairs, name="show_repair_records"),

    path('Factory/Transport/UpdateVehicleRepairs', views.UpdateVehicleRepairs, name="update_repair_records"),
    path('Factory/Transport/deleteVehicleRepairs', views.delete_RepairRecords, name="delete_repair_records"),

    #reports
    path('Factory/Transport/Analysis', views.Reports, name="Reports"),
    path('Factory/Transport/Analysis/VehicleRecordsPDF', GenerateVehicle_RecordsPdf.as_view(), name="VehicleReports"),




]



