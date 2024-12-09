from django.contrib.auth.models import Permission
from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

@receiver((post_save,pre_save), sender = Permission)
def permission_post_save_delete(sender, instance, **kwargs):
    cache.delete_pattern('permission_user_')