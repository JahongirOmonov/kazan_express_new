from django.contrib import admin
from django.apps import apps
from kazan_express import models
# from account.models import SHOP_ADMIN, CATEGORY_ADMIN, PRODUCT_ADMIN


class Photos(admin.TabularInline):
    fk_name = 'product'
    model = models.Image
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'main_photo', "amount", "price", "category")
    inlines = [Photos]
    list_display_links = ("title", "amount", "price")
    actions = ("make_one", )
    # list_per_page = 5
    autocomplete_fields = ['category']
    search_fields = ("title", "price", )
    # list_select_related = ("category", )
    list_filter = ['category']
    raw_id_fields = ['category']





    def make_one(self, request, queryset):
        queryset.update(amount=19)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'shop', 'parent')
    list_display_links = ('id', 'title', 'description', 'shop', 'parent')
    actions = ("change",)
    search_fields = ["title",]

    def change(self, request, queryset):
        queryset.update(description="wonderful")

@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'imageUrl')
    list_display_links = ('id', 'title', 'description', 'imageUrl')
    actions = ("change",)

    def change(self, request, queryset):
        queryset.update(description="nice")















models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
from django.contrib import admin

# Register your models here.
