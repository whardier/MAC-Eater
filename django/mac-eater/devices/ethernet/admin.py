from django.contrib import admin

from devices.admin import GenericDeviceAdmin
from devices.admin import GenericDeviceInterfaceAdmin

from models import EthernetDevice
from models import EthernetDeviceInterfaceMAC
from models import EthernetDeviceInterfaceIPv4
from models import EthernetDeviceInterfaceIPv6
from models import EthernetDeviceInterfaceFQDN

class IPv4Choices(admin.TabularInline):
    model = EthernetDeviceInterfaceIPv4
    extra = 0

class IPv6Choices(admin.TabularInline):
    model = EthernetDeviceInterfaceIPv6
    extra = 0

class MACChoices(admin.TabularInline):
    model = EthernetDeviceInterfaceMAC
    extra = 0

class FQDNChoices(admin.TabularInline):
    model = EthernetDeviceInterfaceFQDN
    extra = 0

class EthernetDeviceAdmin(GenericDeviceAdmin):
    inlines = [IPv4Choices, IPv6Choices, MACChoices, FQDNChoices]

admin.site.register(EthernetDevice, EthernetDeviceAdmin)
admin.site.register(EthernetDeviceInterfaceMAC, GenericDeviceInterfaceAdmin)
admin.site.register(EthernetDeviceInterfaceIPv4, GenericDeviceInterfaceAdmin)
admin.site.register(EthernetDeviceInterfaceIPv6, GenericDeviceInterfaceAdmin)
admin.site.register(EthernetDeviceInterfaceFQDN, GenericDeviceInterfaceAdmin)

