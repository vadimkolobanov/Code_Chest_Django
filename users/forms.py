import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save()
    #     user.is_active = False
    #     salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:6]
    #     user.activation_key = hashlib.sha1((user.email + salt).encode('utf-8')).hexdigest()
    #     user.save()
    #     return user
