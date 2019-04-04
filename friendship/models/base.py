from django.db import models


class BaseModel(models.Model):
    """
    Base model class to define common variables and implement
    common methods.No database table will be created for this
    model as this is only abstract model. Primary purpose of
    this model is to be used as parent class to other concrete
    models.
    """
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        """
        A generic implementation of `repr(obj)`. In order to support more
        extensive debugging please implement this method in child class
        with necessary information.
        """
        return "<{}(id={})>".format(self.__class__.__name__, self.id)
