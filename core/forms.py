from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Введите свое имя',"class":"px-4 py-5 w-full rounded-xl"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Введите пароль',"class":"px-4 py-5 w-full rounded-xl"}))

class SignupForm(UserCreationForm):
    class  Meta:
        model=User
        fields=['username','email', 'password1', 'password2']
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Введите свое имя',"class":"px-4 py-5 w-full rounded-xl"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Введите свой Email',"class":"px-4 py-5 w-full rounded-xl"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Введите пароль',"class":" my-5 px-4 py-5 w-full rounded-xl"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Повторите  пароль',"class":" my-5 px-4 py-5 w-full rounded-xl"}))
    
# this is the form for updating
        
