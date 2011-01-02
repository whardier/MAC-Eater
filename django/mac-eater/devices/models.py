from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import UUIDField
from django_extensions.db.fields import CreationDateTimeField
from django_extensions.db.fields import ModificationDateTimeField

from common.models import *

from geohash import geohash

class DeviceUUID(models.Model):
    uuid = UUIDField()

    class Meta:
        verbose_name = _('Device UUID')
        verbose_name_plural = _('Device UUIDs')

    def __unicode__(self):
        return unicode(self.uuid)

class MACAddressUUID(models.Model):
    uuid = UUIDField()

    class Meta:
        verbose_name = _('MAC Address UUID')
        verbose_name_plural = _('MAC Address UUIDs')

    def __unicode__(self):
        return unicode(self.uuid)

class DeviceMake(models.Model):
    text = models.CharField(_('Make'), max_length=255)

    class Meta:
        verbose_name = _('Device Make')
        verbose_name_plural = _('Device Makes')

    def __unicode__(self):
        return unicode(self.text)

class DeviceModel(models.Model):
    text = models.TextField(_('Model'))
    class Meta:
        verbose_name = _('Device Model')
        verbose_name_plural = _('Device Models')

    def __unicode__(self):
        return unicode(self.text)

class GenericDevice(models.Model):
    uuid = models.ForeignKey(DeviceUUID)
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.ForeignKey(Name, blank=True, null=True)
    description = models.ForeignKey(Text, blank=True, null=True)
    make = models.ForeignKey(DeviceMake, blank=True, null=True)
    model = models.ForeignKey(DeviceModel, blank=True, null=True)
    geohash = models.CharField(_('Geohash'), max_length=12, blank=True, null=True)
    port_count = models.IntegerField(_('Logical Port Count'), blank=True, null=True)
    date_created = CreationDateTimeField()
    date_modified = ModificationDateTimeField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return unicode(self.uuid)

class GenericDeviceInterface(models.Model):
    uuid = models.ForeignKey(MACAddressUUID)    
    name = models.ForeignKey(Name, blank=True, null=True)
    description = models.ForeignKey(Text, blank=True, null=True)
    port = models.IntegerField(_('Logical Port Number'), blank=True, null=True)    
    date_created = CreationDateTimeField()
    date_modified = ModificationDateTimeField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return unicode(self.uuid)

