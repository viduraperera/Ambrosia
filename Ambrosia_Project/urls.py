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

    path('Factory/EmployeeHome', views.EmployeeHome, name="attendance_management"),
    path('Factory/EmployeeHome/markAttendance', views.markAttendance, name="mark_attendance"),
    path('Factory/EmployeeHome/staff_management', views.staff_management, name="staff_management"),
    path('Factory/EmployeeHome/factoryworkers_management', views.factoryworkers_management, name="factoryworkers_management"),


]

