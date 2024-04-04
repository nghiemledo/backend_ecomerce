from django.urls import path
from users import views

urlpatterns = [ 
    path('users/profile/', views.UserAccountUpdateView.as_view(), name='profile') 
]