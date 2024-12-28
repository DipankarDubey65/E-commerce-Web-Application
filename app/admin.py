from django.contrib import admin

# Register your models here.
from .models import Category,Sub_Category,Product,Items,RecommedItems,Slider,Contact,Order,Brand
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Items)
admin.site.register(RecommedItems)
admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Brand)





