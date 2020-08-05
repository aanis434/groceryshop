from django import forms


class LoginClientForm(forms.Form):
    email = forms.EmailField(max_length=60, label='Email Address', error_messages={
                             'required': "Enter email address"})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={
                               'required': "Enter password"})
