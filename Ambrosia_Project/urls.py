from django.conf.urls import url
from django.urls import path
from . import views, admin
from .views import *


urlpatterns = [

    path('', views.home, name="home"),

    path('AddUser', views.registration, name='register'),
    path('ViewAllUsers', views.view_AllUsers, name="view_all_users"),
    path('ViewAllUsers/EditUser', views.ShowUser, name="update_user"),
    path('ViewAllUsers/UpdateUserdetails', views.UpdateUser, name="update_user_details"),
    path('ViewAllUsers/', views.DeleteUser, name="delete_user"),

    path('Factory', views.factoryhome, name='factory_home'),
    path('Shop', views.teashopHomepage, name='teashop_home'),


    path('Factory/LeafInventory/AddInventory', views.NavigateToInventory, name="AddInventory"),
    path('Factory/LeafInventory/PreviousInventories', views.NavigateToPrevInv, name="NavigateToPreInv"),
    path('Factory/LeafInventory/PreviousInventories/UpdateInvenories', views.NavigateToUpdateInv, name="NavigateToUpdateInv"),
    path('Factory/LeafInventory/PreviousInventories/deleteLeaf', views.DeleteLeaf, name="delete_leaf"),
    path('Factory/LeafInventory/AddInventory/leafAdd', views.LeafInvAdd, name="LeafInvAdd"),
    path('Factory/LeafInventory/PreviousInventories/updateLeaf', views.updateLeaf, name="updateLeaf"),
    path('Factory/LeafInventory/PreviousInventories/InventoryReport', views.NavigateToInvReport, name="NavigateToInvReport"),

    path('Factory/FinalProduction/DailyProduction', views.NavigateToProduction, name="final_production_home"),
    path('Factory/FinalProduction/DailyProduction/AddMainProduction', views.addMainFinalProduction, name="addMainFinalProduct"),
    path('Factory/FinalProduction/DailyProduction/deleteSubProdAll', views.deleteSubProd, name="deleteSubProdAll"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction', views.NavigateToCustomDailyProd, name="NavigateToCustomDailyProd"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction/subDel', views.NavigateToDelSubPr, name="delete_sub"),
    path('Factory/FinalProduction/DailyProduction/CurrentDailyProduction', views.NavigateToCurrentProduct, name="NavigateToCurrentProd"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction/ViewProduct', views.NavigateToViewProduct, name="NavigateToViewProd"),
    path('Factory/FinalProduction/DailyProduction/TeaGrades', views.NavigateToTeaGrades, name="NavigateToTeaGrades"),
    path('Factory/FinalProduction/DailyProduction/TeaGrades/Delete', views.DeleteGrade, name="deleteGrade"),


    path('Factory/FinalProduction/StockSales', views.StockSalesHome, name="stock_sales"),
    path('Factory/FinalProduction/NotSoldStocks', views.NotSoldStock, name="stock_notsold"),
    path('Factory/FinalProduction/SoldStocks', views.SoldStock, name="stock_sold"),


    path('Factory/FinalProduction/AuctionStock/', views.AuctionStockHome, name="auction_stock"),
    path('Factory/FinalProduction/AuctionStock/AuctionStockdetails', views.ShowAuctionStock, name="all_catelog"),
    path('Factory/FinalProduction/AuctionStock/UpdateAuctionStockdetails', views.UpdateAuctionStock,name="update_catelog"),

    path('Factory/FinalProduction/AuctionStock/Brokers', views.ShowBrokerDetails, name="all_brokers"),
    path('Factory/FinalProduction/AuctionStock/AddBroker', views.AddNewBroker, name="add_broker"),
    path('Factory/FinalProduction/AuctionStock/UpdateBroker', views.UpdateBroker, name="update_broker"),

    path('Factory/FinalProduction/AuctionStock/Buyers', views.ShowBuyerDetails, name="all_buyers"),
    path('Factory/FinalProduction/AuctionStock/AddBuyer', views.AddNewBuyer, name="add_buyer"),
    path('Factory/FinalProduction/AuctionStock/UpdateBuyer', views.UpdateBuyer, name="update_buyer"),
    path('Factory/FinalProduction/ProductionAnalysis/', views.ProductionAnalysisHome, name="production_analysis"),

]

