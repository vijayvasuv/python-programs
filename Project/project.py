#import used to work with API
import requests
import sys
#Dict to store results of API, print to user and write to file
results = {}

def main():
    while True:
        try:
            #get name of movie/show from user
            name = input("Enter the Flick: ").strip().lower()
            #function to check if user input is valid
            get_input(name)
            #function to call API, store result in Dict and print to user
            results = api_call(name)
            for key, value in results.items():
                print("%s: %s" % (key, value))
            break

        except (TypeError, KeyError):
            print("Flick not available, please re-try.")

    while True:
        try:
            #get user input to save results in a file
            final_step = input("Do you want to save the results? (yes/no) ").strip().lower()
            #function to check user input and decide to write to file or skip
            print(save_result(final_step))
            sys.exit(0)

        except TypeError:
            print("Invalid value, please re-try.")


def get_input(value):
    if value == "":
        raise TypeError
    else:
        return value

def api_call(input):
    #API call
    response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=4df8194d&t="+input)
    o = response.json()
    if o == "":
        raise KeyError
    else:
        #store results to Dict
        results["Movie"] = o["Title"]
        results["Genre"] = o["Genre"]
        results["Plot"] = o["Plot"]
        results["Rated"] = o["Rated"]
        results["imdb Rating"] = o["imdbRating"] + "/10"
        return results

def save_result(next_step):
    if next_step not in ("yes", "no"):
        raise TypeError
    elif next_step == "yes":
        #create/append movie results to txt file
        with open("myfile.txt", "a") as f:
            for key, value in results.items():
                f.write("%s: %s\n" % (key, value))
        return "Data saved in myfile.txt. Binge-watch!"
    else:
        return "Thanks, Binge-watch!"

if __name__ == "__main__":
    main()


