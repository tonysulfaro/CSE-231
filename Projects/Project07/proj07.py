import csv
import pylab

def open_file(message):
    while True:
        file_name = input("Input a file name: ")
        try:
            fp = open(file_name)
            break
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
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
        for x in range(len(line)):
            print(line[x])

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



    pass

def get_country_name(country_list, code):
    pass

def bar_plot(count_list, countries):
    pylab.figure(figsize=(10,6))
    pylab.bar(list(range(len(count_list))), count_list, tick_label = countries)
    pylab.title("Countries with highest number of attacks")
    pylab.xlabel("Countries")
    pylab.ylabel("Number of attacks")
    
def main():
    #file = open_file("Enter the filename for the IP Address location list: ")
    #ip_data = read_ip_location(file)
    
    file = open_file("Enter the filename for the IP Address attacks: ")
    attack_data = read_ip_attack(file)
    
    file = open_file("Enter the filename for the country codes: ")
    country_data = read_country_name(file)

    #answer = input("\nDo you want to plot? ")
    
if __name__ == "__main__":
    main()