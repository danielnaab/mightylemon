from django import forms

from models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
    
    def save(self):
        super(ContactForm, self).save()
        
        # send the email
        self.instance.send_mail()
