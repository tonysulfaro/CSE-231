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

        for x in range(len(line)):
            print(line[x])

        start_ip = line[0]
        end_ip = line[1]
        country_code = line[2]

        for item in start_ip:

            item.split(".")

            for x in range(4):
                item[x] = item[x].zfill(3)

            item

        tup = (start_ip, end_ip, country_code)




    for item in ip_list:
        print(item)

def read_ip_attack(file):
    pass

def read_country_name(file):
    pass
    
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
    file = open_file("Enter the filename for the IP Address location list: ")
    ip_data = read_ip_location(file)
    
    file = open_file("Enter the filename for the IP Address attacks: ")
    attack_data = read_ip_attack(file)
    
    file = open_file("Enter the filename for the country codes: ")
    country_data = read_country_name(file)

    #answer = input("\nDo you want to plot? ")
    
if __name__ == "__main__":
    main()
    

