#To improve: create the inverse dictionary --> better param number validation
# Easier validation of valid action
action_dic = {
    0: ['print', 'sort', 'pop', 'reverse'],
    1: ['remove', 'append'],
    2: ['insert']
}

def execute_command(command, l):
    action, *values = command.split()

    #Check if command is valid
    if not any(action in actions for actions in action_dic.values()):
        return print(f'ERROR, unrecognized command: {command}')
        
    #Check if values number is valid
    if len(values) > (len(action_dic) - 1):
        return print('ERROR, too many values for any command')
    
    #Check according number of values for action
    if action not in action_dic[len(values)]:
        return print(f'ERROR, invalid number of values for {action}')
    
    match (action):
        case 'insert':
            l.insert(int(values[0]), int(values[1]))
        case 'print':
            print(l)
        case 'remove':
            l.remove(int(values[0]))
        case 'append':
            l.append(int(values[0]))
        case 'sort':
            l.sort()
        case 'pop':
            l.pop()
        case 'reverse':
            l.reverse()


if __name__ == '__main__':
    l = []
    N = int(input())
    line=''
    for i in range(N):
        execute_command(str(input()), l)    
    
