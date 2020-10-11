from django.urls import path
from Ambrosia_Project.view_mappings import supplierManagementViews
from Ambrosia_Project.view_mappings.supplierManagementViews import *

urlpatterns = [


    path('', supplierManagementViews.to_reg_suppliers, name="S_AllRegisteredSuppliers"),

    path('S_ViewSupProfile', supplierManagementViews.to_sup_profile, name="S_ViewSupProfile"),

    path('S_ViewSupProfile/S_EditSupplier', supplierManagementViews.to_edit_supplier,name="S_EditSupplier"),

    path('S_DeleteSupplier', supplierManagementViews.delete_supplier, name="S_DeleteSupplier"),

    path('S_PaymentDetails', supplierManagementViews.to_pay_details, name="S_PaymentDetails"),
    path('S_PaymentDetails/S_PaySlipPDF', S_PaySlipPDF.as_view(), name="S_PaySlipPDF"),

    path('S_PaymentDetails/S_SupPayments', supplierManagementViews.to_sup_payments,name="S_SupPayments"),

    # -----
    path('S_PaymentDetails/S_SupPayments/calcPayments', supplierManagementViews.calc_payment,name="S_CalcPayments"),

    path('S_PaymentDetails/S_DeletePay', supplierManagementViews.payment_delete, name="S_DeletePay"),

    path('S_SupRegistration', supplierManagementViews.to_sup_registration, name="S_SupRegistration"),

    path('S_SupRegistration/add_supplier', supplierManagementViews.add_supplier, name="S_AddSupplier"),

    path('S_StockDetails', supplierManagementViews.to_stock_details, name="S_StockDetails"),

    path('S_StockDetails/S_LeafStock', supplierManagementViews.to_leaf_stock, name="S_LeafStock"),

    path('S_StockDetails/leaf_stock_delete', supplierManagementViews.leaf_stock_delete,name="S_LeafStockDelete"),

    path('S_StockDetails/S_LeafStock/leaf_stock_add', supplierManagementViews.leaf_stock_add,name="S_LeafStockAdd"),

]

