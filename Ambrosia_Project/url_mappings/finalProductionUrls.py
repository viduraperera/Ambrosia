from django.urls import path
from Ambrosia_Project.view_mappings import finalProductionAuctionViews
from Ambrosia_Project.view_mappings.finalProductionAuctionViews import ReportAuctionSoldStock

urlpatterns = [

    path('Factory/FinalProduction/AddSubAuctionStock', finalProductionAuctionViews.addAuctionSubStock, name="prepare_auction_stock"),
    path('Factory/FinalProduction/DeleteAuctionSubStock', finalProductionAuctionViews.deleteAuctionSubStock, name="delete_subStock"),
    path('Factory/FinalProduction/AddMainAuctionStock', finalProductionAuctionViews.addMainAuctionStock, name="add_mainStock"),
    path('Factory/FinalProduction/AfterAddAuctionSubStock', finalProductionAuctionViews.afterAddAuctionSubStock, name="after_add_subStock"),
    path('Factory/FinalProduction/AllAuctionMainStocks', finalProductionAuctionViews.showAuctionMainStocks, name="all_catelog"),
    path('Factory/FinalProduction/ViewMainStock', finalProductionAuctionViews.showMainAuctionStock, name="view_mainStock"),
    path('Factory/FinalProduction/viewAuctionSubstock', finalProductionAuctionViews.viewAuctionSubStock, name="view_UpdatesubStock"),
    path('Factory/FinalProduction/UpdateAuctionSubStockdetails', finalProductionAuctionViews.updateAuctionSubStock, name="update_subStock"),


    path('Factory/FinalProduction/AddNotSoldToCurrentCatelog', finalProductionAuctionViews.addNotSoldToCurrentCatelog, name="addNotSold_currentCatelog"),


    path('Factory/FinalProduction/StockSales', finalProductionAuctionViews.stockSalesHome, name="stock_sales"),
    path('Factory/FinalProduction/SoldStocks', finalProductionAuctionViews.soldStock, name="stock_sold"),
    path('Factory/FinalProduction/ViewAddToSoldStock', finalProductionAuctionViews.viewAddSoldStock,name="view_addSoldStock"),
    path('Factory/FinalProduction/AddSoldStock', finalProductionAuctionViews.AddSoldStock, name="add_SoldStock"),
    path('Factory/FinalProduction/ViewSoldStock', finalProductionAuctionViews.showSoldAuctionSubStock, name="view_soldStock"),
    path('Factory/FinalProduction/UpdateSoldStock', finalProductionAuctionViews.updateSoldAuctionSubStock, name="update_soldStock"),
    path('Factory/FinalProduction/MoveSoldStock', finalProductionAuctionViews.moveToNotSoldAuctionSubStock, name="moveto_NotsoldStock"),
    path('Factory/FinalProduction/ViewNotSoldStocks', finalProductionAuctionViews.notSoldStock, name="stock_notsold"),
    path('Factory/FinalProduction/NotSoldStockAdd', finalProductionAuctionViews.NotSoldStockAdd, name="add_NotSoldStock"),
    path('Factory/FinalProduction/NotSoldStockDelete', finalProductionAuctionViews.DeleteNotSoldStock, name="delete_NotSoldStock"),
    path('Factory/FinalProduction/ViewAuctionNotSoldLog', finalProductionAuctionViews.showAuctionNotSoldLog, name="stock_notsoldlog"),


    path('Factory/FinalProduction/SearchAuctionMainStock', finalProductionAuctionViews.searchAuctionMainStock, name="search_mainStock"),
    path('Factory/FinalProduction/SearchAuctionCurrentSubStock', finalProductionAuctionViews.searchAuctionCurrentSubStock, name="search_currentSubStock"),
    path('Factory/FinalProduction/SearchAuctionSoldStock', finalProductionAuctionViews.searchAuctionSoldStock, name="search_soldStock"),
    path('Factory/FinalProduction/AuctionStock/Brokers', finalProductionAuctionViews.showBrokerDetails, name="all_brokers"),
    path('Factory/FinalProduction/AuctionStock/AddBroker', finalProductionAuctionViews.addNewBroker, name="add_broker"),
    path('Factory/FinalProduction/AuctionStock/UpdateBroker', finalProductionAuctionViews.updateBroker, name="update_broker"),
    path('Factory/FinalProduction/AuctionStock/ShowBroker', finalProductionAuctionViews.showBroker, name="show_broker"),
    path('Factory/FinalProduction/AuctionStock/DeleteBroker', finalProductionAuctionViews.deleteBroker, name="delete_broker"),


    path('Factory/FinalProduction/AuctionStock/Buyers', finalProductionAuctionViews.showBuyerDetails, name="all_buyers"),
    path('Factory/FinalProduction/AuctionStock/AddBuyer', finalProductionAuctionViews.addNewBuyer, name="add_buyer"),
    path('Factory/FinalProduction/AuctionStock/ShowBuyer', finalProductionAuctionViews.showBuyer, name="show_buyer"),
    path('Factory/FinalProduction/AuctionStock/UpdateBuyer', finalProductionAuctionViews.updateBuyer, name="update_buyer"),


    path('Factory/FinalProduction/AuctionStock/DeleteBuyer', finalProductionAuctionViews.deleteBuyer, name="delete_buyer"),


    path('Factory/FinalProduction/ProductionAnalysis/', finalProductionAuctionViews.productionAnalysisHome,name="production_analysis"),
    path('Factory/FinalProduction/ProductionAnalysis/GenerateSoldStockReport', ReportAuctionSoldStock.as_view(),name="generateSoldStockReport"),
    # path('Factory/FinalProduction/ProductionAnalysis/GenerateNot-SoldStockReport', ReportAuctionNotSoldStock.as_view() , name="generateNotSoldStockReport"),


]