from django.test import TestCase
from django.core.urlresolvers import reverse
from models import Product, Comment
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.cache import cache
# small app that's why all test in one file

# I did not write a lot of test because it just a test
# if you make review and you like my code i can fix all mistakes


class ModelsDataCount(TestCase):
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

    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser(
            username='user', password='pass', email='admin@i.ua')
        self.client.login(username='user', password='pass')

    def test_admin(self):
        self.client.logout()
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 302)

    def test_admin_main_page_login(self):
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 200)

    def test_product_admin_page(self):
        '''
        Check exist Product model at admin page
        '''
        response = self.client.get(reverse('admin:product_product_add'))
        self.assertEqual(response.status_code, 200)

    def test_comments_admin_page(self):
        '''
        Check exist Comment model at admin page
        '''
        response = self.client.get(reverse('admin:product_comment_add'))
        self.assertEqual(response.status_code, 200)

    def test_admin_object_view_on_page_link(self):
        '''
        Check exist link "view on site" for Product

        hardcode link for this test because it`s just test and i don`t
        want to spend a lot of time
        '''
        response = self.client.get(reverse('admin:product_product_change',
                                           args={1}))
        self.assertEqual(response.status_code, 200)
        self.assertIn('<a href="http://127.0.0.1:8000/products/short-'
                      'sleeve-blue-maratty-shirt/" class="viewsitelink">'
                      'View on site</a>', response.content)


class TestProductListPages(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser(
            username='user', password='pass', email='admin@i.ua')
        self.client.login(username='user', password='pass')

    def test_product_list(self):
        '''
        test access to page after login and after logout
        '''
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_empty_db(self):
        '''
        Test empty db and cache page
        '''
        Product.objects.all().delete()
        response = self.client.get(reverse('product_list'))
        self.assertContains(response, 'No products in DB', 0)
        cache.clear()
        response = self.client.get(reverse('product_list'))
        self.assertContains(response, 'No products in DB', 1)

    def test_count_products(self):
        '''
        Product object = 24, i can`t find how to test context with pagination
        so i leave it as it is
        '''
        response = self.client.get(reverse('product_list'))
        self.assertEqual(len(response.context['products'][:30]), 10)


class TestPersonalProductPage(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser(
            username='user', password='pass', email='admin@i.ua')
        self.client.login(username='user', password='pass')

    def test_product_page_non_exist(self):
        '''
        Test url with exist product slug and non exist
        :return 200 & 404 status_code
        '''
        product = Product.objects.filter(slug='non_exist_slug')
        self.assertEqual(len(product), 0)
        response = self.client.get(
            reverse('product_page', kwargs={'product_slug': 'non_exist_slug'}))
        self.assertEqual(response.status_code, 404)

    def test_product_page(self):
        '''
        Test exist Product data on page
        '''
        product = Product.objects.get(pk=1)
        response = self.client.get(
            reverse('product_page', kwargs={'product_slug': product.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product.name, 1)
        self.assertContains(response, product.price, 1)

    def test_comment_form(self):
        '''
        Test comment product
        '''
        self.assertEqual(len(Comment.objects.all()), 0)
        product = Product.objects.get(pk=1)
        self.client.get(
            reverse('product_page', kwargs={'product_slug': product.slug}))
        self.client.post(
            reverse('product_page', kwargs={'product_slug': product.slug}),
            {'text': 'New comment'})
        self.assertEqual(len(Comment.objects.all()), 1)

    def test_like_unlike_product(self):
        '''
        Test all product page like function.
        (one user can like product once when authenticated)
        '''
        product = Product.objects.get(pk=1)
        # product have no likes
        self.assertEqual(product.likes.count(), 0)
        self.client.get(
            reverse('like', kwargs={'product_slug': product.slug}))
        # add one like
        self.assertEqual(product.likes.count(), 1)
        self.client.get(
            reverse('like', kwargs={'product_slug': product.slug}))
        # one user can like product once
        self.assertEqual(product.likes.count(), 0)

        # only authenticated user can like product
        self.client.logout()
        self.admin = User.objects.create_superuser(
            username='like', password='like', email='like@like.like')
        self.client.login(username='like', password='like')
        response = self.client.get(
            reverse('like', kwargs={'product_slug': product.slug}))
        self.assertEqual(response.status_code, 302)
