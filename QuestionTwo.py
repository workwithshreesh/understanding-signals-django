"""
Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
"""

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

# Simulate saving a user instance
print(f"Main thread: {threading.current_thread().name}")
user = User(username='shreesh')
user.save()
