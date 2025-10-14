# Black Jack simulator
import random, sys, time


#first let's define robot_battle

def robot_battle():
    print('Now, it is my turn to battle you >:)  Let me get my numbers.')
    time.sleep(1)
    comp_num_one = random.randint(1,10)
    comp_num_two = random.randint(1,10)
    comp_num_three = 0
    comp_num_four = 0
    comp_num_five = 0

    def comp_total():
        return comp_num_one + comp_num_two + comp_num_three + comp_num_four + comp_num_five
    print(comp_num_one)
    print(comp_num_two)

    time.sleep(1)
    print('Hmm, should I hit, or miss?')
    time.sleep(2)
    while True:
        if comp_total() < 17:
            print('I\'ll hit.')
            comp_num_three = random.randint(1, 10)
            time.sleep(1)
            print('My number is ' + str(comp_num_three) + '.')
            time.sleep(1)
            print('My total is ' + str(comp_total()) + '.')
            if comp_total() < 17:
                time.sleep(1)
                print('Hmm, should I hit, or miss?')
                time.sleep(2)
                print('I\'ll hit.')
                time.sleep(1)
                comp_num_four = random.randint(1, 10)
                print('My number is ' + str(comp_num_four) + '.')
                time.sleep(1)
                print('My total is ' + str(comp_total()) + '.')
                if comp_total() < 17:
                    time.sleep(1)
                    print('Hmm, should I hit, or miss?')
                    time.sleep(1)
                    print('I\'ll hit.')
                    comp_num_five = random.randint(1, 10)
                    time.sleep(1)
                    print('My number is' + str(comp_num_five) + '.')
                    time.sleep(1)
                    print('My total is ' + str(comp_total()) + '.')
                    if comp_total() <= 21:
                        print('Ha, I automatically win since I hit my maximum draw limit of five!')
                        print('You have ten seconds before this program terminates.  Goodbye.')
                        time.sleep(10)
                        sys.exit()

                else:
                        break
            else:
                break
        else:
            break

    print('I\'ll pass on hitting for now.  Let\'s compare our final results.')
    time.sleep(1)
    print('My total was ' + str(comp_total()) + ' and your total was ' + str(total()) + '.')
    time.sleep(1)
    if comp_total() > total() and comp_total() < 22:
        print('I won!  Haha.  Take that against a computer.\n\n')
    elif comp_total() < total() and total() < 22:
        print('Aw man, you bested me this time.\n\n')
    elif comp_total() > 21 and total() > 21:
        print('Shoot.  We both lost.\n\n')
    elif comp_total() == total() and comp_total() < 22:
        print('Wow, a tie.  How delightful.\n\n')
    elif comp_total() > 21 and total() <= 21:
        print('Dang, you got me.\n\n')
    elif comp_total() <= 21 and total() > 21:
        print('Haha, a win for me!')
    time.sleep(1)
    print('You have ten seconds before this program terminates.  Goodbye.')
    time.sleep(10)


# Welcome stage
print('Welcome to Black Jack!')
time.sleep(0.5)
print('This version is played differently than others.  Would you like me to explain the rules to you?')
while True:
    rules_answer = input('>')
    if rules_answer == 'yes':
        print('You will be given two numbers between 1 and 10.  All numbers have the same likelihood of being generated.')
        time.sleep(1)
        print('So, unlike normal Black Jack, face cards (i.e. 10) do not have a higher chance to be drawn.')
        time.sleep(1)

        print('Additionally, aces are automatically counted as 1.  No 11 exists.  So you will never get 21 on your first two cards.')# This is where the rules will go.
        time.sleep(1)
        break
    elif rules_answer == 'no':
        break
    else:
        print('Please answer with either \'yes\' or \'no\'.')
        continue

# Start of the game
time.sleep(1)
print('\nLet\'s begin.  Here are your first two numbers.')
time.sleep(1)
number_one = random.randint(1, 10)
number_two = random.randint(1, 10)
number_three = 0
number_four = 0
number_five = 0

game_over = 'no'

def total():
    return number_one + number_two + number_three + number_four + number_five

print(number_one)

time.sleep(1)
print(number_two)
time.sleep(1)
print('Would you like to get hit?')

while True:
    first_answer = input('>')
    if first_answer == 'yes':
        number_three = random.randint(1, 10)
        print(number_three)
        print('Your total is ' + str(total()) + '.')
        break
    elif first_answer == 'no':
        print('Your total is ' + str(total()) + '.')
        robot_battle()
        sys.exit()
    else:
        print('Please answer with either \'yes\' or \'no\'.')
        continue

if int(total()) > 21:
    print('Tough luck!')
elif int(total()) == 21:
    print('Nice job!')
else:
    print('Would you like to get hit again?')

    while True:#Second hit
        second_answer = input('>')
        if second_answer == 'yes':
            number_four = random.randint(1, 10)
            print(number_four)
            print('Your total is ' + str(total()) + '.')
            break
        elif second_answer == 'no':
            print('Your total is ' + str(total()) + '.')
            robot_battle()
            sys.exit()
        else:
            print('Please answer with either \'yes\' or \'no\'.')
            continue

    if int(total()) > 21:
        print('Tough luck!')
    elif int(total()) == 21:
        print('Nice job!')
    else:
        print('Would you like to get hit again?')

        while True:
            third_answer = input('>')
            if third_answer == 'yes':
                number_five = random.randint(1, 10)
                print(number_five)
                print('Your total is ' + str(total()) + '.')
                break
            elif third_answer == 'no':
                print('Your total is ' + str(total()) + '.')
                robot_battle()
                sys.exit()
            else:
                print('Please answer with either \'yes\' or \'no\'.')
                continue

        if int(total()) > 21:
            print('Tough luck!')
        elif int(total()) == 21:
            print('Nice job!  You maxed out your draws (maximum 5) and now automatically win, since you\'re still under 21!')
            game_over = 'yes'

if game_over == 'yes':
    print('You never even gave me a chance to play you!')
    sys.exit()
else:
    robot_battle()
