from django.test import TestCase
from .models import Cont


 # Create your tests here.	# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):        
        self.cont = Cont.objects.create(
            sold = 120,
            nume = "test_1",
            credit = 0,
            tipCont = "RON"
        )

    def testData(self):
        self.assertEqual(self.cont.sold,120)
        self.assertEqual(self.cont.nume,"test_1")
        self.assertEqual(self.cont.credit,0)
        self.assertEqual(self.cont.tipCont,"RON")

    def testDb(self):
        cont = Cont.objects.get(slug = self.cont.nume)
        self.assertEqual(self.cont, cont) 