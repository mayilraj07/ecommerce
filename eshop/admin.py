from django.contrib import admin
from .models import *

# Register your models here.
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['category_name','image']
# admin.site.register(Category,CategoryAdmin)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(OrderPlaced)
admin.site.register(BuyProduct)
admin.site.register(Cart)
