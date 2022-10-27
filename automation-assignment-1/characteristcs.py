class Subject:
    def __init__(self, priority_symbol: str):
        self.priority_symbol = priority_symbol

    def calculate_priority(self) -> float:
        if self.priority_symbol == 'low':
            return 0.1
        elif self.priority_symbol == 'medium':
            return 0.5
        elif self.priority_symbol == 'high':
            return 0.9


class AttachedFiles:
    def __init__(self, num_of_files: int):
        self.num_of_files = num_of_files

    def calculate_priority(self) -> float:
        if self.num_of_files <= 1:
            return 0.1
        elif 1 < self.num_of_files <= 8:
            return 0.5
        elif self.num_of_files > 8:
            return 0.9


class ImportantWords:
    def __init__(self, mail_content: str):
        self.mail_content = mail_content

    def calculate_priority(self) -> float:
        important_words = ['loan', 'interest', 'credit', 'asset', 'liability', 'income', 'expenses', 'investment',
                           'stocks', 'taxes', 'refinancing', 'blood ', 'high', 'cut', 'biopsy', 'body',
                           'inpatient', 'outpatient','tests','pressure', 'hospital']
        count_words_in_mail = 0
        for word in important_words:

            if word in self.mail_content:
                count_words_in_mail += 1

        if count_words_in_mail == 0:
            return 0.1
        elif 0 < count_words_in_mail <= 3:
            return 0.5
        elif count_words_in_mail > 3:
            return 0.9


def calculate_final_priority(subject_characteristic: Subject, attached_files_characteristic: AttachedFiles,
                             important_words_characteristic: ImportantWords) -> float:
    subject_priority = subject_characteristic.calculate_priority()
    attached_files_priority = attached_files_characteristic.calculate_priority()
    important_words_priority = important_words_characteristic.calculate_priority()
    final_priority = (subject_priority + attached_files_priority + important_words_priority) / 3
    return final_priority
