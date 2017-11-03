#definition for music_func goes here
def music_func(music, group, singer):
    print("The best kind of music is", music)
    print("The best music group is", group)
    print("The best lead vocalist is", singer)

def main():
    music, group, singer = '', '', ''
    while music != 'quit':
        try:
            music, group, singer = input().split(',')
            music_func(music, group, singer)
        except (EOFError, ValueError):
            music, group, singer = 'Classic Rock', 'The Beatles', 'Freddie Mercury'
            music_func(music, group, singer)
            quit()

main()