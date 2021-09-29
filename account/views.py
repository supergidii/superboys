from django.core.mail import message
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.contrib import messages


from .models import Profile
from .forms import LoginForm, SignUpForm

from django.conf import settings
from .decorators import auth_user_should_not_access
from django.contrib.auth import authenticate, login, logout

from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.contrib.auth import get_user_model
from referrals.signals import create_multi_level_referral

# create_flat_referral.send(sender=User, request, user, 'position')


User = get_user_model()

# Create your views here

@auth_user_should_not_access
def Login(request):
    form = SignUpForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, '⚠️ Invalid credentials, try again')
            return render(request, 'account/Login.html')

        login(request, user)

        return redirect(reverse('account:Dashboard'))

    return render(request, 'account/Login.html', {'form':form})

@auth_user_should_not_access
def Register(request):
    form=SignUpForm()
    if request.method == "POST":
        context = {'has_error': False}
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number= request.POST.get('phone_number')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if len(password1) < 6:
            messages.error(request, '⚠️ Password should be at least 6 characters for greater security')
            return redirect('account:Register')

        if password1 != password2:
            messages.error(request, '⚠️ Password Mismatch! Your Passwords Do Not Match')
            return redirect('account:Register')

        if not username:
            messages.error(request, '⚠️ Username is required!')
            return redirect('account:Register')

        if User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Username is taken! Choose another one')

            return render(request, 'account/Register.html')
        
        if not phone_number:
            messages.error(request, '⚠️ Phone Number is required!')
            return redirect('account:Register')


        if Profile.objects.filter(phone_number=phone_number).exists():
            messages.error(request, '⚠️ Phone Number is taken! Choose another one')

            
            return render(request, 'account/Register.html')
        
    


        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,phone_number=phone_number)
        user.set_password(password1)
        user.save()

        if not context['has_error']:
            login(request,user)
            messages.success(request, '✅ your Registration is Successful')
            return redirect(reverse('account:Login'))

    return render(request, 'account/Register.html', {'form':form})
            
def Logout(request):
    
    logout(request)
    messages.success(request, '✅ Successfully Logged Out!')

    return redirect(reverse('account:Login'))

def Dashboard(request):
    return render(request, 'account/Dashboard.html')
