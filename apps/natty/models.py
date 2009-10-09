from django.db import models
from django_extensions.db.models import TimeStampedModel

class Contact(TimeStampedModel):
    email_address = models.EmailField()
    name = models.CharField(max_length=128)
    
    message = models.TextField()
    
    def __unicode__(self):
        return '%s (%s)' % (self.name, self.email_address)
    
    def send_mail(self):
        from django.core.mail import send_mail
        from django.conf import settings
        from django.template.loader import render_to_string
        
        message = render_to_string('natty/mail/contact.txt', {'contact': self})
        addresses = [admin[1] for admin in settings.ADMINS]
        send_mail('Natty Nerd contact form submission', message, self.email_address, addresses, fail_silently=False)
