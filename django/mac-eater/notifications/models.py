from django.db import models

from django.utils.translation import ugettext_lazy as _

from devices.models import DeviceUUID

class Email(models.Model):
    device_uuid = models.ForeignKey(DeviceUUID)
    address = models.EmailField(_('Email Address'), blank=True)
    notify_on_detect = models.BooleanField(_('Notify On Detect'), default=False)
    notify_on_detected = models.BooleanField(_('Notify On detected'), default=False)
    verified = models.BooleanField(_('Verified Address'), default=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return unicode(self.address)

class MobileEmail(Email):
    mms = models.BooleanField(_('Is MMS capable?'))

    class Meta:
        verbose_name = _('Mobile Email Address')
        verbose_name_plural = _('Mobile Email Addresses')

class MobileEmailCode(models.Model):
    address = models.ForeignKey(MobileEmail)

    class Meta:
        verbose_name = _('Mobile Email Verification Code')
        verbose_name_plural = _('Mobile Email Verification Codes')

    def __unicode__(self):
        return u'%d:%s' % (self.id, self.address)
