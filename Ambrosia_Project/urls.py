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

    path('Shop/InventoryHome', views.inventoryhome, name="inventoryhome"),

    path('Shop/InventoryHome/addCategoryProduct', views.addCategoryProduct, name="addCategoryProduct"),
    path('Shop/InventoryHome/updateategoryProduct', views.updateategoryProduct, name="updateategoryProduct"),
    path('Shop/InventoryHome/viewCategoryProduct', views.viewCategoryProduct, name="viewCategoryProduct"),
    path('Shop/InventoryHome/deleteCategoryProduct', views.deleteCategoryProduct, name="deleteCategoryProduct"),


    path('Shop/InventoryHome/addteapackets', views.addteapackets, name="addteapackets"),
    path('Shop/InventoryHome/addteapackets/editpackets', views.editpackets, name="editpackets"),
    path('Shop/InventoryHome/addteapackets/Updatepackets', views.updatePackets, name="updatepackets"),
    path('Shop/InventoryHome/addteapackets/deletepackets', views.deletepackets, name="deletepackets"),
    path('Shop/InventoryHome/viewpackets', views.viewpackets, name="viewpackets"),

    path('Shop/InventoryHome/availableStock', views.availableStock, name="availableStock"),

    path('Shop/InventoryHome/inventoryreports', views.inventoryreports, name="inventoryreports"),
    path('Shop/InventoryHome/inventoryreports/weeklyreport', views.iweekly, name="iweekly"),
    path('Shop/InventoryHome/inventoryreports/inventorymonthlyreport', views.inventorymonthlyreport, name="monthlyreport"),
    path('Shop/InventoryHome/inventoryreports/inventoryannualreport', views.inventoryannualreport, name="annualreport"),

]

