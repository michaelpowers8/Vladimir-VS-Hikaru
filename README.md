# Vladimir-VS-Hikaru
This is a detailed analysis on the interesting posts regarding Hikaru Nakamura's recent success on chess.com, and his achieving of 3336 blitz rating. The data acquired was NOT from Hikaru's account. Rather, I took the time to create a simulation of results of varying ELO's of Hikaru versus other opponents. The results are incredibly fascinating.
# How to Navigate the Project
- Chess Simulation.py is the file that created the simulation of Hikaru playing many games at different ELOs with opponents of different ELOs
  - Every simulation is Hikaru playing 25,000 games against at a specific ELO versus an opponent at their own specific ELO
    - Example:
    - The initial simulation is Hikaru has an ELO of 3150, and his opponent has an ELO of 2700. The two of them have a 25,000 game match, and the results are recorded
  - The scores recorded in every simulated match of 25,000 games include the following:
    - Hikaru's ELO
    - Anonymous GM's ELO
    - Hikaru's Score
    - Anonymous GM's Score
    - Hikaru's Longest Winning Streak
    - The number of separate winning streaks Hikaru had that were 40 or more wins
## Quick Note
The wins, draws, and losses were calculated with the following formula:
- $$ P(White Win) = {1 \over (1+10^((BLACK ELO-WHITE ELO)\over 400))} $$
  -  All of these scores were then uploaded to a spreadsheet that I called Hikaru Big Simulation.csv
    - 
