from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your models here.

# class Admin_Members(models.Model):

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     admin_img = models.ImageField(upload_to='Admin_Img')
#     admin_name = models.CharField(max_length=50)
#     admin_desc = models.CharField(max_length=250)
#     admin_date = models.DateField(auto_now = True)
#     admin_time = models.TimeField(auto_now = True)

#     class Meta:
#         db_table = 'hotel_admin_table'



class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='ProfilePhotos', null=True)
    bg_img = models.ImageField(upload_to='BGPhotos', null=True)
    name = models.CharField(max_length=50, null=True)
    desc = models.CharField(max_length=250, null=True)
    date = models.DateField(auto_now = True)
    time = models.TimeField(auto_now = True)

    class Meta:
        db_table = 'hotel_profile_table'



class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booker_address = models.CharField(max_length=150, null=True)
    extra_members = models.CharField(max_length=250, null=True)
    booker_mobile = models.PositiveIntegerField(null=True)
    booking_occasion = models.CharField(max_length=200, null=True)
    booking_date = models.DateField(null=True)
    booking_time = models.TimeField(null=True)
    datestamp = models.DateField(auto_now=True)
    timestamp = models.TimeField(auto_now = True)

    class Meta:
        db_table = 'hotel_booking_table'



class ChatRoom(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=150, null=True)
    chatImage = models.ImageField(upload_to='Chat Media', null=True)
    chat_date = models.DateField(auto_now = True)
    chat_time = models.TimeField(auto_now = True)

    class Meta:
        db_table = 'hotel_chat_table'



class PostModel(models.Model):

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to='Post Pics')
    post_caption = models.CharField(max_length=300)
    post_hashtags = models.CharField(max_length=60)
    post_date = models.DateField(auto_now = True)
    post_time = models.TimeField(auto_now = True)

    class Meta:
        db_table = 'hotel_post_table'