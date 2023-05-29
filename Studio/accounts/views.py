
from django.shortcuts import render, redirect,reverse
from .forms import *
from .models import *
from django.contrib.auth import login
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from  django.contrib.auth import logout
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView , UpdateView

# Create your views here.

class RegisterUser(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'form':self.form_class})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(email=data['email'],phone=data['phone'],f_name=data['f_name'],
                                            l_name=data['l_name'],create=datetime.now(),password=data['password_1'])
            login(request,user)
            return redirect('home:photo_list')
        return render(request,self.template_name,{'form':form})

class ProfileUser(DetailView):
    template_name = 'accounts/profile.html'
    context_object_name = 'users'
    slug_field = 'f_name'
    slug_url_kwarg = 'y'
    # pk_url_kwarg = 'id'

    def get_queryset(self,*args,**kwargs):
        queryset = User.objects.filter(id=self.request.user.id)
        return queryset

class UpdateUser(LoginRequiredMixin,UpdateView):
    template_name = 'accounts/update.html'
    fields = ['f_name','l_name']

    def get_queryset(self,*args,**kwargs):
        queryset = User.objects.filter(id=self.request.user.id)
        return queryset

    def get_success_url(self):
        return reverse('accounts:update',kwargs={'pk':self.request.user.id})


class LoginUser(auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(40)
        else:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(LoginUser, self).form_valid(form)

class ChangeUser(LoginRequiredMixin,auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'accounts/change.html'
    success_url = reverse_lazy('accounts:login')

def user_logout(request):
    logout(request)
    messages.success(request,'با موفقیت خارج شدید','success')
    return redirect('home:photo_list')
