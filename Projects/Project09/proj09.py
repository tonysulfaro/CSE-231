'''Skeleton file with all strings for Mimir testing'''

import string, calendar, pylab

MONTH_NAMES = [calendar.month_name[month] for month in range(1,13)]

def open_file():
    """
        prompts for input with the given prompt passed as message
        catches if file isnt there and prompts again
        exits when it can open the file
        :param message - prompt as string:
        :return fp - file pointer:
        """
    while True:
        file_name = "smalldata.csv"#input("Input a file name: ")
        try:
            fp = open(file_name)
            break
        except FileNotFoundError:
            print("Error in input filename. Please try again.")
            continue
    return fp

def validate_hashtag(s):

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

    hashtag_list = list()

    s = s.split(" ")

    for item in s:
        if validate_hashtag(item):
            hashtag_list.append(item)

    return hashtag_list

def read_data(fp):
    '''docstring'''

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

    data_dictionary = dict()

    print(data)

    for lists in data:

        username = lists[0]
        month = lists[1]
        hashtags = lists[2]

        for tag in hashtags:
            if tag not in data_dictionary:
                data_dictionary[tag] = 0
            data_dictionary[tag] += 1

    return data_dictionary

def get_tags_by_month_for_users(data ,usernames):

    data_list = [(i, set()) for i in range(1,13)]

    for lists in data:

        username = lists[0]
        month = lists[1]-1
        hashtags = lists[2]

        for tag in hashtags:
            data_list[month][1].add(tag)

    return data_list

def get_user_names(L):

    user_names = list()

    for item in L:

        user_name = item[0]

        if user_name not in user_names:
            user_names.append(user_name)

    user_names = sorted(user_names)

    return user_names

def three_most_common_hashtags_combined(L,usernames):

    data_dictionary = get_histogram_tag_count_for_users(L, usernames)
    data_list = sorted([(v, k) for k, v in data_dictionary.items()], reverse= True)[:3]

    return data_list

def three_most_common_hashtags_individuals(data_lst,usernames):

    pass


def similarity(data_lst,user1,user2):
    '''docstring'''
    pass
        
def plot_similarity(x_list,y_list,name1,name2):
    '''Plot y vs. x with name1 and name2 in the title.'''
    
    pylab.plot(x_list,y_list)
    pylab.xticks(x_list,MONTH_NAMES,rotation=45,ha='right')
    pylab.ylabel('Hashtag Similarity')
    pylab.title('Twitter Similarity Between '+name1+' and '+name2)
    pylab.tight_layout()
    pylab.show()
    # the next line is simply to illustrate how to save the plot
    # leave it commented out in the version you submit
    #pylab.savefig("plot.png")


def main():
    # Open the file
    # Read the data from the file
    # Create username list from data
    # Calculate the top three hashtags combined for all users
    # Print them
    # Calculate the top three hashtags individually for all users
    # Print them
    # Prompt for two user names from username list
    # Calculate similarity for the two users
    # Print them
    # Prompt to plot or not and plot if 'yes'

    fp = open_file()
    data_list = read_data(fp)
    user_name_list = get_user_names(data_list)
    get_histogram_tag_count_for_users(data_list, user_name_list)
    get_tags_by_month_for_users(data_list, user_name_list)
    three_most_common_hashtags_combined(data_list, user_name_list)
    three_most_common_hashtags_individuals(data_list, user_name_list)

    quit()

   
    print("Top Three Hashtags Combined")
    print("{:>6s} {:<20s}".format("Count","Hashtag"))
    # your printing loop goes here
    print()
    
    print("Top Three Hashtags by Individual")
    print("{:>6s} {:<20s} {:<20s}".format("Count","Hashtag","User"))
    # your printing loop goes here
    print()
        
    #print("Usernames: ", usernames_str)
    #while True:  # prompt for and validate user names
        #user_str = input("Input two user names from the list, comma separated: ")
        # your check to for correct user names goes here
        #    print("Error in user names.  Please try again")
        
    # calculate similarity here
    print()
    #print("Similarities for "+users[0]+" and "+users[1])
    print("{:12s}{:6s}".format("Month","Count"))
    # your printing loop goes here
    print()
    
    # Prompt for a plot
    choice = input("Do you want to plot (yes/no)?: ")
    if choice.lower() == 'yes':
        pass
        # create x_list and y_list
        #plot_similarity(x_list,y_list,users[0],users[1])

if __name__ == '__main__':
    main()