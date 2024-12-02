from django.db import models
from apps.utils.models.base_model import AbstractBaseModel
from django.conf import settings


class Ticket(AbstractBaseModel):
    """
    Model representing support or inquiry tickets raised by users.

    Fields:
        - user: A foreign key linking the ticket to the user who raised it.
        - comment: An optional comment or description of the ticket, up to 500 characters.
        - subject: The subject or title of the ticket, with a maximum length of 100 characters.
        - status: A boolean field indicating whether the ticket is open (False) or closed (True).
        - created_at: The timestamp when the ticket was created.

    Methods:
        - __str__: Returns the subject of the ticket (first 30 characters) as a string representation.
    """
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject[:30]

