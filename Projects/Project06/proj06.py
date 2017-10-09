
import pylab

STATES = {'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY'}
USERS = ["Public", "Domestic", "Industrial", "Irrigation","Livestock"]

def open_file():
    '''Remember to put a docstring here'''
    pass
    
def read_file(fp):
    '''Remember to put a docstring here'''
    pass

def compute_usage(state_list):
    '''Remember to put a docstring here'''
    pass
        
    
def extract_data(data_list, state):
    '''Remember to put a docstring here'''
    pass

def display_data(state_list, state):
    '''Remember to put a docstring here'''
# Some strings useful for Mimir testing
#    title = "Water Usage in " + state + " for 2010"
#    header = "{:22s} {:>22s} {:>22s} {:>22s}".format("County", \
#    "Population", "Total (Mgal/day)", "Per Person (Mgal/person)")

    

def plot_water_usage(some_list, plt_title):
    '''
        Creates a list "y" containing the water usage in Mgal/d of all counties.
        Y should have a length of 5. The list "y" is used to create a pie chart
        displaying the water distribution of the five groups.

        This function is provided by the project.
    '''

    # accumulate public, domestic, industrial, irrigation, and livestock data
    y =[ 0,0,0,0,0 ]

    for item in some_list:

        y[0] += item[5]
        y[1] += item[6]
        y[2] += item[7]
        y[3] += item[8]
        y[4] += item[9]

    total = sum(y)
    y = [round(x/total * 100,2) for x in y] # computes the percentages.

    color_list = ['b','g','r','c','m']
    pylab.title(plt_title)
    pylab.pie(y,labels=USERS,colors=color_list)
    pylab.show()
    #pylab.savefig("plot.png")  # uncomment to save plot to a file
    
def main():

# Some strings to help with Mimir testing
#    print("Water Usage Data from the US and its States and Territories.\n")
#    state = input("\nEnter state code or 'all' or 'quit': ")
#    answer = input("\nDo you want to plot? ")
#    print("Error in state code.  Please try again.")
    pass

if __name__ == "__main__":
    main()
