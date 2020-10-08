from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('ViewAllUsers', views.view_AllUsers, name="view_all_users"),


    path('AddUser', views.registration, name='register'),
    path('Factory', views.factoryHomepage, name='factory_home'),
    path('Shop', views.teashopHomepage, name='teashop_home'),

    path('Factory/EmployeeHome', views.EmployeeHome, name="attendance_date"),
    path('Factory/EmployeeHome/markAttendance', views.markAttendance, name="mark_attendance"),
    path('Factory/EmployeeHome/attendance_management', views.attendance_management, name="attendance_management"),
    path('Factory/EmployeeHome/staff_management', views.staff_management, name="staff_management"),
    path('Factory/EmployeeHome/factoryworkers_management', views.factoryworkers_management, name="factoryworkers_management"),
    path('Factory/EmployeeHome/factoryworkers_management/delete', views.deleteEmployee, name="delete_employee"),
    path('Factory/EmployeeHome/edit_employee', views.edit_employee, name="edit_employee"),
    path('Factory/EmployeeHome/update_employee', views.update_employee, name="update_employee"),
    path('Factory/EmployeeHome/view_employee', views.view_employee, name="view_employee"),
    path('Factory/staff_management/AddEmployee', views.employee_registration, name="employee_registration1"),
    path('Factory/factoryworkers_management/AddEmployee', views.employee_registration, name="employee_registration2"),

    path('Factory/LeafInventory/AddInventory', views.NavigateToInventory, name="AddInventory"),

    path('Factory/FinalProduction/DailyProduction/AddProduction', views.NavigateToProduction, name="NavigateToProduction"),


    path('Factory/S_AllRegisteredSuppliers', views.to_reg_suppliers, name="S_AllRegisteredSuppliers"),


]

