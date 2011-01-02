from django.contrib import admin

from models import Name
from models import Text
from models import MACAddress
from models import IPv4Address
from models import IPv6Address
from models import FQDN

admin.site.register(Name)
admin.site.register(Text)
admin.site.register(MACAddress)
admin.site.register(IPv4Address)
admin.site.register(IPv6Address)
admin.site.register(FQDN)
