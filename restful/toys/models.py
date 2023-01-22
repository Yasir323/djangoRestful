from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Toy(BaseModel):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=500, blank=True, default='')
    toy_category = models.CharField(max_length=150, blank=False, default='', db_column='toyCategory')
    release_date = models.DateTimeField(db_column='releaseDate')
    was_included_in_home = models.BooleanField(default=False, db_column='wasIncludedInHome')

    class Meta:
        """
        Results should be sorted by `name` in Ascending order
        """
        ordering = ('name',)
