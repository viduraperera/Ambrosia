from django.urls import path
from Ambrosia_Project.view_mappings import leafInventoryAndDailyProductionViews

urlpatterns = [

    path('AddInventory', leafInventoryAndDailyProductionViews.NavigateToInventory, name="AddInventory"),
    path('PreviousInventories', leafInventoryAndDailyProductionViews.NavigateToPrevInv, name="NavigateToPreInv"),
    path('PreviousInventories/UpdateInvenories', leafInventoryAndDailyProductionViews.NavigateToUpdateInv,name="NavigateToUpdateInv"),
    path('PreviousInventories/deleteLeaf', leafInventoryAndDailyProductionViews.DeleteLeaf, name="delete_leaf"),
    path('AddInventory/leafAdd', leafInventoryAndDailyProductionViews.LeafInvAdd, name="LeafInvAdd"),
    path('PreviousInventories/updateLeaf', leafInventoryAndDailyProductionViews.updateLeaf, name="updateLeaf"),
    path('PreviousInventories/InventoryReport', leafInventoryAndDailyProductionViews.NavigateToInvReport, name="NavigateToInvReport"),

]