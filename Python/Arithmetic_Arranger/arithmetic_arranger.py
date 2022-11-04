def arithmetic_arranger(problems, bool):
    toppart = ""
    bottompart = ""
    middlepart = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    for math in problems:
        y = math.split(" ")
        length = round(len(math) / 2)
        topsize = len(y[0])
        bottomsize = len(y[2])
        if topsize > 4 or bottomsize > 4:
            return "Error: Numbers cannot be more than four digits."
        elif y[1] != '+' and y[1] != '-':
            return "Error: Operator must be '+' or '-'."
        elif topsize < bottomsize:
            toppart = toppart + (length-topsize)*" " + y[0] + 5 * " "
            bottompart = bottompart + y[1] + " " + y[2] + 4 * " "
            middlepart = middlepart + (bottomsize + 2) * "-" + 4 * " "
        elif topsize > bottomsize:
            toppart = toppart + " " + y[0] + 5 * " "
            bottompart = bottompart + y[1] + (length-bottomsize - 1)*" " + y[2] + 4 * " "
            middlepart = middlepart + (topsize + 1) * "-" + 4 * " "
        elif topsize == bottomsize:
            toppart = toppart + " " + y[0] + 5 * " "
            bottompart = bottompart + y[1] + " " + y[2] + 4*" "
            middlepart = middlepart + (bottomsize + 2) * "-" + 4 * " "
    print(toppart)
    print(bottompart)
    print(middlepart)
print(arithmetic_arranger(["102 + 8" , "28 + 531", "13 + 12","1 + 3","3 - 19"], 0))