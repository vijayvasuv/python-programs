# FLICK IN
    #### Video Demo: https://youtu.be/cV0DErMskas
    #### Summary: FLICK IN displays movie/show details
    #### Description: FLICK_IN is an application which can be used to retrieve movie/show (FLICK) details (IN) - Name, Genre, Plot, Rated and imdbRating.
    User is prompted to enter the name of the flick he wishes to know more about. Any incorrect input is handled with a proper message, so the user can
    re-enter the name. Once the name is valid, the application connects to an external API. The API connects to imdb and retrieves the results, if the
    name matches any of the flicks in it's database. If the flick doesn't match, the application shows a message to user and request to try with the correct
    flick name. If the flick name matches, the API returns a JSON which is stored in a Dict. The application prints the formated flick results to the user. The user is provided with another feature of saving the flick results for offline viewing purpose. The application prompts for user permission to save results, if the user agrees then data is saved to a txt file in append mode so all data remains for use in future and application exists with a greeting. If the user doesn't agree to save, application exists with a greeting. User can choose to save or not save each time they use the application. However, data saved already will remain and can be removed only when the file is deleted.
    Binge Watch!


# project.py
    #### Description: This file contains a main and three different function.

         main()
         #step1: prompts the user for name and passes valid value to get_input() function. If an exception occurs, it prints a message
         and prompts again.
         #step2: If the API returns valid value, the results are printed to user. If an exception occurs, the control is passed to get_input()
         to get correct name.
         #step3: prompts the user for input regarding saving the results. If an exception occurs, it prints a message and prompts again. If the
         input is valid, data is saved to file or skipped.

         get_input()
         #parameter: expects a valid name from user
         #logic: raises TypeError if the input is invalid
         #output: returns the valid name

         api_call()
         #parameter: the output of get_input() function
         #logic: connect to the API with the parameter value and captures the result in a Dict. If the Dict is empty, it raises a KeyError and
         returns to get_input() function to get a valid movie name
         #output: returns the Dict with the movie/show details

         save_result()
         #parameter: expects a valid input (yes/no) from user
         #logic: if the user agrees to save the result, the data in Dict is written to myfile.txt, else the program will end with a message
         #output: Greeting to user based on the input

# test_project.py
    #### Description: This is the unit test file for project.py. It has three functions each corresponding to the one in project.py
        test_get_input()
        #test: assert user input for valid, invalid and TypeError

        test_api_call()
        #test: assert API call to return a Dict and KeyError

        test_save_result()
        #test: assert user input for TypeError and return values based on the input

# requirements.txt
    #### Description: List the pre-requisities required to run the program
        #install: pip install requests
        #logic: to use this for API call

# myfile.txt
    #### Description: txt file to save API results, if user agrees for offline viewing purpose
        #logic: if user input to test_save_result() is "yes", then data is saved to this file - myfile.txt
