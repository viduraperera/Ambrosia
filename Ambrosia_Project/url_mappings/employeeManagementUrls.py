from django.urls import path
from Ambrosia_Project.view_mappings import employeeManagementViews

urlpatterns = [

    path('selectAttendence', employeeManagementViews.selectAttendence, name="attendance_date"),
    path('Factory/EmployeeHome/viewMarkAttendance', employeeManagementViews.viewMarkAttendance, name="viewMarkAttendance"),

    path('Factory/EmployeeHome/markAttendance', employeeManagementViews.markAttendance, name="mark_attendance"),

    path('Factory/EmployeeHome/attendance_management', employeeManagementViews.attendance_management, name="attendance_management"),
    path('Factory/EmployeeHome/staff_management', employeeManagementViews.staff_management, name="staff_management"),
    path('Factory/EmployeeHome/factoryworkers_management', employeeManagementViews.factoryworkers_management, name="factoryworkers_management"),
    path('Factory/EmployeeHome/factoryworkers_management/delete', employeeManagementViews.deleteEmployee, name="delete_employee"),
    path('Factory/EmployeeHome/edit_employee', employeeManagementViews.edit_employee, name="edit_employee"),
    path('Factory/EmployeeHome/update_employee', employeeManagementViews.update_employee, name="update_employee"),
    path('Factory/EmployeeHome/view_employee', employeeManagementViews.view_employee, name="view_employee"),
    path('Factory/staff_management/AddEmployee', employeeManagementViews.employee_registration, name="employee_registration1"),
    path('Factory/factoryworkers_management/AddEmployee', employeeManagementViews.employee_registration, name="employee_registration2"),

]

