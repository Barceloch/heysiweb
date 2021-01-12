# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.utils.translation import ugettext as _
from heysiweb.forms import ContactForm
from django.core.mail import send_mail
from itemssite.models import HomePost, HomeService, Faq
from heysiweb.settings import DEFAULT_FROM_EMAIL, DEFAULT_TO_EMAIL

def home(request):
    homePosts = HomePost.objects.filter(language=request.LANGUAGE_CODE)
    homeServices = HomeService.objects.filter(language=request.LANGUAGE_CODE)
    return render_to_response('index.html', dict(hposts=homePosts, hservices=homeServices), context_instance=RequestContext(request))

def view_contact(request):
    msg_form = " "
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            try:
                recipients = [DEFAULT_FROM_EMAIL, DEFAULT_TO_EMAIL]
                if cc_myself:
                    recipients.append(sender)

                send_mail(subject, message, sender, recipients)
                msg_form = _(u'Su mensage ha sido enviado correctamente')
                return HttpResponseRedirect('/inicio')
            except:
				pass
    else:
        form = ContactForm()

    #recipients=BAD
    return render_to_response("contact.html", dict(form=form, msg_form=msg_form), context_instance=RequestContext(request))

def view_faqs(request):
    faqs = Faq.objects.filter(language=request.LANGUAGE_CODE)

    return render_to_response('faqs.html', { 'faqs': faqs }, context_instance=RequestContext(request))
