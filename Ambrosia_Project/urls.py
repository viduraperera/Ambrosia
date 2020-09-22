from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),

#---------User Profile------------------------------------------------------
    path('AddUser', views.registration, name='register'),
    path('ViewAllUsers', views.view_AllUsers, name="view_all_users"),
    path('ViewAllUsers/EditUser', views.ShowUser, name="update_user"),
    path('ViewAllUsers/UpdateUserdetails', views.UpdateUser, name="update_user_details"),
    path('ViewAllUsers/', views.DeleteUser, name="delete_user"),


#---------Main menues-----------------------------------------------------
    path('Factory', views.factoryhome, name='factory_home'),
    path('Shop', views.teashopHomepage, name='teashop_home'),


#---------final Production Auction------------------------------------------------------
    path('Factory/FinalProduction/AuctionStock/', include('Ambrosia_Project.url_mappings.finalProductionAuctionUrls')),


    path('Factory/EmployeeHome', views.EmployeeHome, name="attendance_management"),
    path('Factory/EmployeeHome/markAttendance', views.markAttendance, name="mark_attendance"),
    path('Factory/EmployeeHome/staff_management', views.staff_management, name="staff_management"),
    path('Factory/EmployeeHome/factoryworkers_management', views.factoryworkers_management, name="factoryworkers_management"),

    path('view_employee/EditProfile', views.edit_employee, name="edit_employee"),
    path('edit_employee/Save', views.view_employee, name="view_employee"),

    path('staff_management/AddEmployee', views.employee_registration, name="employee_registration"),
    path('factoryworkers_management/AddEmployee', views.employee_registration, name="employee_registration"),
    path('Factory/EmployeeHome', views.EmployeeHome, name="EmployeeHome"),

    # path('Factory/EmployeeHome', views.EmployeeHome, name="EmployeeHome"),
    path('Factory/LeafInventory/AddInventory', views.NavigateToInventory, name="AddInventory"),
    path('Factory/LeafInventory/PreviousInventories', views.NavigateToPrevInv, name="NavigateToPreInv"),
    path('Factory/LeafInventory/PreviousInventories/UpdateInvenories', views.NavigateToUpdateInv, name="NavigateToUpdateInv"),

    path('Shop/SalesHomeIncome', views.SalesHomeIncome, name="SalesHomeIncome"),
    path('Shop/SalesHomeIncome/SalesHomeMonthlyIncome', views.SalesHomeMonthlyIncome, name="SalesHomeMonthlyIncome"),
    path('Shop/SalesHomeIncome/SalesHomeAnnuallyIncome', views.SalesHomeAnnuallyIncome, name="SalesHomeAnnuallyIncome"),
    path('Factory/EmployeeHome', views.EmployeeHome, name="EmployeeHome"),
    path('Factory/EmployeeHome', views.EmployeeHome, name="EmployeeHome"),

    path('Factory/S_AllRegisteredSuppliers', views.to_reg_suppliers, name="S_AllRegisteredSuppliers"),
    path('Factory/S_AllRegisteredSuppliers/S_SupPayments', views.to_payments, name="S_SupPayments"),
    path('Factory/S_AllRegisteredSuppliers/S_StockDetails', views.to_stock_details, name="S_StockDetails"),
    path('Factory/S_AllRegisteredSuppliers/S_StockDetails/S_LeafStock', views.to_leaf_stock, name="S_LeafStock"),
    path('Factory/S_AllRegisteredSuppliers/S_StockDetails/S_ViewLeafStock', views.to_view_stock_details, name="S_ViewLeafStock"),
    path('Factory/S_AllRegisteredSuppliers/S_SupRegistration', views.to_sup_registration, name="S_SupRegistration"),
    path('Factory/S_AllRegisteredSuppliers/S_SupRegistration/S_ViewSupplierProfile', views.to_sup_profile, name="S_ViewSupplierProfile"),
    path('Factory/S_AllRegisteredSuppliers/S_SupRegistration/S_ViewSupplierProfile/S_EditSupplier', views.to_edit_profile, name="S_EditSupplier"),


    path('Shop/InventoryHome', views.inventoryhome, name="inventoryhome"),
    path('Shop/InventoryHome/addteapackets', views.addteapackets, name="addteapackets"),
    path('Shop/InventoryHome/preorderlevel', views.preorderlevel, name="preorderlevel"),
    path('Shop/InventoryHome/inventoryreports', views.inventoryreports, name="inventoryreports"),
    path('Shop/InventoryHome/inventoryreports/weeklyreport', views.iweekly, name="iweekly"),
    path('Shop/InventoryHome/inventoryreports/inventorymonthlyreport', views.inventorymonthlyreport, name="monthlyreport"),
    path('Shop/InventoryHome/inventoryreports/inventoryannualreport', views.inventoryannualreport, name="annualreport"),
    path('Shop/InventoryHome/addteapackets/editpackets', views.editpackets, name="editpackets"),

    path('Shop/SalesHomeIncome/SalesCreateInvoice', views.SalesCreateInvoice, name="SalesCreateInvoice"),
    path('Shop/SalesHomeIncome/SalesCreateInvoice/SalesViewBill', views.SalesViewBill, name="SalesViewBill"),


    path('Shop/SalesHomeIncome/SalesTransaction', views.SalesTransaction, name="SalesTransaction"),
    path('Shop/SalesHomeIncome/SalesTransaction/SalesViewBill', views.SalesViewBill, name="SalesViewBill"),

    path('Shop/SalesHomeIncome/SalesPriceTable', views.SalesPriceTable, name="SalesPriceTable"),
    path('Shop/SalesHomeIncome/SalesPriceTable/SalesPriceTableDUST1', views.SalesPriceTableDUST1, name="SalesPriceTableDUST1"),
    path('Shop/SalesHomeIncome/SalesPriceTable/SalesPriceTableDUST2', views.SalesPriceTableDUST2, name="SalesPriceTableDUST2"),
    path('Shop/SalesHomeIncome/SalesPriceTable/SalesPriceTableDUST3', views.SalesPriceTableDUST3, name="SalesPriceTableDUST3"),
    path('Shop/SalesHomeIncome/SalesPriceTable/SalesPriceTableFGS', views.SalesPriceTableFGS, name="SalesPriceTableFGS"),


    path('Factory/FinalProduction/', views.NavigateToProduction,name="final_production_home"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction', views.NavigateToCustomDailyProd,name="NavigateToCustomDailyProd"),
    path('Factory/FinalProduction/DailyProduction/CurrentDailyProduction', views.NavigateToCurrentProduct,name="NavigateToCurrentProd"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction/UpdateProduct', views.NavigateToUpdateProduct,name="NavigateToUpdateProd"),
    path('Factory/FinalProduction/DailyProduction/TeaGrades', views.NavigateToTeaGrades,name="NavigateToTeaGrades"),

    #path('Factory/EmployeeHome', views.EmployeeHome, name="EmployeeHome"),

    path('Factory/EmployeeHome', views.emp_fund_view, name="EmployeeHome"),
    path('Factory/EmployeeHome/emp_fund_view', views.emp_fund_view, name="emp_fund_view"),
    path('Factory/EmployeeHome/emp_funds_add/', views.emp_funds_add, name="emp_funds_add"),
    path('Factory/EmployeeHome/emp_funds_delete<int:id>/', views.emp_funds_delete, name="emp_funds_delete"),
    path('Factory/EmployeeHome/emp_allowance/', views.emp_allowance, name="emp_allowance"),
    path('Factory/EmployeeHome/emp_allowance_add/', views.emp_allowance_add, name="emp_allowance_add"),


]

