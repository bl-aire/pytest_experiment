# To test sending email from one user to another: 
# .....make each user.....send the email from one user to the other..... assert that the other user received that message in their inbox.

# To clean up after test runs:
# .....make sure the other user’s mailbox is emptied before deleting that user

import pytest
from emaillib import Email, MailAdminClient

@pytest.fixture
def mail_admin():
    return MailAdminClient()


@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)


@pytest.fixture
def receiving_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    user.clear_mailbox()
    mail_admin.delete_user(user)


def test_email_received(sending_user, receiving_user):
    email = Email(subject="Hey!", body="How's it going?")
    sending_user.send_email(email, receiving_user)
    assert email in receiving_user.inbox


# Because receiving_user is the last fixture to run during setup, it’s the first to run during teardown.