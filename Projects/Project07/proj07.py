###############################################################################
#   import pylab library for plotting
#   open file function
#       takes message as parameter to prompt user for a filename
#       opens the file if it can and returns the file pointer
#   read ip location function
#       takes the file pointer and reads in all the country ranges into a list
#           ranges are range of integers and a country code
#       returns country range list
#   read ip attack function
#       reads attack information and converts them to integers
#       with zfill and adding on 000 to serve as the 4th ip range
#       return ip list with ip as string and as an int
#   read country name function
#       open the country name file pointer and read all contents
#       return list of tuples of country code and country name
#   locate address function
#       take the ip list and an attack ip and see which range the ip falls in
#       if it falls in the range return the country code that its between
#       else check the next country
#   get country name function
#       takes a country code and country list
#       checks each value until the code given and code in list match up
#       if they do return the country name
#   bar plot function
#       takes a list of countries and counts and plots them with pylab lib
#   main method
#       initialize empty country and count lists
#       prompt for ip address location list and store fp
#       prompt for ip attack lists and store as fp
#       prompt for country code lists and store as fp
#       prompt if user wants to display all attack data
#           if yes then print attack data as it is generated
#           if no generate the data but dont print it
#       for item in the attack data fp
#           get the country code with locate address function
#           get country name after getting country code
#           print the attack information if user entered yes to disp data
#           sort the country data
#
#           for country in country data
#               add the country code to the country list
#               if it appears in the attack increment the index in count_list
#       print title and header for top 10 attackers
#       initialize indexes
#       for x in range 10 (goes down the list to pick top 10 attackers)
#           for x in range count of items in count and country lists
#               if the count at index x is higher than highest attack then its the new highest
#               highest attack country of x is now the highest attack country as well
#           print highest attacker and their count
#           add the entries to the top 10 lists
#           pop the entries out of the list
#           reset highest attack numbers and country
#       prompt if the user wants to plot the data
#       if yes then pass the data to the bar plot function
#   Call main
###############################################################################

import pylab

def open_file(message):
    """
    prompts for input with the given prompt passed as message
    catches if file isnt there and prompts again
    exits when it can open the file
    :param message - prompt as string:
    :return fp - file pointer:
    """
    while True:
        file_name = input(message)
        try:
            fp = open(file_name)
            break
        except FileNotFoundError:
            print("File is not found! Try Again!")
            continue
    return fp


def read_ip_location(file):
    """
    for each line in the file pointer
        strip it and split on a comma
        split items 0,1 on "." because they are an ip
        zfill the ip and then make them ints
        add the new ip integers and country code to tuple and append to list
    :param file - file pointer of country ranges and codes:
    :return ip_list - list of tuples with ip range and country code:
    """

    ip_list = []

    #this one splits based on "," to seperate
    #start ip, end ip, and country code
    for line in file:

        line = line.strip()
        line = line.split(",")

        #extract start ip, end ip, and country code from line
        #split ip on "."
        start_ip = line[0].split(".")
        end_ip = line[1].split(".")
        country_code = line[2]

        #raw ip to be entered into the tuple
        raw_start_ip = ''
        raw_end_ip = ''

        #for each item in the ip pad it with zeros
        #add it to the raw ip string
        for x in range(len(start_ip)):
            start_ip[x] = start_ip[x].zfill(3)
            raw_start_ip += start_ip[x]

        for x in range(len(end_ip)):
            end_ip[x] = end_ip[x].zfill(3)
            raw_end_ip += end_ip[x]

        #start and end ip addresses and country code
        tup = (int(raw_start_ip), int(raw_end_ip), country_code)
        ip_list.append(tup)

    return ip_list


def read_ip_attack(file):
    """
    initialize empty ip list
    for each line in the file pointer of attacks
    strip the line and add xxx onto it
    split on the "." for an ip and fill each set with zeros
    add tuple of ip string and numbers to a list
    :param file - file pointer of attacks:
    :return ip_list - list of ip attack tuples:
    """

    ip_list = []

    for line in file:

        ip_int = ''
        ip_str = ''

        #strip elements and set the line plus xxx equal to ip_str
        line = line.strip()
        line += ".xxx"
        ip_str = line
        line = line.split(".")

        #if theres an xxx in the line replace it with 000 and add it to ip_int
        for x in range(4):
            line[x] = line[x].zfill(3)
            if line[x] == "xxx":
                line[x] = line[x].replace("xxx","000")
                ip_int += line[x]

            else:
                ip_int += line[x]

        tup = (int(ip_int), ip_str)
        ip_list.append(tup)

    return ip_list


def read_country_name(file):
    """
    initialize empty country list
    for each line in the file pointer
        strip and split on ";"
        first item is the full country name
        second is the code
        add both items to a tuple
        append the tuple to the list
    :param file - file pointer of country name file:
    :return country_list - list of country codes and their full name as a tuple:
    """

    country_list = []

    for line in file:

        #basically get the country list and make a list out of it
        line = line.strip().split(";")
        full_name = line[0]
        country_code = line[1]

        tup = (country_code, full_name)
        country_list.append(tup)

    return country_list

    
def locate_address(ip_list, ip_attack):
    """
    for each line in the file pointer
        define the ip ranges and country codes
        if the attacking ip is in between the range then return country code
    :param ip_list - list of ip address ranges and country code:
    :param ip_attack - attacking ip as an integer:
    :return country_code - country code as a string:
    """

    for line in ip_list:

        start_ip = line[0]
        end_ip = line[1]
        country_code = line[2]

        if ip_attack >= start_ip and ip_attack <= end_ip:
            return country_code
        else:
            pass


#gets country name from list that has just code and name
def get_country_name(country_list, code):
    """
    for item in the country list
        if the code in the list matches the code provided then return the name
    :param country_list - list of country names and their codes:
    :param code - country code as string:
    :return country_name - full country name:
    """

    for item in country_list:
        country_code = item[0]
        country_name = item[1]

        if country_code == code:
            return country_name

    return "Kosovo"


def bar_plot(count_list, countries):
    """
    define display attributes
    display plot
    :param count_list - list of attack counts:
    :param countries - list of countries:
    :return <none> :
    """
    pylab.figure(figsize=(10,6))
    pylab.bar(list(range(len(count_list))), count_list, tick_label = countries)
    pylab.title("Countries with highest number of attacks")
    pylab.xlabel("Countries")
    pylab.ylabel("Number of attacks")
    pylab.show()

def main():
    """
    initialize empty country and count lists
       prompt for ip address location list and store fp
       prompt for ip attack lists and store as fp
       prompt for country code lists and store as fp
       prompt if user wants to display all attack data
           if yes then print attack data as it is generated
           if no generate the data but dont print it
       for item in the attack data fp
           get the country code with locate address function
           get country name after getting country code
           print the attack information if user entered yes to disp data
           sort the country data

           for country in country data
               add the country code to the country list
               if it appears in the attack increment the index in count_list
       print title and header for top 10 attackers
       initialize indexes
       for x in range 10 (goes down the list to pick top 10 attackers)
           for x in range count of items in count and country lists
               if the count at index x is higher than highest attack then its the new highest
               highest attack country of x is now the highest attack country as well
           print highest attacker and their count
           add the entries to the top 10 lists
           pop the entries out of the list
           reset highest attack numbers and country
       prompt if the user wants to plot the data
       if yes then pass the data to the bar plot function
    :return <none> :
    """

    #counts the number of times a country was attacked
    count_list = [0 for i in range(249)]
    country_list = []
    top_ten_attack_numbers = []
    top_ten_attack_country = []

    file = open_file("Enter the filename for the IP Address location list: ")
    ip_data = read_ip_location(file)
    
    file = open_file("Enter the filename for the IP Address attacks: ")
    attack_data = read_ip_attack(file)
    
    file = open_file("Enter the filename for the country codes: ")
    country_data = read_country_name(file)

    data_filtering_choice = input("\nDo you want to display all data? ").lower()

    for item in attack_data:
        ip_int = item[0]
        ip_str = item[1]

        country_code = locate_address(ip_data, ip_int)
        country_name = get_country_name(country_data, country_code)

        if data_filtering_choice == 'yes':

         print("{:15s} {:<15s} {:>18s} {:<s}".format("The IP Address:",
                                                      ip_str, "originated from", country_name))

        #finds the number of times a country was an attacker onto the count_list
        count = 0
        country_data = sorted(country_data)
        for country in country_data:

            country_list.append(country[0])
            code = country[0]

            if code == country_code:
                count_list[count] += 1
                count += 1
            else:
                count += 1


    title = "\nTop 10 Attack Countries"
    header = "{:<8s} {:>5s}".format("Country", "Count")

    print(title)
    print(header)

    highest_attack_country = ""
    highest_attack_number = 0

    count = 249
    index = 0
    #while top number is less than 10
    for x in range(10):
        #for every entry in both lists
        for x in range(count):
            #if the current one is larger its the new largest
            if count_list[x] >= highest_attack_number:
                highest_attack_number = count_list[x]
                highest_attack_country = country_list[x]
                #print(highest_attack_country,highest_attack_number)
                index = x

        print("{:<8s} {:>5d}".format(country_list[index], count_list[index]))
        top_ten_attack_country.append(country_list[index])
        top_ten_attack_numbers.append(count_list[index])
        count_list.pop(index)
        country_list.pop(index)
        highest_attack_country = ""
        highest_attack_number = 0
        index = 0
        count -= 1


    answer = input("\nDo you want to plot? ").upper()
    if answer == "YES":
        bar_plot(top_ten_attack_numbers, top_ten_attack_country)
        pass
    else:
        pass


if __name__ == "__main__":
    main()