from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY

FROM_EMAIL = 'tasknotifier0@gmail.com'


def send_email(to_email, subject, content):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        plain_text_content=content + 'hello',
        html_content=f'<p>{content}</p>'
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        if response.status_code == 202:
            return True, "Email accepted for delivery."
        else:
            return False, "Failed to send email." + \
                          f"Status code: {response.status_code}"
    except Exception as e:
        return False, f"Error sending email: {e}"
