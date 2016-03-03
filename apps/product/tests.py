from django.test import TestCase
from django.core.urlresolvers import reverse
from models import Product, Comment
from django.contrib.auth.models import User

# small app that's why all test in one file


class DataCount(TestCase):
    fixtures = ['initial_data.json']

    def test_count_products(self):
        product = Product.objects.all()
        self.assertEqual(product.count(), 24)

    def test_count_comments(self):
        comments = Comment.objects.all()
        self.assertEqual(comments.count(), 0)

    def test_count_user(self):
        users = User.objects.all()
        self.assertEqual(users.count(), 1)
        self.assertEqual(users[0].username, 'admin')


class TestAdminPages(TestCase):
    fixtures = ['initial_data.json']

    def test_admin(self):
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 302)

    # def test_admin_login(self):
    #     admin = {'name': 'admin',
    #              'password': 'admin'}
    #     response = self.client.post(reverse('admin:index'), admin)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_product_admin_page(self):
    #     pass
