from django.db import models
from shortuuidfield import ShortUUIDField


class BaseModel(models.Model):
    idx = ShortUUIDField(unique=True, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    modified_on = models.DateTimeField(auto_now=True, editable=False)
    is_obsolete = models.BooleanField(default=False, db_index=True)

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        self.save()
        return self

    @classmethod
    def new(cls, **kwargs):
        return cls.objects.create(**kwargs)

    def delete(self, force_delete=True, **kwargs):
        if force_delete:
            super(BaseModel, self).delete(**kwargs)
        else:
            self.update(is_obsolete=True)
            return self

    class Meta:
        abstract = True
