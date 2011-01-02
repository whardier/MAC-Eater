from django.db import models

from django.utils.translation import ugettext_lazy as _

from common.models import *

from devices.models import GenericDevice
from devices.models import GenericDeviceInterface

class EthernetDevice(GenericDevice):
    class Meta:
         verbose_name = _('Ethernet Device')
         verbose_name_plural = _('Ethernet Devices')

class EthernetDeviceInterface(GenericDeviceInterface):
    device = models.ForeignKey(EthernetDevice, blank=True, null=True)

    class Meta:
        abstract = True

class EthernetDeviceInterfaceMAC(EthernetDeviceInterface):
    address = models.ForeignKey(MACAddress)

    class Meta:
         verbose_name = _('Ethernet Device Interface MAC Address')
         verbose_name_plural = _('Ethernet Device Interface MAC Addresses')
    
class EthernetDeviceInterfaceIPv4(EthernetDeviceInterface):
    address = models.ForeignKey(IPv4Address)

    class Meta:
         verbose_name = _('Ethernet Device Interface IPv4 Address')
         verbose_name_plural = _('Ethernet Device Interface IPv4 Addresses')

class EthernetDeviceInterfaceIPv6(EthernetDeviceInterface):
    address = models.ForeignKey(IPv6Address)

    class Meta:
         verbose_name = _('Ethernet Device Interface IPv6 Address')
         verbose_name_plural = _('Ethernet Device Interface IPv6 Addresses')

class EthernetDeviceInterfaceFQDN(EthernetDeviceInterface):
    fqdn = models.ForeignKey(FQDN)

    class Meta:
         verbose_name = _('Ethernet Device Interface FQDN')
         verbose_name_plural = _('Ethernet Device Interface FQDNs')
