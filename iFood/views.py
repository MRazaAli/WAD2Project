from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.http import HttpResponse
from iFood.forms import UserForm, UserProfileForm, UserProfileEditForm, UserDetailsForm
from iFood.forms import FeedbackForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User


def index(request):
   context_dict = {'boldmessage' : "Eats whatever you want! "}
   response = render(request, 'iFood/index.html',context = context_dict)
   return response

def about(request):
   context_dict = {'boldmessage' : "Welcome "}
   response = render(request, 'iFood/about.html',context = context_dict)
   return response

def signup(request):
   registered = False
   if request.method == 'POST':
      user_form = UserForm(data=request.POST)
      profile_form = UserProfileForm(data=request.POST)
      if user_form.is_valid() and profile_form.is_valid():
         user = user_form.save()
         user.set_password(user.password)
         user.save()
         profile = profile_form.save(commit=False)
         profile.user = user
         profile.save()
         registered = True
         login(request,user)
      else:
         print(user_form.errors, profile_form.errors)

   else:
      user_form = UserForm()
      profile_form = UserProfileForm()
      
   return render(request, 'iFood/signup.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

@login_required
def edit_profile(request):
    user = request.user
    form = UserDetailsForm(request.POST or None, instance=user)
    prof = UserProfileEditForm(request.POST or None, instance=user.userprofile)
    if request.method == 'POST':
        if form.is_valid() and prof.is_valid():
            # Save the changes but password
            form.save()
            prof.save()
            # Change password
            new_password = form.cleaned_data.get('password')
            if new_password:
                user.set_password(new_password)
            messages.info(request, 'Your new details and password were saved!')
            return HttpResponseRedirect(reverse('account'))
    context = {"form": form, "prof":prof,}

    return render(request, "iFood/user-account.html", context) 
                 
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account has been disabled!")
        else:
            messages.info(request,'Invalid login details supplied. Please try again or sign up.')
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'iFood/login.html', {})

@login_required     
def user_logout(request):
   logout(request)
   return HttpResponseRedirect(reverse('index'))

@login_required
def web_feedback(request):
   if request.method == 'POST':
       feedback_form = FeedbackForm(request.POST)
       if feedback_form.is_valid():
          feedback = feedback_form.save()
          feedback.save()
          messages.info(request, 'Your feedback is very valuable for us! Thanks for submitting.')
          return redirect('web-feedback')
   else:
       feedback_form = FeedbackForm()
   return render(request, 'iFood/web-feedback.html',{'feedback_form':feedback_form})
   

def contact(request):
    return render(request, 'iFood/contact.html',{})
