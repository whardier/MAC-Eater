from django.contrib import admin

from models import EthernetDevice
from models import EthernetDeviceInterfaceMAC
from models import EthernetDeviceInterfaceIPv4
from models import EthernetDeviceInterfaceIPv6
from models import EthernetDeviceInterfaceFQDN

class GenericDeviceAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'user', 'name', 'port_count', 'date_created', 'date_modified')

class GenericDeviceInterfaceAdmin(admin.ModelAdmin):
    pass

admin.site.register(EthernetDevice, GenericDeviceAdmin)
admin.site.register(EthernetDeviceInterfaceMAC, GenericDeviceInterfaceAdmin)
admin.site.register(EthernetDeviceInterfaceIPv4, GenericDeviceInterfaceAdmin)
admin.site.register(EthernetDeviceInterfaceIPv6, GenericDeviceInterfaceAdmin)
admin.site.register(EthernetDeviceInterfaceFQDN, GenericDeviceInterfaceAdmin)

