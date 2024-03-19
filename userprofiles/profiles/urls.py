from django.urls import path
from profiles.views import SignUpView,SignInView,UserCreateView,UserListView,UserDetailView,\
    UserUpdateView,remove_user


urlpatterns=[
    path("",SignUpView.as_view(),name="signup"),
    path("signin",SignInView.as_view(),name="signin"),
    path("add/",UserCreateView.as_view(),name="add"),
    path("list/",UserListView.as_view(),name="listuser"),
    path("<int:pk>/",UserDetailView.as_view(),name="userdetail"),
    path("<int:pk>/change/",UserUpdateView.as_view(),name="useredit"),
    path("<int:pk>/remove/",remove_user,name="deleteuser")

    
]