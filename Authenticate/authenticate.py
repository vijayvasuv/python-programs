import validators
import smtplib
import sys
import string
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main():
    while True:
        try:
            value = input("Enter your email to login: ")
            #valdiates the input email from user
            email = validate_email(value)
        except ValueError:
            print("Incorrect email format, please re-try!")
        else:
            #generates the one-time passcode
            key = generate_code()
            #send email to the user provided valid email ID with the generated one-time passcode
            send_email(email, key)
            #validate user input against the one-time passcode for login
            login_app(key)


def validate_email(e):
    if validators.email(e):
        return e
    else:
        raise ValueError

def generate_code():
    character = string.digits + string.ascii_letters
    result = ""
    for _ in range(6):
    #use random to generate
        result += random.choice(character)
    return result

def send_email(receiver, code):
    # Configuration
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    EMAIL_ADDRESS = ""#your email ID
    EMAIL_PASSWORD = ""#your app password

    # Email content
    subject = "Your One-Time Passcode"
    body = f"""\
    Dear User,

    Use below code to sign-in.
    {code}

    Best,
    AUTH APP
    """

    # Create the email
    message = MIMEMultipart()
    message["From"] = EMAIL_ADDRESS
    message["To"] = receiver
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, receiver, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        sys.exit(f"Error: {e}. Please try again later!")


def login_app(actual):
    i = 0
    #provide three attempts to input correct passcode before exit
    while i<=2:
        response = input("Enter the one-time passcode: ")
        if actual == response:
            sys.exit("Login success. Welcome to myWorld!")
        else:
            print("Incorrect passcode. Please re-try!")
            i+=1
    sys.exit("Login denied!" )

if __name__ == "__main__":
    main()
