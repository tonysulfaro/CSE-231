# TODO make source header
import pylab

STATES = {'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY',
          'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH',
          'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY'}
USERS = ["Public", "Domestic", "Industrial", "Irrigation", "Livestock"]


def open_file():
    '''Remember to put a docstring here'''
    while True:
        # file_name = input("Enter a file name: ")
        try:

            # fp = open(file_name)
            break
        except FileNotFoundError:
            # print("Error Invalid Input")
            continue
    fp = open("Water_Data_2010.csv") #TODO make this user input again instead of hardcoded
    return fp


def read_file(fp):
    '''Remember to put a docstring here'''

    data_list = []
    fp.readline()

    # linecount = 0 TODO take out linecounters

    for line in fp:

        line = line.strip('\n').strip()
        line = line.split(',')

        for x in range(115):
            try:
                if line[x] == '':
                    # print(x)
                    line[x] = 0
                if line[x] == ' ':
                    line[x] = 0
            except TypeError:
                pass

        # have to catch if there is null value and replace with o
        state = line[0]
        county = line[2]
        population = (float(line[6]))
        fresh_water_usage = float(line[114])
        salt_water_usage = float(line[115])
        water_usage_public = float(line[18])
        water_usage_domestic = float(line[26])
        water_usage_industrial = float(line[35])
        water_usage_irrigation = float(line[45])
        water_usage_livestock = float(line[59])

        line_tuple = (state, county, population, fresh_water_usage, salt_water_usage, water_usage_public,
                      water_usage_domestic, water_usage_industrial, water_usage_irrigation, water_usage_livestock)
        data_list.append(line_tuple)

    return data_list


def compute_usage(state_list):
    '''Remember to put a docstring here'''

    usage_list = []

    state = 0
    current_county = ""

    population_total = 0
    total_water = 0

    for line in state_list:

        # print(population_total)
        # print(total_water)
        # print("State",state)

        # print(line) TODO take out for debugging
        county = line[1]
        population = int((float(line[2]) * 1000))
        water = line[3] + line[4] + line[5] + line[6] + line[7] + line[8] + line[9]
        # per_person_water = total_water/population

        # this is pretty much verbaitim from project 5
        # handles the first line with new county
        if county != current_county and state != 0:
            # print('case1') TODO remove these case prints
            state = 3

        # for the first line
        if state == 0:
            # print('case2')
            population_total += population
            total_water += water
            state = 1
            current_county = county

        # for all lines after the first one
        if state == 1 and current_county == county:
            # print('case3')
            population_total += population
            total_water += water
            state = 1
            current_county = county

        # when product change add cumulative stats into new tuple
        else:
            # print('case4')
            # print(county,population_total,total_water)
            tup = (county, population_total, total_water, total_water/population_total)
            usage_list.append(tup)
            population_total = 0
            total_water = 0
            state = 1
            current_county = county

            population_total += population
            total_water += water

    return usage_list


def extract_data(data_list, state):
    '''Remember to put a docstring here'''
    state_list = []

    for line in data_list:

        if state == 'ALL':
            state_list.append(line)
        elif line[0] == state:
            state_list.append(line)

    return state_list


def display_data(state_list, state):
    '''Remember to put a docstring here'''
    # Some strings useful for Mimir testing
    usage_list = compute_usage(state_list)

    title = "{:^88s}".format( "Water Usage in " + state + " for 2010")
    header = "{:22s} {:>22s} {:>22s} {:>22s}".format("County",
                                                     "Population", "Total (Mgal/day)", "Per Person (Mgal/person)")

    print(title)
    print(header)

    for line in usage_list:
        print("{:22s} {:>22d} {:>22.2f} {:>22f}".format(line[0], line[1], line[2], line[3]))


def plot_water_usage(some_list, plt_title):
    '''
        Creates a list "y" containing the water usage in Mgal/d of all counties.
        Y should have a length of 5. The list "y" is used to create a pie chart
        displaying the water distribution of the five groups.

        This function is provided by the project.
    '''

    # accumulate public, domestic, industrial, irrigation, and livestock data
    y = [0, 0, 0, 0, 0]

    for item in some_list:
        y[0] += item[5]
        y[1] += item[6]
        y[2] += item[7]
        y[3] += item[8]
        y[4] += item[9]

    total = sum(y)
    y = [round(x / total * 100, 2) for x in y]  # computes the percentages.

    color_list = ['b', 'g', 'r', 'c', 'm']
    pylab.title(plt_title)
    pylab.pie(y, labels=USERS, colors=color_list)
    pylab.show()
    # pylab.savefig("plot.png")  # uncomment to save plot to a file


def main():
    # Some strings to help with Mimir testing
    print("Water Usage Data from the US and its States and Territories.\n")

    state = ""

    while True:

        state = input("\nEnter state code or 'all' or 'quit': ").upper()

        if state in STATES or state == 'ALL' or state == 'QUIT':
            if state == 'QUIT':
                quit()
            break
        else:
            print("Error in state code.  Please try again.")


    #    answer = input("\nDo you want to plot? ")

    fp = open_file()
    data_list = read_file(fp)
    state_list = extract_data(data_list, state)
    usage_list = compute_usage(state_list)
    display_data(state_list, state)


if __name__ == "__main__":
    main()
