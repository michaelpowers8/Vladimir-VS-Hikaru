import random
from os import system
from time import sleep
import pandas as pd

#writer = turtle.Turtle(visible=False)
#writer.speed(0)
#writer.penup()
#writer.goto(-400,-80)
outcomes = []
final_outcome = []

def simulate_chess_game(player1_elo, player2_elo,game_number):
    global outcomes
    # Calculate winning probabilities based on Elo ratings
    p1_win_prob = 1 / (1 + 10**((player2_elo - player1_elo) / 400))
    draw_prob = 1 / ((1+10**((player2_elo-player1_elo)/400))*(1+10**((player1_elo-player2_elo)/400)))
    p2_win_prob = 1 / (1 + 10**((player1_elo - player2_elo) / 400))

    # Simulate a chess game
    outcome = random.choices(['p1_win', 'p2_win', 'draw'], weights=[p1_win_prob, p2_win_prob, draw_prob])[0]
    del p1_win_prob,p2_win_prob,draw_prob
    if(
        (outcome == 'p1_win')and
        (player1_elo>=3150)
      ):
        outcomes.append('WIN')
    elif(
        (outcome == 'p2_win')and
        (player2_elo>=3150)
    ):
        outcomes.append('WIN')
    elif(
        (outcome == 'draw')
    ):
        outcomes.append('DRAW')
    else:
        outcomes.append('LOSS')
    # Assign points based on the outcome
    if outcome == 'p1_win':
        return 1, 0
    elif outcome == 'p2_win':
        return 0, 1
    else:
        return 0.5, 0.5

def simulate_chess_tournament(num_games,player1_elo,player2_elo):
    global outcomes
    player1_score = 0
    player2_score = 0
    biggest_streak = 0
    forty_plus_streaks = 0
    streak = 0
    outcomes = []

    for x in range(num_games):
        # Determine who goes first in each game
        if random.choice([True, False]):
            p1_score, p2_score = simulate_chess_game(player1_elo, player2_elo,x+1)
        else:
            p2_score, p1_score = simulate_chess_game(player2_elo, player1_elo,x+1)

        # Update scores
        player1_score += p1_score
        player2_score += p2_score
    for result in outcomes:
        if(result == 'WIN'):
            streak += 1
            if(streak > biggest_streak):
                biggest_streak = streak
            if(streak==40):
                forty_plus_streaks += 1
        else:
            streak = 0

    return [player1_elo,player2_elo,player1_score, player2_score, biggest_streak, forty_plus_streaks]

# Set Elo ratings and number of games
num_tournaments = 0
tournament_data = pd.DataFrame(data=None,columns=['Hikaru ELO','Anonymous GM ELO','Hikaru Biggest Win Streak','Number of 40 Win Streaks'])

# Simulate the chess tournament
for hikaru_elo in range(3150,3350):
    for anonymous_gm_elo in range(2700,3100):
        num_tournaments += 1
        tournament = simulate_chess_tournament(25000,hikaru_elo,anonymous_gm_elo)
        system('cls')
        print(f"Number of Tournaments:\t\t{num_tournaments}\nHikaru ELO:\t\t\t{hikaru_elo} ⟶  {tournament[0]}\nAnonymous GM ELO:\t\t{anonymous_gm_elo} ⟶  {tournament[1]}\nHikaru Biggest Win Streak:\t{tournament[2]}\nHikaru 40 Win Streaks:\t\t{tournament[3]}")
        final_outcome.append(tournament)
        if(num_tournaments%1000==0):
            tournament_data = pd.DataFrame(data=final_outcome,columns=['Hikaru ELO','Anonymous GM ELO',"Hikaru Score",'Anonymous GM Score','Hikaru Biggest Win Streak','Number of 40 Win Streaks'])
            tournament_data.to_csv('Hikaru Big Simulation.csv',index=False)
