from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError


class AddUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'confirm_password', 'groups']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if get_user_model().objects.filter(username=username).exists():
            raise ValidationError('This username is already taken.')
        return username

    def clean_confirm_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Passwords do not match')
        return confirm_password

    def save(self, commit=True):
        # Hash password before saving user
        self.cleaned_data.pop('confirm_password')
        self.cleaned_data['password'] = make_password(self.cleaned_data['password'])

        user = super().save(commit=False)

        if commit:
            user.save()

        # Saving the group relations (ManyToManyField)
        self.save_m2m()

        return user

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = get_user_model()  # Foydalanuvchi modelini olish
        fields = ['username', 'email', 'first_name', 'last_name']