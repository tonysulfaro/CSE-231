##################################################################################################
#   Project 09 - Twitter Data
#
#   import dependencies
#   initialize months
#   open file function
#       prompts for filename and returns filepointer if name is valid
#   validate hashtag function
#       check if there is a hashtag in string
#           remove hashtag to evaluate string
#           if theres punctuation or theres only a single number return false
#   get hashtags function
#       takes a tweet and extracts all hashtags out and puts them into a list
#       return hashtag list
#   read data function
#       recieve filepointer
#       for each line in the filepointer
#           slice out data
#           get hashtags from tweet
#           add items to list
#       return master list of data
#   get histogram tag count for users function
#       initialize empty dictionary
#       for each entry in data_list
#           slice out username
#           if the user is in usernames
#               add hashtag to data dictionary/ increment occurances by 1
#       return didctionary of twitter data
#   get tags for month by users function
#       initialize list of months and sets
#       for each list of data in data
#       slice out twitter information
#           if username in username list
#               for each tag in hashtags in tweet
#                   add hashtag to set in data list
#       return list of month numbers and sets of hashtags
#   get user names function
#       takes a list of twitter data and extracts all unique usernames
#       returns list of usernames
#   thee most common hashtags combined
#       fetch data dictionary from get_histogram_tag_count_for_users function
#       sort the dictionary into a list by hashtag occurance
#       slice out top 3 list entries
#       return top 3 hashtags and their counts in list form
#   three most common hashtags individual
#       takes twitter data and finds 3 most used hashtags for each username
#       returns list of usernames, list of hashtags and counts
#   similarity function
#       takes list of twitter data and compares hashtag usage between two users
#       returns list of months and intersections of hashtags
#   plot similarity function
#       plots similarity between two users and hashtags
#   get first second usernames function
#       prompts the user to enter two twitter usernames
#       returns two usernames when input is correct
#   main function
#        Open the file
#        Read the data from the file
#        Create username list from data
#        Calculate the top three hashtags combined for all users
#            Print them
#        Calculate the top three hashtags individually for all users
#            Print them
#        Prompt for two user names from username list
#        Calculate similarity for the two users
#            Print them
#        Prompt to plot or not and plot if 'yes'
#   if name is main call main
##################################################################################################

import string, calendar, pylab

MONTH_NAMES = [calendar.month_name[month] for month in range(1, 13)]

def open_file():
    """
        prompts for input with the given prompt passed as message
        catches if file isnt there and prompts again
        exits when it can open the file
        :param message - prompt as string:
        :return fp - file pointer:
        """
    while True:
        file_name = input("Input a filename: ")
        try:
            fp = open(file_name)
            break
        except FileNotFoundError:
            print("Error in input filename. Please try again.")
            continue
    return fp

def validate_hashtag(s):
    """
    recieve hashtag as string
    if theres a hashtag remove it and continue on with examination
    if the string has punctuation or is just  single number return false
    :param s - string - hashtag:
    :return boolean - if string is valid hashtag:
    """

    if "#" in s:
        s = s[1:]
        s = set(s)

        if s.intersection(string.punctuation) != set():
            return False
        elif len(s) == 1:
            if s.intersection(string.digits) != set():
                return False
        else:
            return True
    else:
        return False

def get_hashtags(s):
    """
    recive tweet as a string
    split tweet on spaces
    for each word in the tweet
        if its a valid hashtag add it to the list
    :param s - string - tweet from file:
    :return hashtag_list - list of hashtags in each tweet:
    """

    hashtag_list = list()

    s = s.split(" ")

    for item in s:
        if validate_hashtag(item):
            hashtag_list.append(item)

    return hashtag_list

def read_data(fp):
    """
    initialize empty list
    for each line in the filepinter
        slice out twitter data
        extract hashtags from tweet
        make list out of user data and list of hashtags
        add list to master list of twitter data
    :param fp - filepointer - source twitterdata csv:
    :return data_list - list of lists of tweets:
    """

    data_list = list()

    for line in fp:

        tweet_list = list()

        line = line.strip().split(',')

        user_name = line[0]
        month_number = int(line[1])
        tweet = line[2]

        hashtag_list = get_hashtags(tweet)

        #create 3-entry list of data
        tweet_list.append(user_name)
        tweet_list.append(month_number)
        tweet_list.append(hashtag_list)

        #append 3-entry list to data list
        data_list.append(tweet_list)

    return data_list

def get_histogram_tag_count_for_users(data, usernames):
    """
    initialize empty dictionary
    for each entry in data_list
        slice out username
        if the user is in usernames
            add hashtag to data dictionary/ increment occurances by 1
    :param data - list of twitter data with usernames, months, and list of hashtags:
    :param usernames - list - usernames from file:
    :return data_dictionary - dicitionary of twitter data:
    """

    data_dictionary = dict()

    for lists in data:

        username = lists[0]
        hashtags = lists[2]

        if username in usernames:

            for tag in hashtags:
                if tag not in data_dictionary:
                    data_dictionary[tag] = 0
                data_dictionary[tag] += 1

    return data_dictionary

def get_tags_by_month_for_users(data , usernames):
    """
    initialize list of months and sets
    for each list of data in data
        slice out twitter information
        if username in username list
            for each tag in hashtags in tweet
                add hashtag to set in data list
    :param data - list of twitter data:
    :param usernames - list of usernames in twitter data:
    :return data_list - list of month numbers and set of unique hashtags:
    """

    data_list = [(i, set()) for i in range(1, 13)]

    for lists in data:

        username = lists[0]
        month = lists[1]-1
        hashtags = lists[2]

        if username in usernames:

            for tag in hashtags:
                data_list[month][1].add(tag)

    return data_list

def get_user_names(L):
    """
    for each line in twitter data
        slice out username
        if its not in username list add it
    :param L - list of twitter data:
    :return user_names - list of user names:
    """

    user_names = list()

    for item in L:

        user_name = item[0]

        if user_name not in user_names:
            user_names.append(user_name)

    user_names = sorted(user_names)

    return user_names

def three_most_common_hashtags_combined(L, usernames):
    """
    fetch data dictionary of twitter data
    find top 3 hashtags by sorting it
    :param L - list of twitter data:
    :param usernames - list of usernames:
    :return list of top three hashtags and their counts:
    """

    data_dictionary = get_histogram_tag_count_for_users(L, usernames)
    data_list = sorted([(v, k) for k, v in data_dictionary.items()], reverse= True)[:3]

    return data_list

def three_most_common_hashtags_individuals(data_lst, usernames):
    """
    for each user in usernames
        find their highest counts of hashtags and counts
        for item in highest counts list
            extract data and create tuple
            add tuple to list
    :param data_lst - list of twitter data:
    :param usernames - list of usernames:
    :return individual_data - list of users and their highest used hashtags:
    """

    individual_data = list()

    for user in usernames:

        highest_counts = get_histogram_tag_count_for_users(data_lst, user)
        highest_counts = sorted([(v, k) for k, v in highest_counts.items()], reverse=True)

        for item in highest_counts:
            hashtag_count = item[0]
            hashtag = item[1]
            tup = (hashtag_count, hashtag, user)
            individual_data.append(tup)

    individual_data = sorted(individual_data, reverse=True)[:3]

    return individual_data

def similarity(data_lst, user1, user2):
    """
    gets list of sets of hashtags for both users
    for each item in user lists
        find intersection of hashtags
        add intersection to intersection list at that month
    :param data_lst - list of twitter data:
    :param user1 - first twitter user entered by user:
    :param user2 - second twitter user entered by user:
    :return intersection list - list of intersections of hashtags by users:
    """

    user1_list = get_tags_by_month_for_users(data_lst, [user1])
    user2_list = get_tags_by_month_for_users(data_lst, [user2])
    intersection_list = list()

    for x in range(len(user1_list)):

        user1_set = set(user1_list[x][1])
        user2_set = set(user2_list[x][1])

        common = (user1_set.intersection(user2_set))

        tup = (x+1, common)
        intersection_list.append(tup)

    return intersection_list

def plot_similarity(x_list,y_list,name1,name2):
    """
    take lists and names and plot similarity
    :param x_list - list of x values:
    :param y_list - list of y values:
    :param name1 - first user entered:
    :param name2 - second user entered:
    :return <none> :
    """
    
    pylab.plot(x_list,y_list)
    pylab.xticks(x_list,MONTH_NAMES,rotation=45,ha='right')
    pylab.ylabel('Hashtag Similarity')
    pylab.title('Twitter Similarity Between '+name1+' and '+name2)
    pylab.tight_layout()
    pylab.show()
    # the next line is simply to illustrate how to save the plot
    # leave it commented out in the version you submit
    #pylab.savefig("plot.png")

def get_first_second_usernames(user_name_list):
    """
    prompt for two user names sperated by comma
    check if input is valid and exists in list of user names
        if its not reprompt
    :param user_name_list - list of usernames in twitter data:
    :return first username, second username - strings of both users:
    """

    not_correct = True
    first_username = ''
    second_username = ''

    while not_correct:

        user_str = input("Input two user names from the list, comma separated: ")

        if ',' in user_str:

            try:
                user_str = user_str.split(',')
                first_username = user_str[0].strip()
                second_username = user_str[1].strip()
            except TypeError:
                print("Error in user names.  Please try again")

            if first_username not in user_name_list or second_username not in user_name_list:
                # your check to for correct user names goes here
                print("Error in user names.  Please try again")
            else:
                break
        else:
            print("Error in user names.  Please try again")


    return first_username, second_username

def main():
    """
    Open the file
    Read the data from the file
    Create username list from data
    Calculate the top three hashtags combined for all users
        Print them
    Calculate the top three hashtags individually for all users
        Print them
    Prompt for two user names from username list
    Calculate similarity for the two users
        Print them
    Prompt to plot or not and plot if 'yes'
    :return <none>:
    """

    #open file and read data
    fp = open_file()
    data_list = read_data(fp)

    #get lists based on twitter data
    user_name_list = get_user_names(data_list)
    top_three_combined = three_most_common_hashtags_combined(data_list, user_name_list)
    top_three_individual = three_most_common_hashtags_individuals(data_list, user_name_list)
    y_list = list() #list for plot function with counts of common tags

    #output statistics
    print()
    print("Top Three Hashtags Combined")
    print("{:>6s} {:<20s}".format("Count","Hashtag"))
    for item in top_three_combined:
        combined_count = item[0]
        combined_hashtag = item[1]
        print("{:>6d} {:<20s}".format(combined_count, combined_hashtag))
    print()
    
    print("Top Three Hashtags by Individual")
    print("{:>6s} {:<20s} {:<20s}".format("Count","Hashtag","User"))
    for item in top_three_individual:
        count = item[0]
        hashtag = item[1]
        user_name = item[2]
        print("{:>6d} {:<20s} {:<20s}".format(count, hashtag, user_name))
    print()

    #generate list of usernames to display
    usernames_str = ""
    for item in user_name_list:
        usernames_str += item+', '
    usernames_str = usernames_str.strip(string.punctuation)
        
    print("Usernames: ", usernames_str)
    first_username, second_username = get_first_second_usernames(user_name_list)

        
    # calculate similarity
    similarity_list = similarity(data_list, first_username, second_username)
    print()
    print("Similarities for "+first_username+" and "+second_username)
    print("{:12s}{:6s}".format("Month","Count"))
    for item in similarity_list:
        month_code = item[0]
        month = calendar.month_name[month_code]
        hashtag_set = len(item[1])
        y_list.append(hashtag_set)
        print("{:12s}{:<6d}".format(month, hashtag_set))
    print()
    
    # Prompt for a plot
    choice = input("Do you want to plot (yes/no)?: ")
    if choice.lower() == 'yes':
        pass
        x_list = [i for i in range(1,13)]
        plot_similarity(x_list, y_list, first_username, second_username)

if __name__ == '__main__':
    main()