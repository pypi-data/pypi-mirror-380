Decorator Router for Django Rest Framework
==========================================

[![build](https://github.com/brenodega28/drf-decorator-router/actions/workflows/build.yml/badge.svg)](https://github.com/brenodega28/drf-decorator-router/actions/workflows/build.yml)

About
-----
Django Rest Framework package to quickly route your views with decorators.
Very lightweight and simple code using only Django and Rest Framework as dependencies.

Supported Versions
------------------
* Python 3.6 and above
* Django >= 2.2
* Django REST Framework >=3.7.0

Installation
------------
```shell
pip install drf-decorator-router
```

How to Use
----------

#### main_app/routes.py
```python
from rest_framework import generics, viewsets
from drf_decorator_router import Router

# Declaring the router
router = Router("api/v1", namespace="api-v1")
```

#### example_app/views.py
## Default Router
```python
@router.route_view("login/", "user-login") # /api/v1/login/
class LoginView(generics.CreateAPIView):
    pass

@router.route_view("company/<int:company_id>/login/", "company-user-login") # /api/v1/company/10/login/
class LoginForCompanyView(generics.CreateAPIView):
    pass

@router.route_viewset("users", "users") # /api/v1/users/
class UserViewSet(viewsets.ModelViewSet):
    pass
```
<b>Important:</b> The decorated view/viewset <u>must be declared or imported</u> in the `views.py` file, or else it
won't be routed. You can also change the file name from which the views will be loaded by adding a `AUTO_ROUTER_MODULES`
in settings.py. Example: `AUTO_ROUTER_MODULES=['decorated_views', 'views']`.

#### main_app/urls.py
```python
from main_app.routers import router

urlpatterns = [
    router.path
]
```

#### Reversing
```python
from rest_framework.reverse import reverse

login_view = reverse("api-v1:user-login")
user_list = reverse("api-v1:users-list")
user_detail = reverse("api-v1:users-detail", (10,))
```

## Admin Router
You can turn Django ModelAdmins into secure APIs using the Admin Router

#### main_app/routes.py
```python
from rest_framework import generics, viewsets
from drf_decorator_router import AdminRouter

# Declaring the router
router = AdminRouter("api/admin", namespace="api-admin")
```

#### main_app/admin.py
```python
from django.contrib import admin
from drf_decorator_router.pagination import StandardResultsSetPagination

from . import models
from .routers import admin_router
from .serializers import ProductSerializer


@admin_router.register(models.User, "users")
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email") # GET List requests will only show the fields in list_display, while GET Retrieve will show all fields
    list_filter = ("city", "state") # You'll be able to filter in the GET List requests using this filters
    search_fields = ("full_name", "username", "email") # GET List requests will allow a ?s=search_here using the fields in search_fields


# You can customize it even more by passing serializer_cls and other optional fields
@admin_router.register(models.Product, "products", serializer_cls=ProductSerializer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    search_fields = ("price",)
    pagination_class = StandardResultsSetPagination
```

#### Available Routes
Using the UserAdmin as example, here are the routes available.
```
GET /api/admin/users/ -> List all users using the list_display fields.
GET /api/admin/users/id/ -> List all fields for specific user.
POST /api/admin/users/ -> Adds new user.
PUT /api/admin/users/id/ -> Updates user using all fields.
PATCH /api/admin/users/id/ -> Updates specific user fields.
DELETE /api/admin/users/id/ -> Deletes a user.
```

#### Authentication
By default all the routes provided by the Admin Router requires superuser privilege.
The Authorization method is defined by Rest Framework DEFAULT_AUTHENTICATION_CLASSES field.

To Do
----------

- [ ] Custom authentication for routers.
- [ ] Docs page with more examples.
