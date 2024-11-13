# add a comment here with your name, email, and student number.
# do not add any additional import lines to this file.

import os.path
from emotions import *

VALID_COUNTRIES = ['bangladesh', 'brazil', 'canada', 'china', 'egypt',
                   'france', 'germany', 'india', 'iran', 'japan', 'mexico',
                   'nigeria', 'pakistan', 'russia', 'south korea', 'turkey',
                   'united kingdom',  'united states']


def ask_user_for_input():
    #booleans to keep track of what was successful
    keywords_valid = False
    comments_valid = False
    country_valid = False
    report_valid = False

    #make sure each individual input is good
    while not keywords_valid:
        #getting an input
        keyword_filename = input("Input keyword file (ending in .tsv): ")

        #check for invalid input
        if not keyword_filename.endswith(".tsv"):
            #we have a problem
            raise ValueError("Keyword file does not end in .tsv!")
        #check for file existence
        if not os.path.exists(keyword_filename):
            #does not exist
            raise IOError(keyword_filename + " does not exist!")

        #if we get to this point we are okay
        keywords_valid = True

    while not comments_valid:
        #getting an input
        comments_filename = input("Input comment file (ending in .csv): ")

        #check for invalid input
        if not comments_filename.endswith(".csv"):
            #we have a problem
            raise ValueError("Comments file does not end in .csv!")
        #check for file existence
        if not os.path.exists(comments_filename):
            #does not exist
            raise IOError(comments_filename + " does not exist!")

        #if we get to this point we are okay
        comments_valid = True

    while not country_valid:
        #getting an input
        country = input("Input a country to analyze (or 'all' for all countries): ").lower()

        #go through valid countries and check if there is a match
        if not(country in VALID_COUNTRIES or country == "all"):
            #there is a problem
            raise ValueError(country + " is not a valid country to filter by!")

        #if we get here we are fine
        country_valid = True

    while not report_valid:
        #getting an input
        report_filename = input("Input the name of the report file (ending in .txt): ")

        #check for invalid input
        if not report_filename.endswith(".txt"):
            #we have a problem
            raise ValueError("Report file does not end in .txt!")
        #check for existing file
        if os.path.exists(report_filename):
            #already exists
            raise IOError(report_filename + " already exists!")

        #if we get here we are okay
        report_valid = True

    return keyword_filename, comments_filename, country, report_filename


def main():
    #ask for input, watch out for exceptions
    valid_input = False
    while not valid_input:
        try:
            info = ask_user_for_input()
            #everything good
            valid_input = True
        except Exception as e:
            print(e)

    #analyze info
    print("Most common emotion is: " + make_report(make_comments_list(info[2], info[1]), make_keyword_dict(info[0]), info[3]))

if __name__ == "__main__":
    main()
