from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://mail.google.com"
EMAIL = "lmoshe670@gmail.com"
PASSWORD = "mmmlll12345"
MAX_WAIT = 10  # seconds


class GmailAutomation:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.waiter = WebDriverWait(self.driver, MAX_WAIT)

    def enter_email(self):
        self.waiter.until(EC.element_to_be_clickable((By.ID, "identifierId")))
        login_bar = self.driver.find_element(By.ID, "identifierId")
        login_bar.send_keys(EMAIL)
        login_bar.send_keys(Keys.ENTER)  # press enter

    def enter_password(self):
        self.waiter.until(EC.element_to_be_clickable((By.NAME, "Passwd")))
        login_bar = self.driver.find_element(By.NAME, "Passwd")
        login_bar.send_keys(PASSWORD)
        login_bar.send_keys(Keys.ENTER)  # press enter

    def login(self):
        try:
            self.driver.get(URL)
        except:
            print("Invalid URL")
            breakpoint()
        self.enter_email()
        self.enter_password()


    def click_primary_tab(self):
        try:
            self.waiter.until(EC.element_to_be_clickable((By.CLASS_NAME, "aKz")))
            promotion_button = self.driver.find_element(By.CLASS_NAME, "aKz")
            promotion_button.click()
        except:
            print("Loading took too much time!")
            breakpoint()


    def get_count_total_emails(self):

        self.waiter.until(EC.element_to_be_clickable((By.CLASS_NAME, "aKz")))
        total_emails = self.driver.find_element(By.XPATH,
                                                '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[1]/span/div[1]/span/span[1]/span[2]').text
        return total_emails

    def get_all_sender_names(self):
        self.waiter.until(EC.element_to_be_clickable((By.CLASS_NAME, "aKz")))

        senders = self.driver.find_elements(By.CLASS_NAME, "yW ")
        senders_names = []
        for sender in senders:
            senders_names.append(sender.text)
        return senders_names

    def get_all_subjects(self):
        self.waiter.until(EC.element_to_be_clickable((By.CLASS_NAME, "aKz")))

        subjects = self.driver.find_elements(By.CLASS_NAME, "y6")
        subjects_names = []
        for subject in subjects:
            subjects_names.append(subject.text)
        return subjects_names

    def get_sender_and_subject_of_email(self, index_of_email: int):
        """Get a number of an email in the list and return his sender and subject."""
        self.waiter.until(EC.element_to_be_clickable((By.CLASS_NAME, "aKz")))

        all_senders = self.get_all_sender_names()
        specific_sender = all_senders[index_of_email]
        all_subjects = self.get_all_subjects()
        specific_subject = all_subjects[index_of_email]
        email = f"{specific_sender} : {specific_subject}"
        return email


def main():
    gmail_automation = GmailAutomation()
    gmail_automation.login()
    gmail_automation.click_primary_tab()
    total_emails = gmail_automation.get_count_total_emails()
    print(f"total emails is: {total_emails}")
    mail_master = int(input(print("which mail master?")))
    # print(gmail_automation.get_all_sender_names())
    # print(gmail_automation.get_all_subjects())
    if (mail_master >= 0) and (mail_master < int(total_emails)):
        print(gmail_automation.get_sender_and_subject_of_email(mail_master))
    else:
        print("requested email number doesn't exist")


if __name__ == '__main__':
    main()
