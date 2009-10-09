from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from natty.forms import ContactForm
from natty.models import Contact

def contact(request, template_name='natty/contact.html'):
    success = None
    flash_message = None
    if request.POST:
        form = ContactForm(request.POST, instance=Contact())
        if form.is_valid():
            form.save()
            redirect_url = reverse(contact, kwargs={}) + '?result=success'
            return HttpResponseRedirect(redirect_url)
    else:
        if request.GET:
            success = request.GET.get('result', None)
            if success:
                flash_message = "Your message has been successfully sent.  I'll be in contact with you shortly!"
        form = ContactForm()
    
    return render_to_response(template_name, {
        'contact_form': form,
        'success': success,
        'flash_message': flash_message,
    }, context_instance=RequestContext(request))

def projects(request, template_name):
    return render_to_response(template_name, {
    }, context_instance=RequestContext(request))