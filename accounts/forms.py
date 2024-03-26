from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):  # usercreation form -> signup
    class Meta:  #another forms dosent know about my custom model so i should tell them -> model=CustomModel
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)   #fields that inheritence of UserCreationForm have everything so i add my new field +('age',)
        fields = ('username', 'age', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'age', 'email',)
