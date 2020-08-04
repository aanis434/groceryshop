from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""

    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def clean_password2(self):
        # check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean(self):

        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                validate_password(password1, self.instance)
            except forms.ValidationError as error:
                self.add_error('password1', error)

    def save(self, commit=True):
        # save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users.Includes all the fields on the user,
    but replaces the password field with admin's password hash display field."""

    password = ReadOnlyPasswordHashField()
    new_password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(),
        required=False
    )
    new_password_confirmation = forms.CharField(
        label='New Password Confirmation',
        widget=forms.PasswordInput(),
        required=False
    )

    def clean_password(self):
        return self.initial["password"]

    def clean_new_password_confirmation(self):
        new_password = self.cleaned_data.get('new_password')
        new_password_confirmation = self.cleaned_data.get('new_password_confirmation')
        if new_password and new_password_confirmation and new_password != new_password_confirmation:
            raise forms.ValidationError("Passwords don't match")

        return new_password_confirmation

    def clean(self):
        password = self.cleaned_data['new_password']

        if password:
            try:
                validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('new_password', error)

    def save(self, commit=True):
        # save the provided password in hashed format
        user = super().save(commit=False)

        if self.cleaned_data['new_password'] and self.cleaned_data['new_password'] is not None:
            print('here')
            user.set_password(self.cleaned_data['new_password'])

        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'active', 'admin',)

