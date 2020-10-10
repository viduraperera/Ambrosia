from . import views
from django.urls import path, include
from .views import *
from django.conf.urls import url


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


#---------final Production Auction- Sandun -----------------------------------------------------
    path('Factory/FinalProduction/AuctionStock/', include('Ambrosia_Project.url_mappings.finalProductionAuctionUrls')),


#---------Leaf Inventory & Daily Production Ravija---------------------------------------------------
    path('Factory/LeafInventory/', include('Ambrosia_Project.url_mappings.leafInventoryUrls')),
    path('Factory/FinalProduction/', include('Ambrosia_Project.url_mappings.dailyProductionUrls')),

#---------Tea Shop Inventory Nethmi S--------------------------------------------------------------------------------------------------------------------
    path('Shop/InventoryHome', include('Ambrosia_Project.url_mappings.teaShopInventoryUrls')),

#---------Tea Shop Ssales Onella-------------------------------------------------------------------------------------------------------------------
    path('Shop/SalesHomeIncome', include('Ambrosia_Project.url_mappings.teaShopSalesUrls')),


]

