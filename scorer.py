def score(string):
    try:
        score = (abs(24 - int(eval(string) + 0.01))) * (-1)            #Epsilon 1/100
    except (ZeroDivisionError, SyntaxError):
        score = -10

    lastPar = False

    for char in string:
        if char == '+':
            score += 5
        elif char == '-':
            score += 4
        elif char == '*':
            score += 3
        elif char == '/':
            score += 2
        elif char == '(':
            lastPar = True
        elif char == ')' and lastPar:
            score -= 1
            lastPar = False
    
    return score
        
