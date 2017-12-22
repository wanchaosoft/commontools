# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from django.test.client import Client
from django.test.client import RequestFactory

# selenium来测试web
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


import django.http
import django.utils.unittest as unittest2

# we can use rebar to help to test our Form.
from rebar.testing import flatten_to_dict

# consume as ListView, Contact as Model, ContactForm as Form
ListContactView = object()
Contact = object()
ContactForm = object()


# 继承TestCase
class ContactListViewTests(TestCase):
    """Contact list view tests."""

    def test_contacts_in_the_context(self):

        client = Client()
        response = client.get('/')

        self.assertEquals(list(response.context['object_list']), [])

        Contact.objects.create(first_name='foo', last_name='bar')
        response = client.get('/')
        self.assertEquals(response.context['object_list'].count(), 1)

    def test_contacts_in_the_context_request_factory(self):

        factory = RequestFactory()
        request = factory.get('/')

        response = ListContactView.as_view()(request)

        self.assertEquals(list(response.context_data['object_list']), [])

        Contact.objects.create(first_name='foo', last_name='bar')
        response = ListContactView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)


class ContactListIntegrationTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(ContactListIntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(ContactListIntegrationTests, cls).tearDownClass()

    def test_contact_listed(self):

        # create a test contact
        Contact.objects.create(first_name='foo', last_name='bar')

        # make sure it's listed as <first> <last> on the list
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.contact')[0].text,
            'foo bar'
        )

    def test_add_contact_linked(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assert_(
            self.selenium.find_element_by_link_text('add contact')
        )

    def test_add_contact(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_element_by_link_text('add contact').click()

        self.selenium.find_element_by_id('id_first_name').send_keys('test')
        self.selenium.find_element_by_id('id_last_name').send_keys('contact')
        self.selenium.find_element_by_id('id_email').send_keys('test@example.com')

        self.selenium.find_element_by_id("save_contact").click()
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.contact')[-1].text,
            'test contact'
        )

# use cleaned_data.get('email') instead of cleaned_data['email']

#　 pip install rebar



class EditContactFormTests(TestCase):

    def test_mismatch_email_is_invalid(self):

        form_data = flatten_to_dict(ContactForm())
        form_data['first_name'] = 'Foo'
        form_data['last_name'] = 'Bar'
        form_data['email'] = 'foo@example.com'
        form_data['confirm_email'] = 'bar@example.com'

        bound_form = ContactForm(data=form_data)
        self.assertFalse(bound_form.is_valid())

    def test_same_email_is_valid(self):

        form_data = flatten_to_dict(ContactForm())
        form_data['first_name'] = 'Foo'
        form_data['last_name'] = 'Bar'
        form_data['email'] = 'foo@example.com'
        form_data['confirm_email'] = 'foo@example.com'

        bound_form = ContactForm(data=form_data)
        self.assert_(bound_form.is_valid())


# ########################## Django #########################
# Unit Test should be fast and not rely on  external services
#### Unit Test


class LocaleMiddlewareTests(unittest2.TestCase):

    def test_request_not_processed(self):
        from middleware.basicauthmiddleware import LocaleMiddleware
        middleware = LocaleMiddleware()
        response = django.http.HttpResponse()
        middleware.process_response(None, response)

        self.assertFalse(response.cookies)

# Test Client is slow, it just like a browser. Sort of.
#### Test Client
# from django.test.client import Client
#
# c = Client()
#
# response = c.get('/login')
# self.assertEqual(response.status_code, 200)
#
# response = c.post('/login/', {'username': 'john', 'password': 'smith'})

# RequestFactory
# Running Tests > ./manage.py test