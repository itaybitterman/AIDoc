from unittest import TestCase

import characteristcs
from characteristcs import Subject, ImportantWords, AttachedFiles


class TestCharacteristics(TestCase):
    def test_subject_low_priority(self):
        subject = Subject('low')
        priority = subject.calculate_priority()
        self.assertEqual(priority, 0.1)

    def test_subject_medium_priority(self):
        subject = Subject('medium')
        priority = subject.calculate_priority()
        self.assertEqual(priority, 0.5)

    def test_subject_high_priority(self):
        subject = Subject('high')
        priority = subject.calculate_priority()
        self.assertEqual(priority, 0.9)

    def test_subject_invalid_symbol(self):
        subject = Subject('fake')
        priority = subject.calculate_priority()
        self.assertEqual(priority, None)

    def test_important_words_low_priority(self):
        important_words = ImportantWords('Hi Moshe, this is a spam message ')
        priority = important_words.calculate_priority()
        self.assertEqual(priority, 0.1)

    def test_important_words_medium_priority(self):
        important_words = ImportantWords('Good evening Moshe, I am attaching the taxes you will have to pay')
        priority = important_words.calculate_priority()
        self.assertEqual(priority, 0.5)

    def test_important_words_high_priority(self):
        important_words = ImportantWords(
            'Good evening Moshe, your tests showed that you have high blood pressure and you must return to the hospital for repeat tests')
        priority = important_words.calculate_priority()
        self.assertEqual(priority, 0.9)

    def test_attached_files_low_priority(self):
        attached_files = AttachedFiles(0)
        priority = attached_files.calculate_priority()
        self.assertEqual(priority, 0.1)

    def test_attached_files_medium_priority(self):
        attached_files = AttachedFiles(4)
        priority = attached_files.calculate_priority()
        self.assertEqual(priority, 0.5)

    def test_attached_files_high_priority(self):
        attached_files = AttachedFiles(10)
        priority = attached_files.calculate_priority()
        self.assertEqual(priority, 0.9)

    def test_final_priority_in_range(self):
        """check if the final priority of the email is between 0 to 1"""
        attached_files = AttachedFiles(4)
        important_words = ImportantWords(
            'Good evening Moshe, your tests showed that you have high blood pressure and you must return to the hospital for repeat tests')
        subject = Subject('low')

        final_priority = characteristcs.calculate_final_priority(subject, attached_files, important_words)
        self.assertTrue(0 <= final_priority <= 1)

    def test_final_priority(self):
        attached_files = AttachedFiles(4)
        important_words = ImportantWords('Hi Moshe, this is a spam message')
        subject = Subject('high')

        final_priority = characteristcs.calculate_final_priority(subject, attached_files, important_words)
        self.assertEqual(final_priority,0.5)
