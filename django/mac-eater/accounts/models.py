from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import post_save

from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField

class UserProfile(models.Model):
    user = models.ForeignKey(User)

    date_created = CreationDateTimeField(db_index=True)
    date_modified = ModificationDateTimeField(db_index=True)

    def __unicode__(self):
        return unicode(self.user)

def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        profile = UserProfile()
        profile.user = user
        profile.save()
    else:
        try:
            user.get_profile().save()
        except:
            pass

post_save.connect(create_profile, sender=User)

