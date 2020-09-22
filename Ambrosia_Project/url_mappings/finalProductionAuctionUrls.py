from django.urls import path
from Ambrosia_Project.view_mappings import finalProductionAuctionViews
from Ambrosia_Project.view_mappings.finalProductionAuctionViews import ReportAuctionSoldStock

urlpatterns = [

    path('AddSubAuctionStock', finalProductionAuctionViews.addAuctionSubStock, name="prepare_auction_stock"),
    path('DeleteAuctionSubStock', finalProductionAuctionViews.deleteAuctionSubStock, name="delete_subStock"),
    path('AddMainAuctionStock', finalProductionAuctionViews.addMainAuctionStock, name="add_mainStock"),
    path('AfterAddAuctionSubStock', finalProductionAuctionViews.afterAddAuctionSubStock, name="after_add_subStock"),
    path('AllAuctionMainStocks', finalProductionAuctionViews.showAuctionMainStocks, name="all_catelog"),
    path('ViewMainStock', finalProductionAuctionViews.showMainAuctionStock, name="view_mainStock"),
    path('viewAuctionSubstock', finalProductionAuctionViews.viewAuctionSubStock, name="view_UpdatesubStock"),
    path('UpdateAuctionSubStockdetails', finalProductionAuctionViews.updateAuctionSubStock, name="update_subStock"),


    path('AddNotSoldToCurrentCatelog', finalProductionAuctionViews.addNotSoldToCurrentCatelog, name="addNotSold_currentCatelog"),


    path('StockSales', finalProductionAuctionViews.stockSalesHome, name="stock_sales"),
    path('SoldStocks', finalProductionAuctionViews.soldStock, name="stock_sold"),
    path('ViewAddToSoldStock', finalProductionAuctionViews.viewAddSoldStock,name="view_addSoldStock"),
    path('AddSoldStock', finalProductionAuctionViews.AddSoldStock, name="add_SoldStock"),
    path('ViewSoldStock', finalProductionAuctionViews.showSoldAuctionSubStock, name="view_soldStock"),
    path('UpdateSoldStock', finalProductionAuctionViews.updateSoldAuctionSubStock, name="update_soldStock"),

    path('MoveSoldStock', finalProductionAuctionViews.moveToNotSoldAuctionSubStock, name="moveto_NotsoldStock"),

    path('ViewNotSoldStocks', finalProductionAuctionViews.notSoldStock, name="stock_notsold"),
    path('NotSoldStockAdd', finalProductionAuctionViews.NotSoldStockAdd, name="add_NotSoldStock"),
    path('NotSoldStockDelete', finalProductionAuctionViews.DeleteNotSoldStock, name="delete_NotSoldStock"),
    path('ViewAuctionNotSoldLogDetails', finalProductionAuctionViews.showAuctionNotSoldLog, name="stock_notsoldlog"),
    path('ViewAuctionNotSoldLog', finalProductionAuctionViews.viewNotSoldLog, name="viewNotSoldLog"),


    path('SearchAuctionMainStock', finalProductionAuctionViews.searchAuctionMainStock, name="search_mainStock"),
    path('SearchAuctionCurrentSubStock', finalProductionAuctionViews.searchAuctionCurrentSubStock, name="search_currentSubStock"),
    path('SearchAuctionSoldStock', finalProductionAuctionViews.searchAuctionSoldStock, name="search_soldStock"),
    path('SearchAuctionNotSoldStockDetails', finalProductionAuctionViews.searchAuctionNotSoldStockDetails, name="findNotSoldStockDetails"),


    path('Brokers', finalProductionAuctionViews.showBrokerDetails, name="all_brokers"),
    path('AddBroker', finalProductionAuctionViews.addNewBroker, name="add_broker"),
    path('UpdateBroker', finalProductionAuctionViews.updateBroker, name="update_broker"),
    path('ShowBroker', finalProductionAuctionViews.showBroker, name="show_broker"),
    path('DeleteBroker', finalProductionAuctionViews.deleteBroker, name="delete_broker"),


    path('Buyers', finalProductionAuctionViews.showBuyerDetails, name="all_buyers"),
    path('AddBuyer', finalProductionAuctionViews.addNewBuyer, name="add_buyer"),
    path('ShowBuyer', finalProductionAuctionViews.showBuyer, name="show_buyer"),
    path('UpdateBuyer', finalProductionAuctionViews.updateBuyer, name="update_buyer"),
    path('DeleteBuyer', finalProductionAuctionViews.deleteBuyer, name="delete_buyer"),


    path('ProductionAnalysis/', finalProductionAuctionViews.productionAnalysisHome,name="production_analysis"),
    path('ProductionAnalysis/GenerateSoldStockReport', ReportAuctionSoldStock.as_view(),name="generateSoldStockReport"),
    # path('Factory/FinalProduction/ProductionAnalysis/GenerateNot-SoldStockReport', ReportAuctionNotSoldStock.as_view() , name="generateNotSoldStockReport"),


]