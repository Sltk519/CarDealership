from django.contrib import admin
from .models import Car, Category, CarDetail,Review,Order

# Import your models (assuming they're in the same file)
from .models import Category, Car, CarDetail


class CarDetailInline(admin.StackedInline):
    model = CarDetail
    fk_name = 'car'  # Foreign key field name
    extra = 1  # Allow adding one extra CarDetail instance

class CarAdmin(admin.ModelAdmin):
    inlines = [CarDetailInline]  # Include CarDetailInline in the admin form
    list_display = ('brand', 'model', 'year', 'is_sold', 'category')
    list_filter = ('category', 'is_sold')
    search_fields = ('brand', 'model', 'description')

    

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'created_at',"quantity")
    list_filter = ('user', 'car', 'created_at',"quantity")
    search_fields = ('user', 'car', 'created_at',"quantity")
    
admin.site.register(Order,OrderAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Category)
admin.site.register(Review)

