from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import models


from common.models import BaseModel


class Config(BaseModel):
    app = models.CharField(max_length=20, blank=False, null=False)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    config = models.JSONField(blank=True, default=dict, null=True)

    class Meta:
        unique_together = ("app", "key")
        ordering = ["-id"]

    def __str__(self):
        return f"{self.app} - {self.key}"

    @classmethod
    def get_config_or_default(cls, key, app="", default=""):
        try:
            return cls.objects.get(key=key, app=app)
        except Config.DoesNotExist:
            pass
        if isinstance(default, str):
            return Config(value=default)
        return Config(config=default)

    @classmethod
    def get_config(cls, key, app=None):
        filters = {"key": key, "is_obsolete": False}
        if app:
            filters["app"] = app

        try:
            return cls.objects.get(**filters)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return None
