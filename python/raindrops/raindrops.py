def convert(number):

    answer = ""

    if number % 3 == 0:
        answer += "Pling"

    if number % 5 == 0:
        answer += "Plang"

    if number % 7 == 0:
        answer += "Plong"

    if len(answer) == 0:
        answer = str(number)

    return answer

