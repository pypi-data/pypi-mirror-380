from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from model_mommy import mommy

from .mockapp.models import MockProduct, MockStore


class DecoratorRouterAPITestCase(APITestCase):
    store_list_url = reverse("api-v1:mock-store-list")
    products_list_url = reverse("api-v1:mock-products")

    def setUp(self):
        self.store_1 = mommy.make(MockStore)
        self.store_2 = mommy.make(MockStore)

        for store in [self.store_1, self.store_2]:
            mommy.make(MockProduct, store=store, _quantity=10)

    def test_it_lists_stores_from_viewset(self):
        response = self.client.get(self.store_list_url)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json), 2)
        self.assertEqual(json[0]['extra_code'], 'test')

    def test_it_retrieves_store_from_viewset(self):
        url = reverse("api-v1:mock-store-detail", (self.store_1.id,))
        response = self.client.get(url)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['id'], self.store_1.id)

    def test_it_lists_products_from_viewset(self):
        response = self.client.get(self.products_list_url)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json), 20)

class DecoratorAdminRouterAPITestCase(APITestCase):
    get_store_url = lambda self, t=None: reverse("admin-api:mock-store-" + (t or 'list'))
    get_products_url = lambda self, t=None: reverse("admin-api:mock-product-" + (t or 'list'))

    def setUp(self):
        self.admin = User.objects.create(username='test', is_superuser=True, is_staff=True)
        self.admin.set_password('test')
        self.main_store = mommy.make(MockStore)

        mommy.make(MockStore, _quantity=10)

        self.client.force_authenticate(user=self.admin)

        for store in [self.main_store]:
            mommy.make(MockProduct, store=store, _quantity=20)

    def test_it_lists_stores_from_admin_viewset(self):
        response = self.client.get(self.get_store_url())
        json = response.json()

        self.assertEquals(response.status_code, 200)
        self.assertEqual(json['count'], 11)
        self.assertEqual(len(json['results']), 10)

    def test_it_lists_products_from_admin_viewset(self):
        response = self.client.get(self.get_products_url())
        json = response.json()

        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(json['results']), 20)
