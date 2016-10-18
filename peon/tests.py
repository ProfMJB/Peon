from django.test import TestCase
from selenium import webdriver

# Create your tests here.

class peonTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()
        
    def test_addPeon(self):
#         User loads page /peon/add/.
        self.browser.get('http://localhost:8000/peon/add/')
#         Title on the page is "Add Peon"
        self.assertIn('Add Peon',self.browser.title)
        self.fail('You have reached the end of your test. WRITE SOME MORE!')
#         There are 5 input boxes, labeled Start Latitude, Start Longitude, Destination Latitude, Destination Longitude and Name, and one button labelled Add Peon.
#         Boxes are validated to be legitimate numbers.
#         After clicking Add Peon, the user is taken to a page (/peon/list/)
#         The title on the page is "Peon List".
#         The page has a list (of one), with the name and lat/long of the peon.
#         The lat/long will gradually move towards the destination lat/long, until reaching it. This can be seen by refreshing the page.
#         When reaching it, the peon is removed from the list, leaving an empty list box.