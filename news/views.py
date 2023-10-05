from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from news.models import ContactModel
from news.forms import ContactForm

class ContactUsView(SuccessMessageMixin,FormView):
    model = ContactModel
    template_name = 'news/contact.html'
    success_message = "Your response is submitted. We will get back to you soon."
    form_class = ContactForm
    success_url = '/contact/'