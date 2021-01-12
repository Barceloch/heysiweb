# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from inns.models import Inn, BookRoom, ReservationKey, Comment
from heysiweb.settings import DEFAULT_FROM_EMAIL, DEFAULT_TO_EMAIL
from django.core.mail import send_mail
####Importar modulos python
import email, imaplib, string

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login('heysiweb@gmail.com', '2014*heysi')
            mail.select("inbox")
            result, data = mail.search(None, "ALL")

            for num in data[0].split():
				result, data = mail.fetch(num, '(RFC822)')
				raw_email = data[0][1]
				email_message = email.message_from_string(raw_email)
				subject = email_message['Subject']
				action = string.split(subject)

				if action[0] == '!heysi':
					model = action[1]
					objpk = action[2]
					cmd = action[3]

					if model == u'Hostal':
						obj = Inn.objects.get(pk=objpk)
						if cmd == 'True':
							obj.is_public = True
							obj.save()
						elif cmd == 'False':
							obj.is_public = False
							obj.save()
						elif cmd == 'Delete':
							obj.delete()
					elif model == u'Comentario':
						obj = Comment.objects.get(pk=int(objpk))
						if cmd == 'True':
							obj.is_public = True
							obj.save()
						elif cmd == 'False':
							obj.is_public = False
							obj.save()
						elif cmd == 'Delete':
							obj.delete()
					elif model == u'Reservacion':
						obj = BookRoom.objects.get(pk=int(objpk))
						if cmd == 'True':
							obj.is_public = True
							obj.save()
							srv = Inn.bookroom_set.filter(pk=obj.pk)
							rkey = ReservationKey.objects.get(book=obj)
							try:
								subject = string.join([u'heySi! -', srv.name, u'- Tiene solicitud de reservacion', obj.created_on.strftime("%d/%m/%y %I:%M%p")])

								message = string.join([obj.name, u'ha solicitado una reservacion desde ', obj.country, u'\n',
											u'Fecha de llegada: ', obj.date_in.strftime("%d/%m/%y %I:%M%p"), u'\n', u'Fecha de salida: ', obj.date_out.strftime("%d/%m/%y %I:%M%p"), u'\n',
											u'Personas: ', str(obj.paxs), u'Habitaciones: ', str(obj.rooms), u'\n\n', u'Mensaje: \n', obj.text, u'\n\n',
											u'Por favor visite el siguiente enlace: ', link, u'\n\n', u'Para confirmar la reservación use el código siguiente: ', rkey.service_key])

								to_email = DEFAULT_FROM_EMAIL
								recipients = [srv.email, DEFAULT_TO_EMAIL]
								send_mail(subject, message, to_email, recipients)
							except:
								pass

						elif cmd == 'False':
							obj.is_public = False
							obj.save()
						elif cmd == 'Delete':
							obj.delete()
					elif model == u'RCode':
						obj = ReservationKey.objects.get(pk=int(objpk))
						if cmd == 'True':
							obj.i_confirmed = True
							obj.save()
						elif cmd == 'False':
							obj.i_confirmed = False
							obj.save()
						elif cmd == 'Delete':
							obj.delete()
					else:
						pass

            mail.close()
            mail.logout()
        except:
			pass
