# do not test directly
# similar to singleton example in class, USE (CLS)

import yagmail
import keyring


class Emailer:

    _sender_address = ""
    _sole_instance = None # the only instance of this class

    # sets the class variable as specified
    @classmethod
    def configure(cls, sender_address):
        cls._sender_address = sender_address

    # return the only instance of this class
    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
            return cls._sole_instance

    # https://pypi.org/project/yagmail/#description
    # from the pypi.org website, example description
        # https://github.com/kootenpv/yagmail/blob/master/yagmail/__main__.py
    def send_plain_email(self, recipients, subject, message):
        try:
            yag = yagmail.SMTP(self._sender_address)
            yag.send(recipients, subject, message)
            print("Email sent!")
        except Exception as error:
            print("An error occurred while sending.", error)



if __name__ == '__main__':
    Emailer.configure('alysonlfutral@gmail.com')
    recipients = ['leighann98dance@gmail.com']
    subject = 'Test Subject'
    message = 'This is a test message.'
    emailer = Emailer.instance()
    emailer.send_plain_email(recipients, subject, message)
