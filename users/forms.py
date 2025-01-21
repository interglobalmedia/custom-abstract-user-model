from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomChangeForm(UserChangeform):

    class Meta:
        model = CustomUser
        fields = ("email",)
