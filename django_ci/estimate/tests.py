from django.test import TestCase, RequestFactory
from django.core.urlresolvers import resolve

from estimate.models import Estimate
from estimate.views import EstimateList

# from selenium import webdriver


class EstimateURLsTestCase(TestCase):

	def test_root_url_uses_index_view(self):
		root = resolve('/')
		self.assertEqual(root.func.view_class, EstimateList)


# class EstimateListTestCase(TestCase):

# 	def setUp(self):
# 		self.browser = webdriver.Firefox()
# 		self.browser.implicitly_wait(2)
# 		# self.factory = RequestFactory()
# 		# self.model = Estimate

# 	def tearDown(self):
# 		self.browser.quit()

# 	def test_estimate(self):
# 		instrument_input = self.browser.find_element_by_css_selector
# 		self.fail('Incomplete Test')

	# def test_index_view_basic(self):
	# 	request = self.factory.get('/')
	# 	response = EstimateList.as_view()(request)
	# 	self.assertEqual(response.status_code, 200)