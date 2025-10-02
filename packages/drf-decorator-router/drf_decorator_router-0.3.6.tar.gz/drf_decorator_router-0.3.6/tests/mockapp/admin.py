from django.contrib import admin

from tests.mockapp.pagination import StandardResultsSetPagination
from tests.mockapp.serializers import MockStoreSerializer

from . import models
from .routers import admin_router


@admin_router.register(models.MockProduct, "mock-product", "mock-product")
class MockProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "store")
    list_filter = ("store", "store__organization")
    search_fields = ("name",)
    list_per_page = 20
    list_max_show_all = 100

    def get_ordering(self, request):
        return ['-id']

@admin_router.register(models.MockStore, "mock-store", serializer_class=MockStoreSerializer, pagination_class=StandardResultsSetPagination)
class MockStoreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "organization")
    search_fields = ("name",)
