from random import random
from unittest import TestCase

from amy import Email, Amy


def generate_random_mail():
    """Generate random mail."""
    random_priority = random()
    return Email(random_priority)


def generate_random_mails(num_mails: int) -> list[Email]:
    mails = []
    for mail in range(num_mails):
        mails.append(generate_random_mail())
    return mails


class TestAmy(TestCase):

    def test_insert_new_mail(self):
        mail = Email(0.5)
        inbox = Amy(20)
        inbox.mails = [Email(0.3), Email(0.7)]
        """check that amy was resorted according to priority"""
        inbox.insert_mail(mail)
        self.assertIs(inbox.mails[1], mail)
        self.assertIn(mail, inbox.mails)

    def test_insert_least_important_and_amy_full(self):
        """Check that if amy is full and the user tries to insert least important mail, it will not be inserted."""
        mail = Email(0.1)
        inbox = Amy(3)
        inbox.mails = [Email(0.3), Email(0.5), Email(0.7)]
        inbox.insert_mail(mail)
        self.assertNotIn(mail, inbox.mails)

    def test_insert_mail_and_amy_full(self):
        """
        Check that if amy is full and the user tries to insert regular mail, it will be inserted,
        and the currently least important mail will be removed.
        """
        mail = Email(0.4)
        inbox = Amy(3)
        inbox.mails = [Email(0.3), Email(0.5), Email(0.7)]
        inbox.insert_mail(mail)

        self.assertNotEqual(inbox.mails[2].priority, 0.3)
        self.assertEqual(inbox.mails[2].priority, 0.4)
