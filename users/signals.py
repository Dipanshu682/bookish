from django.conf import settings
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.utils.timezone import now
from .models import Profile


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = "Welcome to Book Marketplace"
        message = (
            f"Hi {instance.username}, thank you for registering at Book Marketplace."
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)
        print(f"Welcome email sent to {instance.email}")


@receiver(user_logged_in)
def update_last_login(sender, user, request, **kwargs):
    user.profile.last_login = now()
    user.profile.save()
    print(f"User {user.username} logged in at {now()}")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
