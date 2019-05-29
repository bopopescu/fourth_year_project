from django.test import TestCase
from django.urls import reverse
#import datetime
from django.test import Client
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import login
from django.http import HttpRequest
from django.core import mail
from fx import main
from ai import maincry
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver




class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']


    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        driver = webdriver.Chrome('/Users/PaulaMoriarty/Downloads/chromedriver')
        cls.selenium = driver
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/smartpredict/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('john')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('smith_12')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()


class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')

# Create your tests here.
class TestClient(Client):

    def login_user(self, user):
        """
        Login as specified user, does not depend on auth backend (hopefully)

        This is based on Client.login() with a small hack that does not
        require the call to authenticate()
        """
        if not 'django.contrib.sessions' in settings.INSTALLED_APPS:
            raise AssertionError("Unable to login without django.contrib.sessions in INSTALLED_APPS")
        user.backend = "%s.%s" % ("django.contrib.auth.backends", "ModelBackend")

        # Create a fake request to store login details.
        request = HttpRequest()
        if self.session:
            request.session = self.session
        login(request, user)

        # Set the cookie to represent the session.
        session_cookie = settings.SESSION_COOKIE_NAME
        self.cookies[session_cookie] = request.session.session_key
        cookie_data = {
            'max-age': None,
            'path': '/',
            'domain': settings.SESSION_COOKIE_DOMAIN,
            'secure': settings.SESSION_COOKIE_SECURE or None,
            'expires': None,
        }
        self.cookies[session_cookie].update(cookie_data)

        # Save the session values.
        request.session.save()

class LoginFunc(TestCase):

    def test_login(self):
        c = Client()
        response = c.post('/smartpredict/login/', {'username': 'john', 'password': 'smith_12'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'john')

class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/smartpredict/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'smartpredict/index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/smartpredict/')
        self.assertContains(response, 'Home')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/smartpredict/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

class AboutPageTests(TestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/smartpredict/about/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'smartpredict/about.html')

    def test_about_page_contains_correct_html(self):
        response = self.client.get('/smartpredict/about/')
        self.assertContains(response, 'About SmartPredict')

    def test_about_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/smartpredict/about/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

class DashBoardTest(TestCase):

    def setUp(self):
        self.client = TestClient()
        user = User(username="john")
        user.save()
        self.client.login_user(user)

    def test_dashboard_status_code(self):
        response = self.client.get('/smartpredict/dashboard/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'smartpredict/dashboard.html')

    def test_dashboard_contains_correct_html(self):
        response = self.client.get('/smartpredict/dashboard/')
        self.assertContains(response, 'Dashboard')

    def test_dashboard_does_not_contain_incorrect_html(self):
        response = self.client.get('/smartpredict/dashboard/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

    def test_cryptodashboard(self):
        response = self.client.get('/smartpredict/cryptodashboard/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Ethereum')

    def test_forexdashboard(self):
        response = self.client.get('/smartpredict/forexdashboard/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'USD')

class RemainingViewTest(TestCase):

    def setUp(self):
        self.client = TestClient()
        user = User(username="john")
        user.save()
        self.client.login_user(user)

    def test_sentiment(self):
        response = self.client.get('/smartpredict/sentiment/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Postive')

    def test_apiconnect(self):
        response = self.client.get('/smartpredict/apiconnect/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Connect')


class TestAI(TestCase):
    def test_fx(self):
        predict = main()
        self.assertIsNotNone(predict)

    def test_crypto(self):
        predict = maincry()
        self.assertIsNotNone(predict)

class SentimentViewTests(TestCase):
    def test_sentiment_view(self):
        w = self.create_sentiment()
        url = reverse('smartpredict/sentiment.html')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content)
