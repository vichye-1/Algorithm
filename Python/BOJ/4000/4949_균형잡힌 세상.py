while True:
    bracket = []
    sentence = input()

    if sentence == ".":
        break

    for i in sentence:
        if i == "(" or i == "[":
            bracket.append(i)
        elif i == ")":
            if bracket and bracket[-1] == "(":
                bracket.pop()
            else:
                bracket.append(")")
        elif i == "]":
            if bracket and bracket[-1] == "[":
                bracket.pop()
            else:
                bracket.append("]")
    if bracket:
        print("no")
    else:
        print("yes")
