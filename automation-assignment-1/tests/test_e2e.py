from random import random
from unittest import TestCase

from selenium.webdriver.firefox import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from e2e import GmailAutomation

URL = "https://mail.google.com"
EMAIL = "lmoshe670@gmail.com"
PASSWORD = "mmmlll12345"
MAX_WAIT = 10  # seconds


class TestE2e(TestCase):

    def setUp(self):
        """Login to the gmail account automatically ."""
        self.gmail_automation = GmailAutomation()
        self.gmail_automation.login()

    def test_total_emails(self):
        """"checks if the total emails of products true."""

        current_total_emails = self.gmail_automation.get_count_total_emails()
        self.assertEqual(int(current_total_emails), 6)


    def test_email_sender(self):
        """check the value of sender"""

        sender_of_third_email = self.gmail_automation.get_all_sender_names()[2]
        self.assertEqual(sender_of_third_email, 'Tripadvisor')

    def test_email_subject(self):
        """check the value of subject"""
        subject_of_third_email = self.gmail_automation.get_all_subjects()[2]
        self.assertEqual(subject_of_third_email, 'Welcome to better travel')



    def test_total_email(self):
        """checks the sender and subject of a selected email """
        email_number_6 = self.gmail_automation.get_sender_and_subject_of_email(5)
        self.assertEqual(email_number_6 , 'Google Community Te. : Moshe, finish setting up your new Google Account')
