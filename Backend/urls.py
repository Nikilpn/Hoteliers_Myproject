from django.urls import path,include
from Backend import views
urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('roomtype_page/', views.roomtype_page, name="roomtype_page"),
    path('save_roomtype_page/', views.save_roomtype_page, name="save_roomtype_page"),
    path('display_roomtype_page/', views.display_roomtype_page, name="display_roomtype_page"),
    path('edit_roomtype_page/<int:prop_id>/', views.edit_roomtype_page, name="edit_roomtype_page"),
    path('update_roomtype_page/<int:prop_id>/', views.update_roomtype_page, name="update_roomtype_page"),
    path('delete_page/<int:del_id>/', views.delete_page, name="delete_page"),

# #.............hotel pages..............
    path('room_number_page/', views.room_number_page, name="room_number_page"),
    path('save_room_number_page/', views.save_room_number_page, name="save_room_number_page"),
    path('display_room_number_page/', views.display_room_number_page, name="display_room_number_page"),
    path('edit_room_number_page/<int:Edit_id>/', views.edit_room_number_page, name="edit_room_number_page"),
    path('update_room_number_page/<int:prop_id>/', views.update_room_number_page, name="update_room_number_page"),
    path('delete_room_number_page/<int:del_id>/', views.delete_room_number_page, name="delete_room_number_page"),

#lOGIN MAIN
    path('login_page_admin/', views.login_page_admin, name="login_page_admin"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),


##Displaying Webapp(customersendingcontactmessage) in to Backend (8customercontacthtml page)
#connecting Webapp(db) and Backend
    path('contact_details_page/', views.contact_details_page, name="contact_details_page"),
    path('delete_customer_contact_details_page/<int:del_id>/', views.delete_customer_contact_details_page, name="delete_customer_contact_details_page"),

#adding staff details
    path('staff_details_page/', views.staff_details_page, name="staff_details_page"),
    path('save_staff_page/', views.save_staff_page, name="save_staff_page"),
    path('display_staff_page/', views.display_staff_page, name="display_staff_page"),
    path('edit_STAFF_page/<int:Edit_id>/', views.edit_STAFF_page, name="edit_STAFF_page"),
    path('update_staff_page/<int:prop_id>/', views.update_staff_page, name="update_staff_page"),
    path('delete_staff_page/<int:del_id>/', views.delete_staff_page, name="delete_staff_page"),

    #details of room booked people
    path('detailsbooked_page/', views.detailsbooked_page, name="detailsbooked_page"),
    path('deletebooked_details/<int:del_id>/', views.deletebooked_details, name="deletebooked_details"),


#total amount of moneypayed by customer (displaypage)
    path('customertotalamount_page/', views.customertotalamount_page, name="customertotalamount_page"),
    path('deletecustomertotalamount_page/<int:del_id>/', views.deletecustomertotalamount_page, name="deletecustomertotalamount_page"),


]