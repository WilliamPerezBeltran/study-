import re
def WildcardCharacters(strParam):
    # code goes here
    breakpoint = strParam.find(' ')
    wildCard = strParam[:breakpoint]
    result = strParam[breakpoint + 1:]
    index = 0
    step = 0
    
    while index < len(wildCard):
        if wildCard[index] == '+':
            step += 1
        elif wildCard[index] == '*':
            sequenceLenght = 3
            if index + 1 < len(wildCard):
                if wildCard[index + 1] == '{':
                    num = ''
                    while wildCard[index] != '}':
                        if wildCard[index] >= '0' and wildCard[index] <= '9':
                            num += wildCard[index]
                        index += 1
                    sequenceLenght = int(num)
            if step + sequenceLenght-1 > len(result):
                return "false"
            else:
                tempChar = result[step]
                while sequenceLenght > 0:
                    if result[step] != tempChar:
                        return "false"
                    step += 1
                    sequenceLenght -= 1
        elif wildCard[index] != result[step]:
            return "false"
        else:
            step += 1
        index += 1
    if step != len(result):
        return "false"
    return "true"

# keep this function call here 
print WildcardCharacters(raw_input())