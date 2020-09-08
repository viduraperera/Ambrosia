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

    path('Factory/FinalProduction', views.FinalProduction, name="final_production_home"),
    path('Factory/FinalProduction/AuctionStock/', views.AuctionStockHome, name="auction_stock"),
    path('Factory/FinalProduction/AuctionStock/AuctionStockdetails', views.ShowAuctionStock, name="all_catelog"),
    path('Factory/FinalProduction/AuctionStock/UpdateAuctionStockdetails', views.UpdateAuctionStock, name="update_catelog"),

    path('Factory/FinalProduction/AuctionStock/Brokers', views.ShowBrokerDetails, name="all_brokers"),
    path('Factory/FinalProduction/AuctionStock/AddBroker', views.AddNewBroker, name="add_broker"),
    path('Factory/FinalProduction/AuctionStock/UpdateBroker', views.UpdateBroker, name="update_broker"),

    path('Factory/FinalProduction/AuctionStock/Buyers', views.ShowBuyerDetails, name="all_buyers"),
    path('Factory/FinalProduction/AuctionStock/AddBuyer', views.AddNewBuyer, name="add_buyer"),
    path('Factory/FinalProduction/AuctionStock/UpdateBuyer', views.UpdateBuyer, name="update_buyer"),

    path('Factory/FinalProduction/StockSales', views.StockSalesHome, name="stock_sales"),
    path('Factory/FinalProduction/NotSoldStocks', views.NotSoldStock, name="stock_notsold"),
    path('Factory/FinalProduction/SoldStocks', views.SoldStock, name="stock_sold"),

    path('Factory/FinalProduction/ProductionAnalysis/', views.ProductionAnalysisHome, name="production_analysis"),

]

