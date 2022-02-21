from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import User


from users.tasks import send_welcome_email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_welcome_email_to_new_user(sender, instance, created, **kwargs):
    user = instance

    if created:
        send_welcome_email.delay(user.email, user.name)
