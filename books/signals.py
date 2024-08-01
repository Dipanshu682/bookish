from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book


@receiver(post_save, sender=Book)
def log_book_addition(sender, instance, created, *args, **kwargs):
    if created:
        print(f'Book "{instance.title}" by {instance.author} was added.')


@receiver(post_save, sender=Book)
def log_book_change(sender, instance, created, *args, **kwargs):
    if created:
        print(f'Book "{instance.title}" by {instance.author} was added.')
    else:
        print(f'Book "{instance.title}" by {instance.author} was updated.')
