def find_state(state, ch):

    if state == 1:
        if ch == 'h':
            state = 1
            return state
        elif ch == 'a' or ch == 'o':
            state = 2
            return state
        else:
            state = 5
            return state

    if state == 2 or state == 3:
        if ch == 'a' or ch == 'o':
            state = 2
            return state
        elif ch == 'h':
            state = 3
            return state
        elif ch == '!':
            state = 4
            return state
        else:
            state = 5
            return state

    if state == 4:
        state = 4
        return state

    if state == 5:
        state = 5
        return state

state = 1
ch = input("Enter a Character: ")
ch = str(ch)
if ch == '':
    quit()
state = find_state(state, ch)
print(state)

while input != "":

    ch = input("Enter a Character: ")
    ch = str(ch)
    if ch == '':
        break
    state = find_state(state, ch)
    print(state)
