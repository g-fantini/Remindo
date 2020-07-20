from django.test import TestCase
from register.forms import ProfileRegisterForm

class ProfileRegisterFormTests(TestCase):
    def test_clean_phone(self):
        form = ProfileRegisterForm(data={"phone": "07566832293"})
        self.assertTrue(form.is_valid())
        
        form = ProfileRegisterForm(data={"phone": "7566832293"})
        self.assertEqual(form.errors["phone"], ["Invalid phone number"])
        
        form = ProfileRegisterForm(data={"phone": "0756683229"})
        self.assertEqual(form.errors["phone"], ["Invalid phone number"])
        
        form = ProfileRegisterForm(data={"phone": "0756683s29"})
        self.assertEqual(form.errors["phone"], ["Invalid phone number"])
        
        form = ProfileRegisterForm(data={"phone": "0756683229000"})
        self.assertEqual(form.errors["phone"], ["Invalid phone number"])

    