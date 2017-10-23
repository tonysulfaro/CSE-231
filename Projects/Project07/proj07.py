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

    for line in file:

        line = line.strip()
        line = line.split(".")

        for x in range(3):
            line[x] = line[x].zfill(3)

        print(line)

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
    

