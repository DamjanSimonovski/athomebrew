from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Courses


# from .models import Courses


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class CourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Courses
        exclude = ("author",)
