from django.urls import path, include
from Ambrosia_Project.view_mappings import teaShopSalesViews
from Ambrosia_Project.view_mappings.teaShopSalesViews import *

urlpatterns = [

    path('', teaShopSalesViews.SalesHomeIncome, name="SalesHomeIncome"),
    path('Shop/SalesHomeIncome/IncomeMonthlyGeneratePDF', GeneratePDFInvoiceMonthly.as_view(),name="generateIncomePdfMonthly"),
    path('Shop/SalesHomeIncome/AnnualIncomeGeneratePDF', GeneratePDFInvoiceAnnually.as_view(),name="SalesHomeAnnuallyIncome"),

    path('Shop/SalesHomeIncome/SalesCreateInvoice', teaShopSalesViews.SalesCreateInvoice, name="SalesCreateInvoice"),
    path('Shop/SalesHomeIncome/DeleteSalesCreateInvoice', teaShopSalesViews.BillRowDelete, name="BillRowDelete"),
    path('Shop/SalesHomeIncome/SalesCreateInvoice/SalesViewBill', teaShopSalesViews.SalesViewBill, name="SalesViewBill"),

    path('Shop/SalesHomeIncome/SalesTransaction', teaShopSalesViews.SalesTransaction, name="SalesTransaction"),
    path('Shop/SalesHomeIncome/SalesTransaction/SalesViewBill', teaShopSalesViews.SalesViewBill, name="SalesViewBill"),
    path('Shop/SalesHomeIncome/SalesTransaction/BillPDF', GenerateBill.as_view(), name="SalesBill"),

    # path('Shop/SalesHomeIncome/SalesTransaction/SalesViewBill/Vdelete', views.Vdelete, name="Vdelete"),
    path('Shop/SalesHomeIncome/SalesPriceTable', teaShopSalesViews.SalesPriceTable, name="SalesPriceTable"),

    path('Shop/SalesHomeIncome/SalesPriceTable/ShopPriceTableEdit', teaShopSalesViews.ShopPriceTableEdit,name="ShopPriceTableEdit"),
    path('Shop/SalesHomeIncome/SalesPriceTable/ShopPriceTableUpdate', teaShopSalesViews.ShopPriceTableUpdate,name="ShopPriceTableUpdate"),


]

