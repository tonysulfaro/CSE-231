
import pylab

STATES = {'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY'}
USERS = ["Public", "Domestic", "Industrial", "Irrigation","Livestock"]

def open_file():
    '''Remember to put a docstring here'''
    while True:
        file_name = input("Enter a file name: ")
        try:

            fp = open(file_name)
            break
        except FileNotFoundError:
            print("Error Invalid Input")
            continue

    return fp

    
def read_file(fp):
    '''Remember to put a docstring here'''

    data_list = []
    fp.readline()

    for line in fp:

        line = line.strip('\n').strip()
        line = line.split(',')
        #print(line)

        state = line[0]
        county = line[2]
        population = int(float(line[6])*1000)
        fresh_water_usage = line[114]
        salt_water_usage = line[115]
        water_usage_public = line[18]
        water_usage_domestic = line[26]
        water_usage_industrial = line[35]
        water_usage_irrigation = line[45]
        water_usage_livestock = line[59]

        line_tuple = (state,county,population, fresh_water_usage,salt_water_usage,water_usage_public,
                      water_usage_domestic,water_usage_industrial,water_usage_irrigation,water_usage_livestock)
        data_list.append(line_tuple)

    for item in data_list:
        print(item)

    return data_list

def compute_usage(state_list):
    '''Remember to put a docstring here'''

    usage_list = []

    for line in state_list:
        county = line[2]
        population = int(line[6]) * 1000
        total_water = line[114] + line[115] +line[18] +line[26] +line[35]+line[45]+line[59]
        per_person_water = total_water/population
        tup = (county, population, total_water, per_person_water)
        usage_list.append(tup)

    return usage_list
        
    
def extract_data(data_list, state):
    '''Remember to put a docstring here'''
    state_list = []

    for line in data_list:
        if data_list[0] == state:
            state_list.append(line)

    return state_list

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
    print("Water Usage Data from the US and its States and Territories.\n")
    state = input("\nEnter state code or 'all' or 'quit': ")
#    answer = input("\nDo you want to plot? ")
#    print("Error in state code.  Please try again.")
    fp = open_file()
    data_list = read_file(fp)
    state_list = extract_data(data_list,state)
    usage_list = compute_usage(state_list)


if __name__ == "__main__":
    main()
