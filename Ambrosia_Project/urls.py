from . import views
from django.urls import path, include

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


    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction', views.NavigateToCustomDailyProd,name="NavigateToCustomDailyProd"),
    path('Factory/FinalProduction/DailyProduction/CurrentDailyProduction', views.NavigateToCurrentProduct,name="NavigateToCurrentProd"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction/UpdateProduct', views.NavigateToUpdateProduct,name="NavigateToUpdateProd"),
    path('Factory/FinalProduction/DailyProduction/TeaGrades', views.NavigateToTeaGrades,name="NavigateToTeaGrades"),

    path('Factory/EmployeeHome', views.EmployeeHome, name="attendance_management"),
    path('Factory/S_AllRegisteredSuppliers', views.to_reg_suppliers, name="S_AllRegisteredSuppliers"),
    path('Factory/FinalProduction/', views.NavigateToProduction, name="final_production_home"),
    path('Factory/LeafInventory/AddInventory', views.NavigateToInventory, name="AddInventory"),


]

