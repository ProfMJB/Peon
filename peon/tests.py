from django.test import TestCase
from selenium import webdriver
from django.http.request import HttpRequest
from views import add

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
#         There are 4 input boxes, labeled Start Latitude, Start Longitude, Lifetime and Name, and one button labelled Add Peon.
        startLatBox = self.browser.find_element_by_id('startLat')
        self.assertEqual(startLatBox.get_attribute('placeholder'),'Start Latitude')
        startLongBox = self.browser.find_element_by_id('startLong')
        self.assertEqual(startLongBox.get_attribute('placeholder'),'Start Longitude')
        lifetimeBox = self.browser.find_element_by_id('lifetime')
        self.assertEqual(lifetimeBox.get_attribute('placeholder'),'Lifetime')
        nameBox = self.browser.find_element_by_id('name')
        self.assertEqual(nameBox.get_attribute('placeholder'),'Name')
        addButton = self.browser.find_element_by_id('submit')
        self.assertEqual(addButton.get_attribute('value'),'Add Peon')
#         User inputs a name, a lat/long and a lifetime.
        startLatBox.send_keys("0")
        startLongBox.send_keys("0")
        lifetimeBox.send_keys("20")
        nameBox.send_keys("Geoffery")
        self.fail('You have reached the end of your test, which is probably a good thing :D. WRITE SOME MORE!')
#         Boxes are validated to be legitimate numbers.
#         After clicking Add Peon, the user is taken to a page (/peon/list/)
#         The title on the page is "Peon List".
#         The page has a list (of one), with the name and lat/long of the peon.
#         When the lifetime is up, the peon is removed from the list, leaving an empty list box.

class peonUnitTests(TestCase):
    def test_addPeonSavesPOSTRequest(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['startLat'] = '1'
        request.POST['startLong'] = '2'
        request.POST['name'] = 'Geoffery'
        request.POST['lifetime'] = '10'
        
        response = add(request)
        
        self.assertIn('<tr><td>Geoffery</td><td>1</td><td>2</td><td>10</td></tr>',response.content.decode())