from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    new_token = models.CharField(max_length=50, default='', blank=True)
    ex_date = models.DateTimeField(null=True, blank=True)
    
# Create profile automatic when user craeted 
@receiver(post_save, sender=User)
def auto_add_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user = user)
        profile.save()  