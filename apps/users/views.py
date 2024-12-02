from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, TemplateView


class UserListView(ListView):
    model = get_user_model()
    ordering = ['username']
    paginate_by = 10
    template_name = 'pages/all-users.html'
    context_object_name = 'users'
    def get_queryset(self):
        queryset = get_user_model().objects.all()
        return queryset


class CreateUserView(CreateView):
    model = get_user_model()
    fields = ['username', 'email']
    template_name = 'pages/add-new-user.html'


class VendorListView(ListView):
    model = get_user_model()
    template_name = 'pages/vendor-list.html'


class CreateVendorView(CreateView):
    model = get_user_model()
    template_name = 'pages/create-vendor.html'


class UpdateUserView(UpdateView):
    model = get_user_model()
    template_name = 'pages/profile-setting.html'
