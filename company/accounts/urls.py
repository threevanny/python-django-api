from .views import SignUpView,Update_ProfileView,LoginView,LogoutView
from django.urls import path, include  # new




urlpatterns = [

    path('accounts/login/', LoginView.as_view(), name='login'),#overriding login url of default auth app.
    path('signup', SignUpView.as_view(), name='sign-up'),
    path('profile/<int:pk>/',Update_ProfileView.as_view(), name='profile'),
    path ('accounts/logout/',LogoutView.as_view() , name='logout'),#overriding logout url of default auth app.
    path('accounts/', include('django.contrib.auth.urls')),#Adding the url of default auth app to use it

]





