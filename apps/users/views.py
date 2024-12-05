from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.users.forms import AddUserForm, UserForm


class UserListView(PermissionRequiredMixin, ListView):
    permission_required = 'users.view_user'
    model = get_user_model()
    ordering = ['username']
    paginate_by = 10
    template_name = 'pages/all-users.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        return queryset


class CreateUserView(PermissionRequiredMixin, CreateView):
    permission_required = 'users.add_user'
    model = get_user_model()
    form_class = AddUserForm
    template_name = 'pages/add-new-user.html'
    success_url = reverse_lazy('users:user_list')


class UserEditView(PermissionRequiredMixin, UpdateView):
    permission_required = 'users.change_user'
    model = get_user_model()
    form_class = UserForm
    template_name = 'pages/user_edit.html'
    context_object_name = 'user'

    def form_valid(self, form):
        user = form.save(commit=False)

        password = form.cleaned_data.get('password')
        if password:
            user.set_password(password)

        user.save()

        groups = form.cleaned_data.get('groups')
        user.groups.set(groups)
        return redirect('users:user_list')

    def get_success_url(self):
        return reverse_lazy('users:user_list')


class UserDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'users.delete_user'
    model = get_user_model()
    template_name = 'pages/user_confirm_delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users:user_list')

    def get_success_url(self):
        if not self.model.objects.exists():
            return reverse_lazy('login')
        return reverse_lazy('users:user_list')


class UpdateUserView(PermissionRequiredMixin, UpdateView):
    permission_required = 'users.change_user'
    model = get_user_model()
    template_name = 'pages/profile-setting.html'
