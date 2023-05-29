from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.LoginUser.as_view(),name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/<slug:y>/',views.ProfileUser.as_view(),name='profile'),
    path('update/int:pk/',views.UpdateUser.as_view(),name='update'),
    path('change/<int:pk>/', views.ChangeUser.as_view(), name='change'),
    path('logout/',views.user_logout,name='logout'),
]