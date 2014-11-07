from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import (ugettext, ugettext_lazy as _,
                                    pgettext_lazy as __)

from cartridge.shop.models import Category

class UserCategory(models.Model):
    user = models.ForeignKey(User)
    categories = models.ManyToManyField(Category, blank=True,
                                        verbose_name=_("Product categories"))


