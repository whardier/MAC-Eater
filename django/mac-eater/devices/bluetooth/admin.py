from django.contrib import admin

from devices.admin import GenericDeviceAdmin
from devices.admin import GenericDeviceInterfaceAdmin

from models import BluetoothDevice
from models import BluetoothDeviceInterfaceMAC

admin.site.register(BluetoothDevice, GenericDeviceAdmin)
admin.site.register(BluetoothDeviceInterfaceMAC, GenericDeviceInterfaceAdmin)

