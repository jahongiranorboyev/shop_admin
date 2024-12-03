from django.urls import path

from apps.users.views import UserListView, CreateUserView, UpdateUserView, UserEditView, UserDeleteView

app_name = 'users'
urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('edit/<uuid:pk>/', UserEditView.as_view(), name='user_edit'),
    path('delete/<uuid:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('profile-setting/', UpdateUserView.as_view(), name='profile_setting'),
]
