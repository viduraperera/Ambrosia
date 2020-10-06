from django.urls import path
from Ambrosia_Project.view_mappings import salary_management_views


# employee_funds_VUP

urlpatterns = [

    path('emp_fund_view', salary_management_views.emp_fund_view, name="emp_fund_view"),
    path('emp_funds_add/', salary_management_views.emp_funds_add, name="emp_funds_add"),
    path('emp_funds_delete<int:id>', salary_management_views.emp_funds_delete, name="emp_funds_delete"),
    path('emp_funds_edit<int:id>', salary_management_views.emp_funds_edit, name="emp_funds_edit"),
    path('emp_funds_update<int:id>', salary_management_views.emp_funds_update, name="emp_funds_update"),

    # employee_allowance_VUP
    path('emp_allowance/', salary_management_views.emp_allowance, name="emp_allowance"),
    path('emp_allowance_add/', salary_management_views.emp_allowance_add, name="emp_allowance_add"),
    path('emp_allowance_delete<int:id>/', salary_management_views.emp_allowance_delete, name="emp_allowance_delete"),
    path('emp_allowance_edit<int:id>', salary_management_views.emp_allowance_edit, name="emp_allowance_edit"),
    path('emp_allowance_update<int:id>', salary_management_views.emp_allowance_update, name="emp_allowance_update"),

    # employee_salary_VUP
    path('emp_salary_main/', salary_management_views.emp_salary_main, name="emp_salary_main"),
    path('emp_final_salary_view', salary_management_views.emp_final_salary_view, name='emp_final_salary_view')


]

