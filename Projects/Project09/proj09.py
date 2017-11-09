'''Skeleton file with all strings for Mimir testing'''

import string, calendar, pylab

MONTH_NAMES = [calendar.month_name[month] for month in range(1,13)]

def open_file():
    '''docstring'''
#    filename = input("Input a filename: ")
#        except FileNotFoundError:
#            print("Error in input filename. Please try again.")
    pass

def validate_hashtag(s):
    '''docstring'''
    pass

def get_hashtags(s):
    '''docstring'''
    pass

def read_data(fp):
    '''docstring'''
    pass

def get_histogram_tag_count_for_users(data,usernames):
    '''docstring'''
    pass

def get_tags_by_month_for_users(data,usernames):
    '''docstring'''
    pass

def get_user_names(L):
    '''docstring'''
    pass

def three_most_common_hashtags_combined(L,usernames):
    '''docstring'''
    pass

def three_most_common_hashtags_individuals(data_lst,usernames):
    '''docstring'''
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