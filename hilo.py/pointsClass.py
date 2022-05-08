#create Points class
from tracemalloc import stop


class Points:
    def __init__(score):
        score.points = 300

#function to add 100 points for correct guess and subtract 75 for an incorrect guess
    def adjust_score(score, guess, answer):
        score.points = 300
        if guess == 'h' and answer == 'h':
            score.points += 100
        elif guess == 'l' and answer == 'l':
            score.points += 100
        elif score == 'h' and answer != 'h':
            score.points -= 75
        elif guess == 'l' and answer != 'l':
            score.points -= 75
    
#function to end game if score = 0
    def lose_game(score):
        if score.points == 0:
           print('Better luck next time!')
        else:
            pass

        
