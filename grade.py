print("\n\t\t***************************************\n")
print("\t\t\tWelcome to my grade system\n")

print("""
    \t\tScore\t\tGrade\n
    \t\t>= 0.9\t\tA\n
    \t\t>= 0.8\t\tB\n
    \t\t>= 0.7\t\tC\n
    \t\t>= 0.6\t\tD\n
    \t\t<0.6\t\tF\n
    ***Enter q or Q to Quit
    
""")
cont = True
while cont:
    score = input('Enter Score: ')
    if score is 'q' or score is 'Q':
        print('Quitting ....')
        break
    else:
        try:
            score = float(score)
        except:
            print('Bad Code')
            print('Enter numeric number between 0 and 1\n')
            continue
        if score <= 1.0 and score > 0.9:
            print('A')
        elif score < 0.9 and score >= 0.8:
            print('B')
        elif score < 0.8 and score >= 0.7:
            print('C')
        elif score < 0.7 and score >= 0.6:
            print('D')
        elif score < 0.6 and score >= 0:
            print('F')
        else:
            print('Bad Score')
            print('Enter number between 0 and 1\n')
