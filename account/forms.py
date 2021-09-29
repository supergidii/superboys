from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import fields
from phonenumber_field.formfields import PhoneNumberField
from referrals.widgets import ReferralWidget
from referrals.fields import ReferralField
from django.core.validators import RegexValidator


User=get_user_model()

class ReferralSignupForm(forms.Form):
     referral = ReferralField(widget=ReferralWidget())



       
class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'username',
                'class':'form_control'
            }
        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form_control'
            }
        )
    )



class SignUpForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Phone number must be entered in the format: '+254714726618'. Up to 13 digits allowed.")
    
    first_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'first_name',
                'class':'form_control'
            }
        )
    )

    last_name=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'last_name',
                'class':'form_control'
            }
        )
    )

    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'username',
                'class':'form_control'
            }
        )
    )

    phone_number=PhoneNumberField(validators=[phone_regex], max_length=17,
        widget=forms.TextInput(
            attrs={
                'placeholder':'phone_number',
                'class':'form_control'
            }
        )
    )

    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form_control'
            }
        )
    )

    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'confirm_password',
                'class':'form_control'
            }
        )
    )
    
    class Meta:
        model=User
        fields=('first_name','last_name','username','phone_number','password1','password2')