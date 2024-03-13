from django.urls import path
from .views import *



urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogOutUserView.as_view(), name='logout'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('pasword-change/', UserChangePaswordView.as_view(), name='pasword-change'),

]