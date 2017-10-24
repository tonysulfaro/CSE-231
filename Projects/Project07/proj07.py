import csv
import pylab

def open_file(message):
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

    ip_list = []

    #this one splits based on "," to seperate
    #start ip, end ip, and country code
    for line in file:

        line = line.strip()
        line = line.split(",")

        #print all items in line
        #start ip, end ip, country code
        #for x in range(len(line)):
         #   print(line[x])

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

        tup = (int(raw_start_ip), int(raw_end_ip), country_code)
        ip_list.append(tup)

    return ip_list


def read_ip_attack(file):

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

    for item in country_list:
        country_code = item[0]
        country_name = item[1]

        if country_code == code:
            return country_name

    return "Kosovo"



def bar_plot(count_list, countries):
    pylab.figure(figsize=(10,6))
    pylab.bar(list(range(len(count_list))), count_list, tick_label = countries)
    pylab.title("Countries with highest number of attacks")
    pylab.xlabel("Countries")
    pylab.ylabel("Number of attacks")
    
def main():

    #counts the number of times a country was attacked
    count_list = [0 for i in range(249)]
    country_list = []

    file = open_file("Enter the filename for the IP Address location list: ")
    ip_data = read_ip_location(file)
    
    file = open_file("Enter the filename for the IP Address attacks: ")
    attack_data = read_ip_attack(file)
    
    file = open_file("Enter the filename for the country codes: ")
    country_data = read_country_name(file)

    data_filtering_choice = input("\nDo you want to display all data? ")

    for item in attack_data:
        ip_int = item[0]
        ip_str = item[1]

        country_code = locate_address(ip_data, ip_int)
        country_name = get_country_name(country_data, country_code)

        print("{:15s} {:<15s} {:>18s} {:<s}".format("The IP Address:",
                                                      ip_str, "originated from", country_name))

        #finds the number of times a country was an attacker onto the count_list
        count = 0
        for country in country_data:

            code = country[0]

            if code == country_code:
                count_list[count] += 1
                count += 1
            else:
                count += 1

        #adds all countries to country_list
        for country in country_data:
            country_list.append(country[0])

    title = "\nTop 10 Attack Countries"
    header = "{:<8s} {:>5s}".format("Country", "Count")

    print(title)
    print(header)

    highest_attack_country = ""
    highest_attack_number = 0

    n = 1
    count = 249
    index = 0
    #while top number is less than 10
    while n <= 10:
        #for every entry in both lists
        for x in range(count):
            #if the current one is larger its the new largest
            if count_list[x] > highest_attack_number:
                highest_attack_number = count_list[x]
                highest_attack_country = country_list[x]
                #print(highest_attack_country,highest_attack_number)
                index = x

        print("{:<8s} {:>5d}".format(country_list[index], count_list[index]))
        count_list.pop(index)
        country_list.pop(index)
        highest_attack_country = ""
        highest_attack_number = 0
        index = 0
        count -= 1
        n += 1

    answer = input("\nDo you want to plot? ").upper()
    if answer == "YES":
        #bar_plot(count_list, country_list)
        pass
    else:
        pass



if __name__ == "__main__":
    main()