from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import auth
import os
from .models import User,UserProfileInfo
from .forms import  UserCreateForm,UserProfileForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, request
from django.urls import reverse
from pathlib import Path
from django.contrib.auth.decorators import login_required
from django.views.generic import View
import pyautogui as pu

# Create your views here.
class SignUpView(View):
   model = User,UserProfileInfo
   #login_url = reverse_lazy('login')
   form_class = UserCreateForm
   template_name = "signup.html"

   def get(self, request, *args, **kwargs):
       form = self.form_class()
       return render(request, self.template_name, {'form': form})


   def post(self, request, *args, **kwargs):
       form = UserCreateForm(request.POST, request.FILES or None)


       if form.is_valid():
           # Cleaned(normalized) data
           city = form.cleaned_data.get('city')
           contact_no = form.cleaned_data.get('contactno')
           date_of_birth = form.cleaned_data.get('dob')
           password = form.cleaned_data.get('password')
           username = form.cleaned_data.get('username')
           email = form.cleaned_data.get('email')
           firstname = form.cleaned_data.get('first_name')
           lastname = form.cleaned_data.get('last_name')
           confirm_password = form.cleaned_data.get('confirm_password')
           image = form.cleaned_data.get('image')


           # check if the password match
           if password == confirm_password:
               if not User.objects.filter(email=email).exists():


                   if  User.objects.filter(username=username).exists():
                       pu.alert("Username already exists.Registration Failed.Try again.")
                       return redirect('sign-up')
                   else:
                       new_user = User.objects.create_user(username=username, password=password, email=email,
                                                           first_name=firstname, last_name=lastname)
                       new_user.save()
                       user= User.objects.get(username=username)
                       p_form = UserProfileForm()
                       p_form = p_form.save(commit=False)
                       p_form.user = user
                       p_form.dob = date_of_birth
                       p_form.username=username
                       p_form.city = city
                       p_form.contactno = contact_no
                       p_form.image = image
                       p_form.save()
                       pu.alert( text="New User Created Successfully",title="Success")
                       # Create UserProfile model

                       # logged in the user
                       login(request, new_user)
                       pu.alert( text="New User Loggedin susuccessfully",title="Success")                      
                       return redirect('home')
               else:
                   pu.alert('Registration Failed - Try different email address')
                   return redirect('sign-up')

           else:
               pu.alert("password and confirmpassword does not match.Try again")
               return redirect('sign-up')

       else:

           return render(request, self.template_name, {'form': form})



class LoginView(View):
    form_class = LoginForm
    redirect_authenticated_user = True
    model = UserProfileInfo

    def get(self, request, *args, **kwargs):  # GET Method
        form = self.form_class()
        return (render(request, 'registration/login.html', {'form': form}))  # Renders Login page

    def post(self, request, *args, **kwargs):  # POST Method
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']           
            
            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                if user.is_active and user.is_superuser:
                    if not User.objects.filter(username=username).exists():
                        new_userprofile= UserProfileInfo.objects.create(user=user,username=username, city= '',contactno='',dob='2010-05-25')
                        new_userprofile.save()# Creating userprofile record for superuser(admin)with default date
                    return redirect("/")  # Redirect to home page
       

                else:
                    if user.is_active:
                        return redirect("/") # Redirect to home page
                    else:
                        return redirect('login')  # Redirect to Login page

            else:
                pu.alert("Wrong Username or Password")
                return redirect('login')

        else:
            return render(request, 'registration/login.html', {'form': form})







class LogoutView(View):
    def get(self, request):
     logout(request)
     return HttpResponseRedirect('/')


@method_decorator(login_required, name='dispatch')
class Update_ProfileView(UpdateView):
    model = User, UserProfileInfo
    # login_url = reverse_lazy('login')
    form_class = UserProfileForm
    template_name = "userprofile.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
      if request.method == 'POST':
          form = UserProfileForm(request.POST, request.FILES or None)
          if form.is_valid():
              # Cleaned(normalized) data
              uId = form.cleaned_data.get('id')
              city = form.cleaned_data.get('city')
              username = form.cleaned_data.get('username')
              contact_no = form.cleaned_data.get('contactno')
              date_of_birth = form.cleaned_data.get('dob')
              image = form.cleaned_data.get('image')

              userprofile = UserProfileInfo.objects.get(username=username)

              userprofile.city = city
              userprofile.contactno = contact_no
              userprofile.dob = date_of_birth
              userprofile.image = image
              userprofile.save()
              pu.alert(text="New User Profile Updated Successfully", title="Success")
              return HttpResponseRedirect('/')


          else:
              pu.alert(text="Form is not valid.Date might be not in 'YYYY-MM-DD' Format", title="Error")

              return HttpResponseRedirect('/')

      else:
          return HttpResponseRedirect('/')













