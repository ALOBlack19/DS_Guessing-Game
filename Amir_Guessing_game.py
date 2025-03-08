import random

print("Welcome to the guessing game!")
print("Get ready!")
#______________________________________________________________________________
win_num = random.randint(1,1000)
#______________________________________________________________________________

var_range1 = 1
var_range2 = 1000
max_plays = 10
plays = [] # receiving the guesses from the user
 # counting the list of guesses
input_play = 0
#______________________________________________________________________________
# Loop to change the range for each user guess

while input_play != win_num:        # avoiding users errors
    input_play = int(input(f"Guess a number between {var_range1} and {var_range2}: "))  # user only can write integer
    plays.append(input_play)        # loop to save and print user guesses
    play_count = len(plays)
    print(f"That was your {play_count}st guess, try again!")
    print(f"You have` only {max_plays - play_count} remaining")
    if input_play > 1000:
        max_plays -= 1
        print("try again!")
        continue
    elif input_play > win_num:
        var_range2 = input_play - 1
    elif input_play < win_num:
        var_range1 = input_play + 1
    elif input_play < 1:              # User can not inset number below 1 and above 1000
        print("try again!")
        max_plays -= 1
        continue
    if max_plays == 0 or play_count == 10:
        print("No more tries, !!!!Game Over!!!!")
        break
    elif input_play == win_num:
        print("You win!")
        break


#______________________________________________________________________________

