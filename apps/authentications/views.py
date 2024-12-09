from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class LoginPageView(TemplateView):
    template_name = 'auth/login.html'

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if user is not None:
            login(self.request, user)
            return redirect('home-page')
        return super().form_invalid(form)


    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = 'authentications:login'


class RegisterView(FormView):
    template_name = 'auth/sign-up.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('authentications:register-login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(self.request, "Your account has been created successfully!")
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form=form))



