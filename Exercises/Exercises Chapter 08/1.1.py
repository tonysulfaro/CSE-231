#definition for music_func goes here
def music_func(music, group, singer):
    print("The best kind of music is", music)
    print("The best music group is", group)
    print("The best lead vocalist is", singer)

def main():

    music, group, singer = input().split(',')
    music_func(music, group, singer)

    while music != '' or  group != '' or singer != '':
        try:

            music, group, singer = input().split(',')
            music_func(music, group, singer)
        except ValueError:
            break
main()