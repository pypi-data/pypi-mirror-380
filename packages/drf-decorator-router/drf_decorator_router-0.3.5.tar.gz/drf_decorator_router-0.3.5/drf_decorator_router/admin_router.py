from typing import Callable
from django.contrib.admin import ModelAdmin, site
from django.db.models import Model
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.viewsets import ModelViewSet, ViewSet

from .base import BaseRouter


class AdminRouter(BaseRouter):
    def register(self, model: Model, route: str, basename: str = "", serializer_cls: type[Serializer] | None = None):
        def inner(model_admin: ModelAdmin):
            site.register(model, model_admin)
            self._log(
                "Routing admin viewset "
                + str(model_admin)
                + " to "
                + self.endpoint
                + route
            )

            class _viewset(ModelViewSet):
                model_admin: ModelAdmin
                permission_classes = [IsAdminUser]
                filterset_fields = []
                search_fields = []
                serializer_cls: type[Serializer]

                def get_queryset(self):
                    return self.model_admin.get_queryset(self.request)

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
                def from_admin(cls, model_admin: ModelAdmin, serializer_cls: type[Serializer] | None = None):
                    cls.model_admin = model_admin
                    cls.filterset_fields = model_admin.list_filter
                    cls.search_fields = model_admin.search_fields

                    if serializer_cls:
                        cls.serializer_cls = serializer_cls

                    if hasattr(model_admin, "filter_backends"):
                        cls.filter_backends = getattr(model_admin, "filter_backends")

                    if hasattr(model_admin, "filterset_class"):
                        cls.filterset_class = getattr(model_admin, "filterset_class")

                    if hasattr(model_admin, "pagination_class"):
                        cls.pagination_class = getattr(model_admin, "pagination_class")

                    return cls

            _viewset = _viewset.from_admin(model_admin(model, site), serializer_cls)
            self._router.register(route, _viewset, basename=basename or route)
            return _viewset

        return inner
