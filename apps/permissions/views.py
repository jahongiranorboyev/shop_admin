from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from django.contrib.auth.models import Group, ContentType
from django.views.generic import CreateView, ListView

from apps.permissions.forms import AddGroupForm



class GroupListView(PermissionRequiredMixin,ListView):
    permission_required = 'permissions.view_group'
    model = Group
    template_name = 'pages/all_groups.html'
    context_object_name = 'permissions'



class CreateGroupView(PermissionRequiredMixin,CreateView):
    permission_required = 'permissions.add_group'
    model = Group
    form_class = AddGroupForm
    template_name = 'pages/add-new-group.html'
    success_url = reverse_lazy('permissions:group_list')
    extra_context = {'content_types':ContentType.objects.exclude(
        model__in=['session','contenttype','group','permission','logentry']
    ).all().prefetch_related('permission_set')}
