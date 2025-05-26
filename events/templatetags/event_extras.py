from django import template
from events.models import Ticket
from django.contrib.auth.models import AnonymousUser

register = template.Library()

@register.filter
def user_has_ticket(event, user):
    if isinstance(user, AnonymousUser):
        return False  # User not logged in, can't have ticket
    return Ticket.objects.filter(event=event, user=user).exists()
