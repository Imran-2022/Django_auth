from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.sign_up,name='sign_up'),
    path('login/', views.user_login,name='login'),
    path('', views.home,name='home'),
    path('profile/', views.profile,name='profile'),
    path('logout/', views.user_logout,name='logout'),

]
