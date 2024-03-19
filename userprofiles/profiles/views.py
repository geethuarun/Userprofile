from django.shortcuts import render,redirect
from profiles.forms import RegistrationForm,LoginForm,UserCreateForm,UserChangeForm
from django.views.generic import View,CreateView,ListView,DetailView,UpdateView
from profiles.models import Users
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request,"registration.html",{"form":form})
        

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("add")
            else:
                return render(request,"login.html",{"form":form})
            

class UserCreateView(CreateView):
    
    template_name="useradd.html"
    form_class=UserCreateForm
    model=Users
    success_url=reverse_lazy("listuser")

class UserListView(ListView):
    template_name="userlist.html"
    context_object_name="users"
    model=Users
    def get_queryset(self):
        qs=Users.objects.all().order_by('name')
        return qs
    

class UserDetailView(DetailView):
    template_name="userdetail.html"
    context_object_name="user"
    model=Users


class UserUpdateView(UpdateView):
    template_name="userupdate.html"
    form_class=UserChangeForm
    model=Users
    success_url=reverse_lazy("listuser")

def remove_user(request,*args,**kwargs):
    id=kwargs.get("pk")
    Users.objects.filter(id=id).delete()
    return redirect("listuser")


    
