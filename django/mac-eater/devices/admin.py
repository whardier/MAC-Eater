from django.contrib import admin

from models import DeviceUUID
from models import DeviceMake
from models import DeviceModel
from models import MACAddressUUID
    
class GenericDeviceAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'user', 'name', 'port_count', 'date_created', 'date_modified')

class GenericDeviceInterfaceAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'port', 'date_created', 'date_modified')

admin.site.register(DeviceUUID)
admin.site.register(DeviceMake)
admin.site.register(DeviceModel)
admin.site.register(MACAddressUUID)

