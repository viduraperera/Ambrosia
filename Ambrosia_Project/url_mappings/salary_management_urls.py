from django.urls import path
from Ambrosia_Project.view_mappings import salary_management_views
from Ambrosia_Project.view_mappings.salary_management_views import FinalSalaryReportPDF, FinalEpfReportPDF

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
    path('emp_final_salary_view', salary_management_views.emp_final_salary_view, name='emp_final_salary_view'),
    path('emp_epf_view', salary_management_views.emp_epf_view, name='emp_epf_view'),
    path('emp_etf_view', salary_management_views.emp_etf_view, name='emp_etf_view'),
    path('emp_salary_single_view', salary_management_views.emp_salary_single_view, name='emp_salary_single_view'),
    path('emp_add_salary_view', salary_management_views.emp_add_salary_view, name='emp_add_salary_view'),
    path('emp_final_salary_view', salary_management_views.emp_final_salary_view, name='emp_final_salary_view'),
    path('emp_final_salary_single_view', salary_management_views.emp_final_salary_single_view, name='emp_final_salary_single_view'),
    path('emp_final_total_salary_view', salary_management_views.emp_final_total_salary_view, name='emp_final_total_salary_view'),
    path('delete_total_salary', salary_management_views.delete_total_salary, name='delete_total_salary'),
    path('final_salary_report_view', salary_management_views.final_salary_report_view, name='final_salary_report_view'),


    path('searchEmployee', salary_management_views.searchEmployee, name='searchEmployee'),
    path('final_salary_view_search', salary_management_views.final_salary_view_search, name='final_salary_view_search'),
    path('final_salary_report_search', salary_management_views.final_salary_report_search, name='final_salary_report_search'),
    path('final_epf_report_search', salary_management_views.final_epf_report_search, name='final_epf_report_search'),

    path('final_salary_pdf', FinalSalaryReportPDF.as_view(), name='final_salary_pdf'),
    path('final_epf_pdf', FinalEpfReportPDF.as_view(), name='final_epf_pdf'),

]



