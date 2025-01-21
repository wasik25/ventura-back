from django.contrib import admin
from .models import Product, Cart, CartItem, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "size", "color", "popularity", "slug")
    list_filter = ("size", "color")  
    search_fields = ("name",)  
    readonly_fields = ("slug",) 

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:  
            form.base_fields.pop("slug", None)  
        return form


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("cart_code", "user", "paid", "created_at", "modified_at")
    list_filter = ("paid", "created_at")  
    search_fields = ("cart_code", "user__username")  

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")
    list_filter = ("cart", "product")  
    search_fields = ("cart__cart_code", "product__name")  


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewer", "product", "rating", "created")
    list_filter = ("rating", "created")  
    search_fields = ("reviewer__username", "product__name") 
