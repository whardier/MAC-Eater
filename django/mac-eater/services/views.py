import logging
 
import email
from email.iterators import typed_subpart_iterator

from StringIO import StringIO

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from notifications.models import MobileEmailCode

from google.appengine.api import mail
 
@csrf_exempt    
def email_handler(request, address=''):
    if request.POST:
        logging.info("Received a message")
        try:
            message = email.message_from_string(request.raw_post_data)
        except:
            return HttpResponse('fail')

        if message.is_multipart():
            mms = True
        else: 
            mms = False

        for part in typed_subpart_iterator(message, 'text', 'plain'):
            body = StringIO(part.get_payload()).readlines()

        for line in body:
            try:
                mec_id = int(line)
            except ValueError, msg: 
                continue

            if mec_id:
                mec_object = MobileEmailCode.objects.filter(id=mec_id)
                if mec_object:
                    for mec in mec_object:
                        address = mec.address
                        address.address = message['From']
                        address.mms = mms
                        address.save()
                        mec.delete()

    return HttpResponse('ok')
