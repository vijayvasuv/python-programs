# PASS GEN
    #### Summary: Generate random password.
    #### Description: PASS GEN is an application which generates random passwords of length requested by the user.
    User is prompted to enter a number. Any incorrect input is handled with a proper message, so the user can
    re-enter. Once the number is valid, the application uses random module. A password of the given lenth is generated
    and returned to the user. The user can re-run and generate password of desired length multiple times.


# password.py
    #### Description: This file contains a main and a function.

         main()
         #step1: Prompts the user for a positive number and passes the value to generate_password() function.
         #step2: Print the return value from generate_password() which is the generated password back to the user
         #step3: If an exception occurs, the control is retunred to main, it prints a message and prompts again.

         generate_password()
         #parameter: expects a valid number from user
         #logic: Uses random class to generate value of length given by user. Also raises ValueError if the input is invalid
         #output: returns the generated password


# test_password.py
    #### Description: This is the unit test file for password.py. It has one function each corresponding to the one in project.py
        test_generate_password()
        #test: assert user input for valid, invalid and ValueError


