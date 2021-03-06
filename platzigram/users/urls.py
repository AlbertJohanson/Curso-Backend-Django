"""Users URLs"""

#Django
from django.urls import path

#Views 
from users import views

urlpatterns = [

    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    path(

        route='login/', 

        view=views.LoginView.as_view(), 

        name="login"),
                                    
    path(   

        route='logout/',

        view=views.LogoutView.as_view(), 

        name="logout"),

    path(

        route='signup/',

        view=views.UserSignUpView.as_view(), 

        name="signup"),

    path(

        route='me/profile/', 

        view=views.UserUpdateView.as_view(), 

        name="update_profile")
]