import logging

from django.db.models.signals import pre_save

geohash_models = {}

def update_geohash_precision(sender, **kw):
    instance = kw["instance"]
    if instance.geohash:
        if instance.geohash >= 6:
            instance.geohash_p1 = instance.geohash[0:1]
            instance.geohash_p2 = instance.geohash[0:2]
            instance.geohash_p3 = instance.geohash[0:3]
            instance.geohash_p4 = instance.geohash[0:4]
            instance.geohash_p5 = instance.geohash[0:5]
            instance.geohash_p6 = instance.geohash[0:6]

def register_geohash_model(model):
    geohash_models[str(model)] = model
    pre_save.connect(update_geohash_precision, sender=model)
    logging.info(str(geohash_models))


