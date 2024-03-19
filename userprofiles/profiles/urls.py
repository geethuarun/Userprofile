from django.urls import path
from profiles.views import SignUpView,SignInView


urlpatterns=[
    path("",SignUpView.as_view(),name="signup"),
    path("/signin",SignInView.as_view(),name="signin")
    
]