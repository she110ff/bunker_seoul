from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import (ugettext, ugettext_lazy as _,
                                    pgettext_lazy as __)

from cartridge.shop.models import Category, Product

class UserCategory(models.Model):
    user = models.ForeignKey(User)
    categories = models.ManyToManyField(Category, blank=True,
                                        verbose_name=_("Product categories"))

class ProductLike(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    like = models.BooleanField(default=False)
