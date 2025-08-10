from django.contrib.auth.forms import UserCreationForm
from clients.models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "Email address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Password confirmation"