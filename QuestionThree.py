"""Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
"""


from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    print("Signal received. Raising an exception to trigger rollback.")
    raise Exception("Error in signal.")

try:
    with transaction.atomic():
        user = User(username='shreesh')
        user.save()  # This will trigger the signal
        print("User saved successfully.")
except Exception as e:
    print(f"Transaction rolled back due to: {e}")
