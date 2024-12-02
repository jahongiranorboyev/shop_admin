from django.urls import path

from apps.users.views import UserListView, CreateUserView, VendorListView, CreateVendorView, UpdateUserView

app_name = 'users'
urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('create/',CreateUserView.as_view(), name='create_user'),
    path('vendors/',VendorListView.as_view(), name='vendor_list'),
    path('vendor-create/',CreateVendorView.as_view(), name='vendor_create'),
    path('profile-setting/',UpdateUserView.as_view(), name='profile_setting'),
]
