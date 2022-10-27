class Email:
    def __init__(self, priority: float):
        self.priority = priority

    def __str__(self):
        return f"Email({self.priority})"


class Amy:


    def __init__(self, max_mails: int):
        self.mails: list[Email] = []
        self.max_mails = max_mails

    def insert_mail(self, new_mail: Email):
        self.mails.append(new_mail)
        self.mails.sort(key=lambda mail: mail.priority, reverse=True)
        self.mails = self.mails[:self.max_mails]  # In case the inbox is full, remove the last one.

    def __str__(self):
        all_mails = ','.join(map(str, self.mails))
        return f"Inbox([{all_mails}])"


if __name__ == '__main__':
    amy = Amy(20)
