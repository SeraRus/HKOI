import re
n = int(input())
for i in range(n):
    command = input()
    command = command[1:]
    pos = command.find("\"")
    string = command[:pos]
    command = command[pos+2:]
    action = command.split(" ")[0]
    commandString = command[len(action)+1:]

    if action == "Cut":
        commandString = re.match('"(.*)"', commandString).group(1)
        string = string.replace(commandString, "", 1)
    elif action == "Append":
        commandString = re.match('"(.*)"', commandString).group(1)
        string += commandString
    elif action == "Insert":
        commandString = re.match('(\\d+) "(.*)"', commandString)
        num = int(commandString.group(1))
        string = string[:num-1] + commandString.group(2) + string[num-1:]
    elif action == "Replace":
        commandString = re.match('"(.*?)" "(.*?)"', commandString)
        string = string.replace(commandString.group(1), commandString.group(2), 1)

    print(f'Command #{i + 1}: "{string}"')
