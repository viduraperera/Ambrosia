from django.urls import path, include
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

    path('view_employee/EditProfile', views.edit_employee, name="edit_employee"),
    path('edit_employee/Save', views.view_employee, name="view_employee"),

    path('staff_management/AddEmployee', views.employee_registration, name="employee_registration"),
    path('factoryworkers_management/AddEmployee', views.employee_registration, name="employee_registration"),
    path('Factory/EmployeeHome', views.EmployeeHome, name="EmployeeHome"),

    path('Factory/EmployeeHome', views.EmployeeHome, name="EmployeeHome"),
    path('Factory/LeafInventory/AddInventory', views.NavigateToInventory, name="AddInventory"),


    path('Shop/SalesHomeIncome', views.SalesHomeIncome, name="SalesHomeIncome"),
    path('Factory/EmployeeHome', views.EmployeeHome, name="EmployeeHome"),

    path('Factory/S_AllRegisteredSuppliers', views.to_reg_suppliers, name="S_AllRegisteredSuppliers"),

    path('Shop/InventoryHome', views.inventoryhome, name="inventoryhome"),

    path('Shop/SalesHomeIncome/SalesCreateInvoice', views.SalesCreateInvoice, name="SalesCreateInvoice"),
    path('Shop/SalesHomeIncome/SalesCreateInvoice/SalesViewBill', views.SalesViewBill, name="SalesViewBill"),

    path('Factory/FinalProduction/', views.NavigateToProduction, name="final_production_home"),



    # employee_funds_VUP
    path('Factory/EmployeeHome/', include('Ambrosia_Project.url_mappings.salary_management_urls')),

]

