from django.urls import path

from apps.permissions.views import CreateGroupView, GroupListView

app_name = 'permissions'
urlpatterns = [
    path('groups/', GroupListView.as_view(), name='group_list'),
    path('group/add/', CreateGroupView.as_view(), name='add_group'),
]
