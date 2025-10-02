from typing import Callable
from django.contrib.admin import ModelAdmin, site
from django.db.models import Model
from rest_framework.pagination import BasePagination, PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.viewsets import ModelViewSet, ViewSet

from .base import BaseRouter


class AdminRouter(BaseRouter):
    def register(self, model: Model, route: str, basename: str = "", serializer_class: type[Serializer] | None = None, pagination_class: type[BasePagination] | None = None):
        def inner(model_admin: ModelAdmin):
            site.register(model, model_admin)
            self._log(
                "Routing admin viewset "
                + str(model_admin)
                + " to "
                + self.endpoint
                + route
            )

            class _pagination(PageNumberPagination):
                page_size = 10
                page_size_query_param = 'page_size'
                max_page_size = 100

                @classmethod
                def from_values(cls, page_size, max_page_size):
                    cls.page_size = page_size
                    cls.max_page_size = max_page_size

                    return cls


            class _viewset(ModelViewSet):
                model_admin: ModelAdmin
                permission_classes = [IsAdminUser]
                filterset_fields = []
                search_fields = []
                serializer_cls: type[Serializer] | None = None

                def get_ordering(self):
                    ma_ordering = self.model_admin.get_ordering(self.request)

                    if len(ma_ordering) > 0 and ma_ordering[0]:
                        return ma_ordering

                    return self.model_admin.model._meta.ordering

                def get_queryset(self):
                    return self.model_admin.get_queryset(self.request).order_by(*self.get_ordering())

                def get_serializer_class(self):
                    if self.serializer_cls:
                        return self.serializer_cls

                    class _serializer(ModelSerializer):
                        class Meta:
                            pass

                    _serializer.Meta.model = self.model_admin.model

                    if self.action == 'list':
                        _serializer.Meta.fields = self.model_admin.list_display
                    else:
                        _serializer.Meta.exclude = []

                    return _serializer

                @classmethod
                def from_admin(cls, model_admin: ModelAdmin, serializer_class, pagination_class):
                    cls.model_admin = model_admin
                    cls.filterset_fields = model_admin.list_filter
                    cls.search_fields = model_admin.search_fields

                    if pagination_class:
                        cls.pagination_class = pagination_class
                    else:
                        list_per_page = getattr(model_admin, 'list_per_page') if hasattr(model_admin, 'list_per_page') else 10
                        list_max_show_all = getattr(model_admin, 'list_max_show_all') if hasattr(model_admin, 'list_per_page') else 20
                        cls.pagination_class = _pagination.from_values(list_per_page, list_max_show_all)

                    if serializer_class:
                        cls.serializer_cls = serializer_class

                    if hasattr(model_admin, "filter_backends"):
                        cls.filter_backends = getattr(model_admin, "filter_backends")

                    if hasattr(model_admin, "filterset_class"):
                        cls.filterset_class = getattr(model_admin, "filterset_class")

                    return cls

            _viewset = _viewset.from_admin(model_admin(model, site), serializer_class, pagination_class)
            self._router.register(route, _viewset, basename=basename or route)
            return _viewset

        return inner
