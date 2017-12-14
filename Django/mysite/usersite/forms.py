from django import forms

from usersite import models

class NameForm(forms.Form):
    lastname = forms.CharField(label='Last name', max_length=100)
    firstname = forms.CharField(label='First name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    usertype = forms.CharField(label='User type')

class UserReportForm(forms.Form):
    usertype = forms.CharField(label='User type')