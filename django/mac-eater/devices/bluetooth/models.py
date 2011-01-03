from django.db import models

from django.utils.translation import ugettext_lazy as _

from common import register_geohash_model
from common.models import *

from devices import register_device

from devices.models import GenericDevice
from devices.models import GenericDeviceInterface

class BluetoothDevice(GenericDevice):
    class Meta:
         verbose_name = _('Bluetooth Device')
         verbose_name_plural = _('Bluetooth Devices')

register_device(BluetoothDevice)
register_geohash_model(BluetoothDevice)

class BluetoothDeviceInterface(GenericDeviceInterface):
    device = models.ForeignKey(BluetoothDevice, blank=True, null=True)

    class Meta:
        abstract = True

class BluetoothDeviceInterfaceMAC(BluetoothDeviceInterface):
    address = models.ForeignKey(MACAddress)

    class Meta:
         verbose_name = _('Bluetooth Device Interface MAC Address')
         verbose_name_plural = _('Bluetooth Device Interface MAC Addresses')

