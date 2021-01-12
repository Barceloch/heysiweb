# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from inns.models import Inn, BookRoom, ReservationKey, Comment
from heysiweb.settings import DEFAULT_FROM_EMAIL, DEFAULT_TO_EMAIL
from django.core.mail import send_mail

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        no_public_inns = Inn.objects.filter(is_public=False)
        no_public_comments = Comment.objects.filter(is_public=False)
        no_public_books    = BookRoom.objects.filter(is_public=False)

        msg_text = u' '
        if no_public_inns.count() != 0 or no_public_comments.count() != 0 or no_public_books.count() != 0:
		    if no_public_inns.count() != 0:
		    	msg_text += u'#Servicios sin publicar:\n\n '
		    	for inn in no_public_inns:
		    		msg_text += inn.name + ' ' + str(inn.inn_type) + ' Id: ' + str(inn.pk) + u':\n\nE-Mail: ' + inn.email + u'\n\nDetalles:\n'  + inn.details[:100]  + u'\n\n ----------------- \n\n'
		    if no_public_comments.count() != 0:
			    msg_text += u'#Comentarios sin publicar:\n\n '
			    for comment in no_public_comments:
			    	msg_text += comment.name + ' ' + comment.country + ' Id: ' + str(comment.pk) + u':\n\nE-Mail: ' + comment.email + u'\n\nMensaje:\n'  + comment.text[:100]  + u'\n\n ----------------- \n\n'
		    if no_public_books.count() != 0:
		    	msg_text += u'#Reservaciones sin publicar:\n\n '
		    	for book in no_public_books:
		    		rkey = ReservationKey.objects.get(book=book)
		    		msg_text += book.name + ' ' + book.country + ' Id: ' + str(book.pk) + u':\n\nE-Mail: ' + book.email + '\n\nMensaje:\n'  + book.text[:100]  + u'\n\nObjeto para confirmación: ' + str(rkey.pk)   + u'\n\nCódigo del servicio: ' + rkey.inn_key + u'\n\nCódigo del cliente: ' + rkey.client_key + u'\n\n ----------------- \n\n'

		    try:
		    	subject = u'heySí, Elementos sin publicar'
		    	message = msg_text
		    	email = DEFAULT_FROM_EMAIL
		    	recipients = [DEFAULT_TO_EMAIL]
		    	send_mail(subject, message, email, recipients)

		    except:
			    print 'No se pudo enviar el email con los datos obtenidos'
