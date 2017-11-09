import pylab as py
from operator import itemgetter


def open_file():
    """
    prompts for input with the given prompt passed as message
    catches if file isnt there and prompts again
    exits when it can open the file
    :param message - prompt as string:
    :return fp - file pointer:
    """
    while True:
        file_name = input("Input a file name: ")
        try:
            fp = open(file_name)
            break
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
            continue
    return fp


def update_dictionary(dictionary, year, hurricane_name, data):
    """
    checks if year from file isnt in dictionary
        adds it if it is not
    checks if there is data for each hurricane
        adds the data if there is not
    append data to data list inside hurricane dictionary inside year dictionary
    :param dictionary - dictionary passed by the create_dictionary function:
    :param year - year as an integer from create_dictionary:
    :param hurricane_name - string of hurricane name from create_dictionary:
    :param data - tuple of weather data from create_dictionary:
    :return dictionary - dictionary updated with new information:
    """

    #finally this logic works
    if year not in dictionary:
        dictionary[year] = {}
    if hurricane_name not in dictionary[year]:
        dictionary[year][hurricane_name] = list()

    dictionary[year][hurricane_name].append(data)

    return dictionary


def create_dictionary(fp):
    """
    initialize empty dictionary
    for each line in the filepointer
        strip and split the line on a space
        remove empty strings from the line
        truncate line to data that is needed
        slice out data from the line
        replace empty data with 0 for wind and pressure
        create tuple with sliced data
        update the dictionary with update_dictionary function and new information as parameters
    :param fp - filepointer from file provided by user:
    :return data dictionary - fully populated dictionary from filepointer:
    """

    data_dictionary = dict()

    for line in fp:

        line = line.strip().split(" ")

        # remove null values from line list
        line = [x for x in line if x]  # https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
        # truncate line up to everything before pressure
        line = line[:8]

        year = line[0]
        hurricane_name = line[1]
        lat = float(line[3])
        lon = float(line[4])
        date = line[5]
        try:
            wind = float(line[6])
        except ValueError:
            wind = 0

        try:
            pressure = float(line[7])
        except ValueError:
            pressure = 0

        tup = (lat, lon, date, wind, pressure)

        data_dictionary = update_dictionary(data_dictionary, year, hurricane_name, tup)

    return data_dictionary


def display_table(unsorted_dictionary, selected_year):
    """
    filter dictionary entries by selected year
    create list of items from sorted dictionary
    for storm name and data in the dictionary list
        initialize variables
        sort data list
        for item in data list
            slice out wind speed
            find max wind speed
                set coordinates, speed, and dates equal to their constants at top
        print values of data
    :param unsorted_dictionary - dictionary that is not sorted passed through by main:
    :param selected_year - selected year by the user to display:
    :return <none>:
    """


    #sort the dictionary alphabetically by storm name
    dictionary = unsorted_dictionary[selected_year]
    dictionary = sorted(dictionary.items(), key=itemgetter(0))

    print("{:^70s}".format("Peak Wind Speed for the Hurricanes in " + selected_year))
    print("{:15s}{:>15s}{:>20s}{:>15s}".format("Name", "Coordinates", "Wind Speed (knots)", "Date"))

    #iterate over dictionary data list
    for storm_name, data in dictionary:

        max_speed = 0
        lat = 0
        lon = 0
        date = ''

        data = sorted(data)

        #iterate over data list of tuples
        for item in data:

            wind_speed = item[3]

            if wind_speed >= max_speed:
                max_speed = wind_speed
                lat = item[0]
                lon = item[1]
                date = str(item[2])

        print("{:15s}({:6.2f},{:6.2f}){:>20.2f}{:>15s}".format(storm_name, lat, lon, max_speed, date))


def get_years(dictionary):
    """
    initialize year list
    for year, and weather dictionary in dictionary
        add year to year list
    sort year list
    slice out min and max years
    :param dictionary - unsorted dictionary from filepointer in main:
    :return min and max years as tuple:
    """
    year_list = list()

    for year, data in dictionary.items():
        year_list.append(year)

    sorted(year_list)

    min_year = year_list[0]
    max_year = year_list[-1]

    return min_year, max_year


def prepare_plot(unsorted_dictionary, year):
    """
    initialize lists
    sort and filter the dictionary read from the file in main
    for key storm name and value list of tuples
        find max wind speed and add do max_speed list
        find unique hurricane names and add to name list
        find all coordinates and add to coordinate lists
    :param unsorted_dictionary - dictionary that is unsorted from main:
    :param year - integer that specifies the year user would like to see:
    :return names, coordinates, max_speed - lists of storm data attributes:
    """

    #initialize lists
    names = list()
    max_speed = list()
    coordinates = list()

    #sort dictionary by storm name
    dictionary = unsorted_dictionary[year]
    dictionary = sorted(dictionary.items(), key=itemgetter(0))

    #iterates through the dictionary
    for storm_name, data in dictionary:

        max_wind_speed = 0
        data = sorted(data)
        latlon = list()

        for item in data:

            wind_speed = item[3]

            #find max wind speed
            if wind_speed >= max_wind_speed:
                max_wind_speed = wind_speed

            lat = item[0]
            lon = item[1]
            cord_pair = (lat, lon)
            latlon.append(cord_pair)

        #append values to lists
        names.append(storm_name)
        max_speed.append(max_wind_speed)
        coordinates.append(latlon)

    return names, coordinates, max_speed


def plot_map(year, size, names, coordinates):
    """

    :param year:
    :param size:
    :param names:
    :param coordinates:
    :return:
    """

    # The the RGB list of the background image
    img = py.imread("world-map.jpg")

    # Set the max values for the latitude and longitude of the map
    max_longitude, max_latitude = 180, 90

    # Set the background image on the plot
    py.imshow(img, extent=[-max_longitude, max_longitude,
                           -max_latitude, max_latitude])

    # Set the corners of the map to cover the Atlantic Region
    xshift = (50, 190)
    yshift = (90, 30)

    # Show the atlantic ocean region
    py.xlim((-max_longitude + xshift[0], max_longitude - xshift[1]))
    py.ylim((-max_latitude + yshift[0], max_latitude - yshift[1]))

    # Generate the colormap and select the colors for each hurricane
    cmap = py.get_cmap('gnuplot')
    colors = [cmap(i / size) for i in range(size)]

    # plot each hurricane's trajectory
    for i, key in enumerate(names):
        lat = [lat for lat, lon in coordinates[i]]
        lon = [lon for lat, lon in coordinates[i]]
        py.plot(lon, lat, color=colors[i], label=key)


        # Set the legend at the bottom of the plot
    py.legend(bbox_to_anchor=(0., -0.5, 1., 0.102), loc=0, ncol=3, mode='expand',
              borderaxespad=0., fontsize=10)

    # Set the labels and titles of the plot
    py.xlabel("Longitude (degrees)")
    py.ylabel("Latitude (degrees)")
    py.title("Hurricane Trayectories for {}".format(year))
    py.show()  # show the full map


def plot_wind_chart(year, size, names, max_speed):
    '''Remember to put a docstring here'''

    # Set the value of the category
    cat_limit = [[v for i in range(size)] for v in [64, 83, 96, 113, 137]]

    # Colors for the category plots
    COLORS = ["g", "b", "y", "m", "r"]

    # Plot the Wind Speed of Hurricane
    for i in range(5):
        py.plot(range(size), cat_limit[i], COLORS[i], label="category-{:d}".format(i + 1))

    # Set the legend for the categories
    py.legend(bbox_to_anchor=(1.05, 1.), loc=2,
              borderaxespad=0., fontsize=10)

    py.xticks(range(size), names, rotation='vertical')  # Set the x-axis to be the names
    py.ylim(0, 180)  # Set the limit of the wind speed

    # Set the axis labels and title
    py.ylabel("Wind Speed (knots)")
    py.xlabel("Hurricane Name")
    py.title("Max Hurricane Wind Speed for {}".format(year))
    py.plot(range(size), max_speed)  # plot the wind speed plot
    py.show()  # Show the plot


def select_year(min_year, max_year):
    """

    :param min_year:
    :param max_year:
    :return:
    """

    selected_year = input("Enter the year to show hurricane data or 'quit': ")

    while selected_year != 'quit':

        try:
            int(selected_year)
            if selected_year >= min_year and selected_year <= max_year:
                break

            # if year not within dict range
            if selected_year < min_year or selected_year > max_year:
                print("Error with the year key! Try another year")

        except (TypeError, ValueError):
            if selected_year.lower() == 'quit':
                quit()
            else:
                print('Error with the year key! Try another year')

        selected_year = input("Enter the year to show hurricane data or 'quit': ")

    return selected_year


#main method
def main():
    """

    :return <none>:
    """

    #open file for writing and initialize dictionary
    fp = open_file()
    data_dictionary = create_dictionary(fp)

    #extract date range from dictionary
    date_range = get_years(data_dictionary)
    min_year = date_range[0]
    max_year = date_range[1]

    print("Hurricane Record Software")
    print("Records from {:4s} to {:4s}".format(min_year, max_year))

    #fetch selected year
    selected_year = select_year(min_year, max_year)

    #mainloop
    while selected_year != 'quit':

        #print out hurricane data in table
        display_table(data_dictionary, selected_year)

        #plotting hurricane data
        plot_choice = input("\nDo you want to plot? ").lower()
        names, coordinates, max_speed = prepare_plot(data_dictionary, selected_year)

        size = len(names)

        #plots if user says so
        if plot_choice == 'yes':
            plot_map(selected_year, size, names, coordinates)
            plot_wind_chart(selected_year, size, names, max_speed)

        selected_year = select_year(min_year, max_year)


if __name__ == "__main__":
    main()