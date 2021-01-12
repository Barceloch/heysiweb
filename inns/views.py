# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, TemplateView

from inns.models import Album, Image, Inn, BookRoom, ReservationKey, Comment
from inns.forms import Add_InnForm, CommentForm, ReservationForm, InnConfirmForm, ClientConfirmForm

from itemssite.models import BannerSlider
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.mail import send_mail
from captcha.models import CaptchaStore
from django.forms.formsets import formset_factory
from django.contrib.auth.models import User
from visits.models import Visit
from django.utils.translation import ugettext_lazy as _
from heysiweb.settings import DEFAULT_FROM_EMAIL, DEFAULT_TO_EMAIL
####Importar modulos python
import random, datetime, calendar, time, string

# Create your views here.
def inns(request, **kwargs):
    """Inns listing."""
    inns = Inn.objects.all()

    paginator = Paginator(inns, 9)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        inns = paginator.page(page)
    except (InvalidPage, EmptyPage):
        inns = paginator.page(paginator.num_pages)

    return render_to_response("inns.html", dict(inns=inns), context_instance=RequestContext(request))


def view_inn(request, **kwargs):
    inn = get_object_or_404(Inn, machine_name=kwargs['slug'])
    Visit.objects.add_object_visit(request, obj=inn)
    msg_form = " "
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.inn = inn
        comment.save()
        request.session["name"] = comment.name
        request.session["email"] = comment.email
        request.session["country"] = comment.country
        return redirect(request.path)
        msg_form = _(u'Su comentario ha sido guardado correctamente')
    form.initial['name'] = request.session.get('name')
    form.initial['email'] = request.session.get('email')
    form.initial['country'] = request.session.get('country')
    return render_to_response('viewinn.html',
                              {
                                  'inn': inn,
                                  'form': form,
                                  'msg_form': msg_form,
                              },
                              context_instance=RequestContext(request))

def view_reservation(request, **kwargs):
    inn = get_object_or_404(Inn, machine_name=kwargs['slug'])
    msg_form = " "
    ToDay = datetime.date.today()
    form = ReservationForm(request.POST or None)

    if form.is_valid():
        reservation = form.save(commit=False)
        reservation.inn = inn
        reservation.is_confirmed = False
        reservation.save()


        ikey = ' '
        ckey = ' '
        for i in range(6):
            ikey += str(random.choice('QAZXSWEDCVFRTGBNHYUJMKIOLP0123456789'))
            ckey += str(random.choice('QAZXSWEDCVFRTGBNHYUJMKIOLP0123456789'))

        rk = ReservationKey(inn_key=ikey , client_key=ckey, book=reservation)
        rk.save()

        link = u'http://heysi.pythonanywhere.com/' + inn.machine_name + u'/reservacion' 
        #Enviar notificacion
        #Al administrador
        try:
            subject = u'heySi!:' + inn.name + u'- Tiene solicitud de reservacion' + str(reservation.created_on.strftime("%d/%m/%y %I:%M%p"))

            message = (reservation.name + u'ha solicitado una reservacion desde ' + reservation.country + u'\n' +
                      u'Fecha de llegada: ' + str(reservation.date_in.strftime("%d/%m/%y %I:%M%p")) + u'\n', u'Fecha de salida: ' + str(reservation.date_out.strftime("%d/%m/%y %I:%M%p")) + u'\n' +
                      u'Personas: ' + str(reservation.paxs) + u'Habitaciones: ' + str(reservation.rooms) + u'\n\nMensaje: \n' + reservation.text + 
                      u'\n\nPor favor visite el siguiente enlace: ' + link + u'\n\nPara confirmar la reservación use el código siguiente: ' + rk.inn_key +
                      u'\n\nBookRoom pk: ' + str(reservation.pk) + u'\n\nReservationKey pk: ' + str(rk.pk), u'\n\nClient Code: ' + rk.client_key)

            from_email = DEFAULT_FROM_EMAIL
            recipients = [DEFAULT_FROM_EMAIL, DEFAULT_TO_EMAIL]

            send_mail(subject, message, from_email, recipients)

            #Al cliente
            subject = 'heySi! - Reservacion enviada a: ' + service.name
            message = ('Su reservacion ha sido enviada, pronto recibira confirmacion de ' + service.name + '\n\n' +
                  'Your reservation has been sent to ' + service.name + ' mush you wait confirmation')

            from_email = DEFAULT_FROM_EMAIL
            recipients = [reservation.email]

            send_mail(subject, message, from_email, recipients)
        except:
		    pass

        return redirect(request.path)
        msg_form = _(u'Su reservación ha sido enviada correctamente')
    #Confirmar reservacion
    #bookrooms = BookRoom.objects.get(service=service)
    for bookroom in inn.bookroom_set.all():
        rkey = ReservationKey.objects.get(book=bookroom)

        if bookroom.is_confirmed == False and ToDay > bookroom.date_in:
            rkey.delete()
            bookroom.delete()

        elif bookroom.is_confirmed == True and ToDay > bookroom.date_out:
            rkey.delete()
            bookroom.delete()

        elif bookroom.is_confirmed==False and rkey.i_confirmed and rkey.c_confirmed:
            bookroom.is_confirmed = True
            bookroom.save()
            try:
                subject = 'heySi! - Reservacion totalmente confirmada'
                message = ('La reservación está oficialmente confirmada \n\n' +
                        'The reservation is confirmed complety')

                from_email = DEFAULT_FROM_EMAIL
                recipients = [service.email, bookroom.email, DEFAULT_TO_EMAIL, DEFAULT_FROM_EMAIL]

                send_mail(subject, message, from_email, recipients)
            except:
		        pass

        else:
            bookroom.is_confirmed = False
            bookroom.save()

    return render_to_response('reservation.html',
                              {
                                  'inn': inn,
                                  'form': form,
                                  'msg_form': msg_form,

                              },
                              context_instance=RequestContext(request))

def view_confirmation(request, **kwargs):
    inn = get_object_or_404(Inn, machine_name=kwargs['slug'])
    reservation = BookRoom.objects.get(id=kwargs['bookroom_id'])
    rk = reservation.reservationkey_set.get(book=reservation)

    form1 = InnConfirmForm(request.POST or None)
    form2 = ClientConfirmForm(request.POST or None)


    if form1.is_valid():
            rk = ReservationKey.objects.get(service_key__icontains=form1.cleaned_data['key_inn'])
            rk.s_confirmed = True
            rk.save()

            try:
                subject = u'heySí! - Reservacion confirmada por: ' + inn.name
                message = (inn.name + u' ha confirmado su reservación, ahora used debe confirmar la misma \n\n' +
                            inn.name + u'has confirmed your  reservación, now you mush confirmate too\n\n' +
                            u'Código de confirmación/Confirmation code: ' + rk.client_key)

                from_email = DEFAULT_FROM_EMAIL
                recipients = [reservation.email, DEFAULT_TO_EMAIL]

                send_mail(subject, message, from_email, recipients)
            except:
		         pass

            return redirect('.')

    if form2.is_valid():
            rk = ReservationKey.objects.get(client_key__icontains=form2.cleaned_data['key_client'])
            rk.c_confirmed = True
            rk.save()

            return redirect('.')


    return render_to_response('confirmation.html',
                              {
                                  'reservation': reservation,
                                  'inn': inn,
                                  'form1': form1,
                                  'form2': form2,
                                  'rk': rk,
                              },
                              context_instance=RequestContext(request))


def Add_InnView(request):
    if request.method == 'POST':
        form = Add_InnForm(request.POST or None, request.FILES)
        if form.is_valid():
            inn = form.save(commit=False)
            inn.is_premium = False
            inn.is_public = False
            inn.save()
            return redirect('/hostales')
    else:
        form = Add_InnForm()         
    return render_to_response('add_inn_form.html',
                              { 'form': form },
                              context_instance=RequestContext(request))
