"""
Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
"""

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    print("Signal received. Simulating delay...")
    time.sleep(5)  
    print("Signal execution completed.")

user = User(username='shreesh')
user.save()

print("User saved, but signal not completed yet.")
