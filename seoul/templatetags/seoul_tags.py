from django import template
from django.conf import settings
from django.db.models import Count, Q, Sum
from cartridge.shop.models import Category, Product
from django.contrib.auth.models import User
from seoul.models import UserCategory

register = template.Library()



@register.simple_tag(takes_context=True)
def setenv(context):
    context['S3_URL']=settings.S3_URL
    return ""
    

@register.assignment_tag
def splitstr(text):
    new_texts = text.split('-')
    print new_texts
    return new_texts[1]

@register.assignment_tag
def product_latest(category, count=20):
	try:
		category = Category.objects.get(slug=category)
		products = category.products.filter(available=True).order_by('-publish_date')[0:count]
	except Category.DoesNotExist:
		products = []
	
	return products

@register.assignment_tag
def sub_products(user):
	try:
		uc, created= UserCategory.objects.get_or_create(user=user)
		uc_all  = uc.categories.all()
		products = [product for category in uc_all for product in category.products.all()]
		print "sub_products :", 
	except Category.DoesNotExist:
		products = []
	
	return products



@register.assignment_tag
def subscription_list(user):
	try:
		print "subscription_list"
		print "user name ", user.username
		obj = {}
		uc, created= UserCategory.objects.get_or_create(user=user)
		uc_all  = uc.categories.all().values_list('id', flat=True)
		print "uc.categories : ", uc_all
		categories = Category.objects.all().exclude(id__in=uc_all)
		obj['sub'] = uc.categories.all()
		obj['notsub'] = categories
	except UserCategory.DoesNotExist:
		obj['sub'] = []
		categories = Category.objects.all().order_by('-publish_date')
		obj['notsub'] = categories
	except Category.DoesNotExist:
		obj['sub'] = []
		obj['notsub'] = []
	
	return obj
        