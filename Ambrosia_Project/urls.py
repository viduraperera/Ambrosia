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

    path('Shop/SalesHomeIncome', views.SalesHomeIncome, name="SalesHomeIncome"),
    path('Shop/SalesHomeIncome/SalesHomeMonthlyIncome', views.SalesHomeMonthlyIncome, name="SalesHomeMonthlyIncome"),
    path('Shop/SalesHomeIncome/SalesHomeAnnuallyIncome', views.SalesHomeAnnuallyIncome, name="SalesHomeAnnuallyIncome"),


    path('Shop/SalesHomeIncome/SalesCreateInvoice', views.SalesCreateInvoice, name="SalesCreateInvoice"),
    path('Shop/SalesHomeIncome/SalesCreateInvoice/SalesViewBill', views.SalesViewBill, name="SalesViewBill"),


    path('Shop/SalesHomeIncome/SalesTransaction', views.SalesTransaction, name="SalesTransaction"),
    path('Shop/SalesHomeIncome/SalesTransaction/SalesViewBill', views.SalesViewBill, name="SalesViewBill"),

    path('Shop/SalesHomeIncome/SalesPriceTable', views.SalesPriceTable, name="SalesPriceTable"),
path('Shop/SalesHomeIncome/SalesPriceTable/ShopPriceTableBOPFUpdate', views.ShopPriceTableBOPFUpdate, name="ShopPriceTableBOPFUpdate"),

    path('Shop/SalesHomeIncome/SalesPriceTable/SalesPriceTableDUST1', views.SalesPriceTableDUST1, name="SalesPriceTableDUST1"),
    path('Shop/SalesHomeIncome/SalesPriceTable/SalesPriceTableDUST1/ShopPriceTableDUST1Update', views.ShopPriceTableDUST1Update, name="ShopPriceTableDUST1Update"),

    path('Shop/SalesHomeIncome/SalesPriceTable/SalesPriceTableDUST2', views.SalesPriceTableDUST2, name="SalesPriceTableDUST2"),
    path('Shop/SalesHomeIncome/SalesPriceTable/SalesPriceTableDUST2/ShopPriceTableDUST2Update', views.ShopPriceTableDUST2Update, name="ShopPriceTableDUST2Update"),


    path('Shop/SalesHomeIncome/SalesPriceTable/SalesPriceTableFGS', views.SalesPriceTableFGS, name="SalesPriceTableFGS"),
    path('Shop/SalesHomeIncome/SalesPriceTable/SalesPriceTableFGS/ShopPriceTableFGSUpdate', views.ShopPriceTableFGSUpdate, name="ShopPriceTableFGSUpdate"),
    
]

