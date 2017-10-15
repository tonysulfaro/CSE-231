#mutute_list function goes here
def mutate_list(user_list, index_num, v):
    user_list = user_list.insert(user_list,index_num,v)
    return user_list


#remove_index function goes here
def remove_index(user_list, index_num):
    print(len(user_list))
    user_list = user_list.remove(user_list[index_num])
    print(len(user_list))
    return user_list

#reverse_list function goes here
def reverse_list(user_list):
    user_list = user_list.reverse()
    return user_list



def main():
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    print(user_list)
    print("Menu: ")
    print("mutate list(m), remove (r), reverse_list (R)")
    user_choice = input("Enter choice (m,r,R): ")
    if user_choice == 'm':
        index_num, v = input().split(",")
        index_num = int(index_num)
        v = int(v)
        user_list= mutate_list(user_list, index_num, v)
        print(user_list)
    elif user_choice == 'r':
        index_num = int(input())
        user_list = remove_index(user_list, index_num)
        print(user_list)
    elif user_choice == 'R':
        new_list = reverse_list(user_list)
        print(new_list)
main()