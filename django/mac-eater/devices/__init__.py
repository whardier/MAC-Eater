import logging

from django.db.models.signals import pre_save

devices = {}

def update_device_uuid_model(sender, **kw):
    instance = kw["instance"]
    instance.uuid.model = str(sender)
    instance.uuid.save()

def register_device(model):
    devices[str(model)] = model
    pre_save.connect(update_device_uuid_model, sender=model)
    logging.info(str(devices))



