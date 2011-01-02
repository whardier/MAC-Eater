from django.db import models

from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import UUIDField

from geohash import geohash

class Name(models.Model):
    text = models.CharField(max_length=4096)

    class Meta:
         verbose_name = _('Name')
         verbose_name_plural = _('Names')

    def __unicode__(self):
        return unicode(self.text)

class Text(models.Model):
    text = models.TextField()

    class Meta:
         verbose_name = _('Text')
         verbose_name_plural = _('Texts')

    def __unicode__(self):
        return unicode(self.text)

class MACAddress(models.Model):
    text = models.CharField(max_length=17)
    geohash = models.CharField(max_length=12, blank=True, null=True)
        
    class Meta:
         verbose_name = _('MAC Address')
         verbose_name_plural = _('MAC Addresses')

    def __unicode__(self):
        return unicode(self.text)

class IPv4Address(models.Model):
    text = models.CharField(max_length=15)

    class Meta:
         verbose_name = _('IPv4 Address')
         verbose_name_plural = _('IPv4 Addresses')

    def __unicode__(self):
        return unicode(self.text)

class IPv6Address(models.Model):
    text = models.CharField(max_length=39)

    class Meta:
         verbose_name = _('IPv6 Address')
         verbose_name_plural = _('IPv6 Addresses')

    def __unicode__(self):
        return unicode(self.text)

class FQDN(models.Model):
    text = models.CharField(max_length=1024)

    class Meta:
         verbose_name = _('FQDN')
         verbose_name_plural = _('FQDNs')

    def __unicode__(self):
        return unicode(self.text)

