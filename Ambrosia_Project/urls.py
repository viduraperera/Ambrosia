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

]

