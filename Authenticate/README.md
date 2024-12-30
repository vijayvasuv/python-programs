# AUTH APP
    #### Summary: Login using an one-time passcode.
    #### Description: AUTH APP is an authentication application which helps the user to login using an email ID and an one-time passcode that will be sent to the provided email address.
    User is prompted to enter an email ID. Any incorrect input is considered as an expection and handled with a proper message, so the user can re-enter. Once the email is valid, the application generates an one-time passcode and sends it the email address provided by the user. The user must enter the one-time passcode and if the code matches, the user logs in to the application. If the user inputs incorrect passcode on three attempts, login is denied.


# authenticate.py
    #### Description: This file contains a main and three different functions.

         main()
         #step1: Prompts the user for an email ID and passes it to the validate_email function to validate it.
         #step2: Handles exception returned by validate_email for email ID and prints appropriate message to user.
         #step3: Calls generate_code to generate a 6 digit one-time passcode.
         #step4: Calls send_email to send email with the generated passcode to the user input email address
         #step5: Calls function login_app to validate user input

         validate_email()
         #parameter: expects a valid email ID from user
         #logic: Uses validators to check the user input and raise exception in case of any error.
         #output: returns the valid email address

         generate_code()
         #parameter: NA
         #logic: Generates a 6 digit passcode using random module
         #output: returns the geneated 6 digit passcode

         send_email()
         #parameter: 6 digit code from generate_code function and email address from validate_email function
         #logic: Sends email using smtplib
         #output: Email with the one-time passcode

         login_app()
         #parameter: 6 digit code from generate_code function
         #logic: Compares the 6 digit geneated code with the user input. If it matches, user logs-in else login is denied
         #output: User logs-in or denied based on user input



# test_authenticate.py
    #### Description: This is the unit test file for authenticate.py. It has two functions each corresponding to the one in authenticate.py
        test_validate_email()
        #test: assert user input for valid, invalid and ValueError

        test_generate_email()
        #test: assert generated code for length of 6

# requirement.txt
    #### Description: List the required pip install to run the program


