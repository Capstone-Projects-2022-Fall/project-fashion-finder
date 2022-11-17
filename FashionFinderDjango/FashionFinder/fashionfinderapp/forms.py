from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import authenticate as django_authenticate, login as django_login, logout as django_logout 

from django import forms
from django.contrib.auth.hashers import check_password
from django.db.models import Q

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    """
    A Sign-Up page for the app

    :param forms.ModelForm: Basic fields and associated data
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm = forms.CharField(label='Confirm', widget=forms.PasswordInput)

    class Meta:
        """
        An inner class for setting form fields
        """
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_password(self):
        """
        Return a password if both password inputs on registration page match.

        :param self: The Registration Form (current instance)
        :type self: form
        :return: password
        :rtype: str
        """
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords do not match")
        return password

    def save(self, commit=True):
        """
        If registration form is complete, adds new user to user database.
        Returns new user.

        :param self: The Registration Form (current instance)
        :param commit
        :type self: form
        :type commit: boolean
        :return: user
        :rtype: model
        """
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user



class UploadImgForPredMicroserviceForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
 
class SignInForm(forms.Form):
    """
    A login form for the app.

    :param forms.Form: A collection of fields and their data.
    :data field username: A user's identifier
    :type username: string
    :data field password: A user's verification method
    :type password: string

    """
 
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    go = forms.CharField(required=False, max_length=50, widget=forms.HiddenInput())
 
    def is_valid(self):
        """
        If the form is complete and user is found, login procedes. Returns a boolean.

        :param self: The Signin Form (current instance)
        :type self: form
        :variable: valid: checks if the form has errors.
        :type valid: boolean
        :
        """
        valid = super(SignInForm, self).is_valid()
 
        if not valid:
            return valid
 
        try:
            user = User.objects.get(
                Q(username=self.cleaned_data['username']) | Q(email=self.cleaned_data['username'])
            )
 
        except User.DoesNotExist:
            self._errors['no_user'] = 'User does not exist'
            return False
 
        if not check_password(self.cleaned_data['password'], user.password):
            self._errors['invalid_password'] = 'Password is invalid'
            return False
 
        return True
