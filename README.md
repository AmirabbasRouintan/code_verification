# Code Verification
This is a Python script that sends an HTML-based email with a verification code to a user's email address.

## Features
***Send Emails***: The script uses the `smtplib` library to send emails to users.
***Generate Random Codes***: The script generates random codes for each user and includes them in the email message.
***Verify User Input***: The script prompts users to enter their verification code, and verifies that it matches the randomly generated code.

## How It Works
1. ***Get User Input***: The script asks the user to input their name and email address.
2. ***Generate Random Code***: The script generates a random code for the user.
3. ***Send Email***: The script sends an email to the user with the random code included in the message.
4. ***Verify User Input***: The script prompts the user to enter their verification code, and verifies that it matches the randomly generated code.

## Requirements
* Python 3.x
* `smtplib` library (comes with Python)
* `email.mime.multipart`, `email.mime.text`, and `email.mime.application` libraries (comes with Python)

## Installation
To install this script, simply download or clone the repository and run the `send_email.py` file using your preferred Python interpreter.

## Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request. I'm always happy to receive feedback and improvements!



![Screenshot 2024-06-14 174858](https://github.com/AmirabbasRouintan/code_verification/assets/110909074/a2884760-d104-4172-99d3-5bdbfd0cc3aa)
