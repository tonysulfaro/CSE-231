# new_list_function definition goes here
def new_list_function(initial_list):
    return initial_list*3

def main():
  #loop to ask users for values goes here
    list =[]
    new_list = []
    while input != 'exit':
        input_str = input('Enter value to be added to list: ')
        list = list.append(input_str)
    new_list = new_list_function(list)
  for element in new_list:

  #print values in new list

main()