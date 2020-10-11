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

    path('Factory/S_AllRegisteredSuppliers', views.to_reg_suppliers, name="S_AllRegisteredSuppliers"),

    path('Factory/S_AllRegisteredSuppliers/S_ViewSupProfile', views.to_sup_profile, name="S_ViewSupProfile"),

    path('Factory/S_AllRegisteredSuppliers/S_ViewSupProfile/S_EditSupplier', views.to_edit_supplier, name="S_EditSupplier"),

    path('Factory/S_AllRegisteredSuppliers/S_DeleteSupplier', views.delete_supplier, name="S_DeleteSupplier"),

    path('Factory/S_AllRegisteredSuppliers/S_PaymentDetails', views.to_pay_details, name="S_PaymentDetails"),

    path('Factory/S_AllRegisteredSuppliers/S_PaymentDetails/S_SupPayments', views.to_sup_payments, name="S_SupPayments"),

#-----
    path('Factory/S_AllRegisteredSuppliers/S_PaymentDetails/S_SupPayments/calcPayments', views.calc_payment, name="S_CalcPayments"),

    path('Factory/S_AllRegisteredSuppliers/S_PaymentDetails/S_DeletePay', views.payment_delete, name="S_DeletePay"),

    path('Factory/S_AllRegisteredSuppliers/S_SupRegistration', views.to_sup_registration, name="S_SupRegistration"),

    path('Factory/S_AllRegisteredSuppliers/S_SupRegistration/add_supplier', views.add_supplier, name="S_AddSupplier"),

    path('Factory/S_AllRegisteredSuppliers/S_StockDetails', views.to_stock_details, name="S_StockDetails"),

    path('Factory/S_AllRegisteredSuppliers/S_StockDetails/S_LeafStock', views.to_leaf_stock, name="S_LeafStock"),

    path('Factory/S_AllRegisteredSuppliers/S_StockDetails/leaf_stock_delete', views.leaf_stock_delete, name="S_LeafStockDelete"),

    path('Factory/S_AllRegisteredSuppliers/S_StockDetails/S_LeafStock/leaf_stock_add', views.leaf_stock_add, name="S_LeafStockAdd"),


]

