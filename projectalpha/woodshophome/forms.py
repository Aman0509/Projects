from django import forms

class ForgotPassword(forms.Form):
    username=forms.CharField(label='Username')
    mobile_number=forms.IntegerField(help_text='Enter your registered mobile number', label='Mobile number')

class CapturePassword(forms.Form):
    password1=forms.CharField(min_length=8,label="New Password")
    password2=forms.CharField(min_length=8,label="Confirm new Password")