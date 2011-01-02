from django.db import models

from django.utils.translation import ugettext_lazy as _

from common.models import *

from devices.models import GenericDevice
from devices.models import GenericDeviceInterface

class BluetoothDevice(GenericDevice):
    class Meta:
         verbose_name = _('Bluetooth Device')
         verbose_name_plural = _('Bluetooth Devices')

class BluetoothDeviceInterface(GenericDeviceInterface):
    device = models.ForeignKey(BluetoothDevice, blank=True, null=True)

    class Meta:
        abstract = True

class BluetoothDeviceInterfaceMAC(BluetoothDeviceInterface):
    address = models.ForeignKey(MACAddress)

    class Meta:
         verbose_name = _('Bluetooth Device Interface MAC Address')
         verbose_name_plural = _('Bluetooth Device Interface MAC Addresses')

