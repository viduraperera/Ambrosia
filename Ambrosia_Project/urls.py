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
    path('Factory/LeafInventory/AddInventory', views.NavigateToInventory, name="AddInventory"),
    path('Factory/LeafInventory/PreviousInventories', views.NavigateToPrevInv, name="NavigateToPreInv"),
    path('Factory/LeafInventory/PreviousInventories/UpdateInvenories', views.NavigateToUpdateInv, name="NavigateToUpdateInv"),

    path('Factory/FinalProduction/DailyProduction/AddProduction', views.NavigateToProduction, name="NavigateToProduction"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction', views.NavigateToCustomDailyProd, name="NavigateToCustomDailyProd"),
    path('Factory/FinalProduction/DailyProduction/CurrentDailyProduction', views.NavigateToCurrentProduct, name="NavigateToCurrentProd"),
    path('Factory/FinalProduction/DailyProduction/CustomDailyProduction/UpdateProduct', views.NavigateToUpdateProduct, name="NavigateToUpdateProd"),



]

