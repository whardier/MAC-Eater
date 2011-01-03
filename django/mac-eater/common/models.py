from django.db import models

from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import UUIDField

from Geohash import geohash

class GeohashModel(models.Model):
    geohash = models.CharField(_('Geohash'), max_length=12, blank=True, null=True, db_index=True)
    geohash_p1 = models.CharField(_('Geohash Precision 1'), max_length=1, blank=True, null=True, editable=False, db_index=True)
    geohash_p2 = models.CharField(_('Geohash Precision 2'), max_length=2, blank=True, null=True, editable=False, db_index=True)
    geohash_p3 = models.CharField(_('Geohash Precision 3'), max_length=3, blank=True, null=True, editable=False, db_index=True)
    geohash_p4 = models.CharField(_('Geohash Precision 4'), max_length=4, blank=True, null=True, editable=False, db_index=True)
    geohash_p5 = models.CharField(_('Geohash Precision 5'), max_length=5, blank=True, null=True, editable=False, db_index=True)
    geohash_p6 = models.CharField(_('Geohash Precision 6'), max_length=6, blank=True, null=True, editable=False, db_index=True)

    class Meta:
        abstract = True
    
    def __unicode__(self):
        return unicode(self.geohash)
    
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

