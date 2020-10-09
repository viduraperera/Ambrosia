from django.urls import path
from Ambrosia_Project.view_mappings import leafInventoryAndDailyProductionViews

urlpatterns = [

    path('DailyProduction', leafInventoryAndDailyProductionViews.NavigateToProduction, name="final_production_home"),
    path('AddMainProduction', leafInventoryAndDailyProductionViews.addMainFinalProduction, name="addMainFinalProduct"),
    path('deleteSubProdAll', leafInventoryAndDailyProductionViews.deleteSubProd, name="deleteSubProdAll"),
    path('CustomDailyProduction', leafInventoryAndDailyProductionViews.NavigateToCustomDailyProd, name="NavigateToCustomDailyProd"),
    path('CustomDailyProduction/subDel', leafInventoryAndDailyProductionViews.NavigateToDelSubPr, name="delete_sub"),
    path('CustomDailyProduction/ViewProduct', leafInventoryAndDailyProductionViews.NavigateToViewProduct, name="NavigateToViewProd"),
    path('TeaGrades', leafInventoryAndDailyProductionViews.NavigateToTeaGrades, name="NavigateToTeaGrades"),
    path('TeaGrades/Delete', leafInventoryAndDailyProductionViews.DeleteGrade, name="deleteGrade"),

]