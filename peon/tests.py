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
#         Title on the page is "Add Peon", and header is 'Add Peon'
        self.assertIn('Add Peon',self.browser.title)
        headerText = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Add Peon',headerText)
#         There are 5 input boxes, labeled Start Latitude, Start Longitude, Destination Latitude, Destination Longitude and Name, and one button labelled Add Peon.
        startLatBox = self.browser.find_element_by_id('startLat')
        self.assertEqual(startLatBox.get_attribute('placeholder'),'Start Latitude')
        startLongBox = self.browser.find_element_by_id('startLong')
        self.assertEqual(startLongBox.get_attribute('placeholder'),'Start Longitude')
        destinationLatBox = self.browser.find_element_by_id('destinationLat')
        self.assertEqual(destinationLatBox.get_attribute('placeholder'),'Destination Latitude')
        destinationLongBox = self.browser.find_element_by_id('destinationLong')
        self.assertEqual(destinationLongBox.get_attribute('placeholder'),'Destination Longitude')
        nameBox = self.browser.find_element_by_id('name')
        self.assertEqual(nameBox.get_attribute('placeholder'),'Name')
        
        self.fail('You have reached the end of your test, which is probably a good thing :D. WRITE SOME MORE!')
#         Boxes are validated to be legitimate numbers.
#         After clicking Add Peon, the user is taken to a page (/peon/list/)
#         The title on the page is "Peon List".
#         The page has a list (of one), with the name and lat/long of the peon.
#         The lat/long will gradually move towards the destination lat/long, until reaching it. This can be seen by refreshing the page.
#         When reaching it, the peon is removed from the list, leaving an empty list box.