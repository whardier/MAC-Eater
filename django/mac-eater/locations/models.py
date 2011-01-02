from django.db import models

from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import CreationDateTimeField
from django_extensions.db.fields import ModificationDateTimeField

from Geohash import geohash

from common.models import Name
from common.models import Text

from devices.models import DeviceUUID
from devices.models import MACAddressUUID

class Source(models.Model):
    result = models.TextField()
    date_created = CreationDateTimeField(_('Creation Date/Time'))
    date_modified = ModificationDateTimeField(_('Creation Date/Time'))


class Location(models.Model):
    source = models.ForeignKey(Source)
    device_uuid = models.ForeignKey(DeviceUUID)
    mac_address_uuid = models.ForeignKey(MACAddressUUID)
    geohash = models.CharField(_('Geohash'), max_length=12)
    date_created = CreationDateTimeField(_('Creation Date/Time'))
    date_located = models.DateTimeField(_('Address Location Date/Time'))
    date_device_uploaded = models.DateTimeField(_('Device Upload Date/Time')) #The date the device reports uploading the report
    date_device_located = models.DateTimeField(_('Device Address Location Date/Time')) #The date the device located the mac address.. just take one minus the other to figure out a more accurate location time

    class Meta:
        verbose_name = _('Address Location')
        verbose_name_plural = _('Address Locations')

    def __unicode__(self):
        return unicode(self.geohash)
    
