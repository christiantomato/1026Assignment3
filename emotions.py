# add a comment here with your name, email, and student number
# you can not add any import lines to this file

EMOTIONS = ['anger', 'joy', 'fear', 'trust', 'sadness', 'anticipation']


def clean_text(comment):
    #replace any characters that are not letters with a space and convert to lowercase

    cleaned_string = ""

    for char in comment:
        #if not in the alphabet
        if not char.isalpha():
            #add space instead
            cleaned_string += " "
        else:
            #just add normally and lowercase it
            char = char.casefold()
            cleaned_string += char

    return cleaned_string


def make_keyword_dict(keyword_file_name):
    # make a dictionary with the keys being the words, and the values as a dictionary of each emotion value
    words_dict = {}

    #open up the file to read from it
    file = open(keyword_file_name)

    for line in file:
        #strip any leading or trailing white space
        line = line.strip()
        #now we want to split using tab as a seperator
        line = line.split("\t")

        #make a dictionary with the emotion values
        emotions_dict = {
            "anger": int(line[1]),
            "joy": int(line[2]),
            "fear": int(line[3]),
            "trust": int(line[4]),
            "sadness": int(line[5]),
            "anticipation": int(line[6])
        }

        #add it to the dictionary
        words_dict[line[0]] = emotions_dict

    return words_dict


def classify_comment_emotion(comment, keywords):
    #counters for each emotion
    anger = 0
    joy = 0
    fear = 0
    trust = 0
    sadness = 0
    anticipation = 0

    #first clean the comment
    comment = clean_text(comment)
    #split the comment into words
    comment = comment.split()

    #loop through the entire list of words
    for word in comment:
        #if the word is in the keywords dictionary
        if word in keywords:
            #total up its score
            anger += keywords[word]["anger"]
            joy += keywords[word]["joy"]
            fear += keywords[word]["fear"]
            trust += keywords[word]["trust"]
            sadness += keywords[word]["sadness"]
            anticipation += keywords[word]["anticipation"]

    #put all the scores and their names into a list
    emotions_scores = [anger, joy, fear, trust, sadness, anticipation]

    #loop through the scores and find the highest
    #starting with anger as the sentinel will ensure correct order if ties are present
    comment_emotion = "anger"
    highest_score = anger
    for i in range(len(emotions_scores)):
        #if the score is higher than current
        if emotions_scores[i] > highest_score:
            #set new current highest score and also set the name of the emotion
            comment_emotion = EMOTIONS[i]
            highest_score = emotions_scores[i]

    return comment_emotion


def make_comments_list(filter_country, comments_file_name):
    #make a list with each entry being a dictionary with the comment information
    comment_list = []

    #open up the file to read from it
    file = open(comments_file_name)

    #correct country
    same_country = False

    for line in file:
        #strip any leading or trailing whitespace
        line = line.strip()
        #split into a list using the comma as the delimiter
        line = line.split(",")
        #strip the comment text of any whitespace
        line[3] = line[3].strip()

        #check if correct country
        if filter_country in line[2]:
            same_country = True

        #add it to the list if country matches or all was requested
        if same_country or "all" in filter_country:
            #make a dictionary with the comment info
            comment_dict = {
                "comment_id": int(line[0]),
                "username": line[1],
                "country": line[2],
                "text": line[3]
            }

            #add it to the list
            comment_list.append(comment_dict)

            #reset the country variable
            same_country = False

    return comment_list


def make_report(comment_list, keywords, report_filename):
    # add your code here and remove the pass keyword on the next line
    pass

