from . import views
from django.urls import path, include
from .views import *

urlpatterns = [

    path('', views.home, name="home"),

#---------User Profile------------------------------------------------------
    path('AddUser', views.registration, name='register'),
    path('ViewAllUsers', views.view_AllUsers, name="view_all_users"),
    path('ViewAllUsers/EditUser', views.ShowUser, name="update_user"),
    path('ViewAllUsers/UpdateUserdetails', views.UpdateUser, name="update_user_details"),
    path('ViewAllUsers/', views.DeleteUser, name="delete_user"),


#---------Main menues-----------------------------------------------------
    path('Factory', views.factoryhome, name='factory_home'),
    path('Shop', views.teashopHomepage, name='teashop_home'),


#---------final Production Auction------------------------------------------------------
    path('Factory/FinalProduction/AuctionStock/', include('Ambrosia_Project.url_mappings.finalProductionAuctionUrls')),


#---------final Production Daily Production----------------------------------------------------

    path('Factory/FinalProduction/', views.NavigateToProduction,name="final_production_home"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction', views.NavigateToCustomDailyProd,name="NavigateToCustomDailyProd"),
    path('Factory/FinalProduction/DailyProduction/CurrentDailyProduction', views.NavigateToCurrentProduct,name="NavigateToCurrentProd"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction/UpdateProduct', views.NavigateToUpdateProduct,name="NavigateToUpdateProd"),
    path('Factory/FinalProduction/DailyProduction/TeaGrades', views.NavigateToTeaGrades,name="NavigateToTeaGrades"),

    path('Factory/LeafInventory/AddInventory', views.NavigateToInventory, name="AddInventory"),
    path('Factory/LeafInventory/PreviousInventories', views.NavigateToPrevInv, name="NavigateToPreInv"),
    path('Factory/LeafInventory/PreviousInventories/UpdateInvenories', views.NavigateToUpdateInv,
         name="NavigateToUpdateInv"),
    path('Factory/LeafInventory/PreviousInventories/deleteLeaf', views.DeleteLeaf, name="delete_leaf"),
    path('Factory/LeafInventory/AddInventory/leafAdd', views.LeafInvAdd, name="LeafInvAdd"),
    path('Factory/LeafInventory/PreviousInventories/updateLeaf', views.updateLeaf, name="updateLeaf"),
    path('Factory/LeafInventory/PreviousInventories/InventoryReport', views.NavigateToInvReport,
         name="NavigateToInvReport"),

    path('Factory/FinalProduction/DailyProduction', views.NavigateToProduction, name="final_production_home"),
    path('Factory/FinalProduction/DailyProduction/AddMainProduction', views.addMainFinalProduction,
         name="addMainFinalProduct"),
    path('Factory/FinalProduction/DailyProduction/deleteSubProdAll', views.deleteSubProd, name="deleteSubProdAll"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction', views.NavigateToCustomDailyProd,
         name="NavigateToCustomDailyProd"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction/subDel', views.NavigateToDelSubPr,
         name="delete_sub"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction/ViewProduct', views.NavigateToViewProduct,
         name="NavigateToViewProd"),
    path('Factory/FinalProduction/DailyProduction/TeaGrades', views.NavigateToTeaGrades, name="NavigateToTeaGrades"),
    path('Factory/FinalProduction/DailyProduction/TeaGrades/Delete', views.DeleteGrade, name="deleteGrade"),

]

