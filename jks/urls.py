from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login_index, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),

    path('', views.index, name='index'),
    path('our_team/', views.team, name='team'),
    path('hotel_gallary/', views.gallary, name='gallary'),
    path('user_profile/<int:id>', views.profile, name='profile'),
    path('hotel_booking/', views.booking, name='booking'),
    path('contact_team/', views.contact, name='contact'),
    path('about_us/', views.about, name='about'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    # path('friends_profile/<int:id>', views.friends_profile, name='friends_profile'),
]
