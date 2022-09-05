import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertNotEqual(englishToFrench("Thank you"),"Merci")
        self.assertEqual(englishToFrench("Girl"),"Fille")
        #self.assertRaises(englishToFrench(""))

class TestFrenchTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        self.assertEqual(frenchToEnglish("Merci"),"Thank you")
        self.assertNotEqual(frenchToEnglish("Fille"),"Girl")
        #self.assertRaises(frenchToEnglish(""))


unittest.main()
