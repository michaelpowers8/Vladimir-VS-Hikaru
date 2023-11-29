# Vladimir-VS-Hikaru
This is a detailed analysis on the interesting posts regarding Hikaru Nakamura's recent success on chess.com, and his achieving of 3336 blitz rating. The data acquired was NOT from Hikaru's account. Rather, I took the time to create a simulation of results of varying ELO's of Hikaru versus other opponents. The results are incredibly fascinating.
# Deep Dive 
## Chess Simulation.py
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
### Quick Note
The wins, draws, and losses were calculated with the following formula:

$$ P(White Win) = {1 \over {1+10^{BLACK ELO-WHITE ELO\over 400}}} $$

$$ P(Draw) = {1 \over {({1+10^{WHITE ELO-BLACK ELO\over 400}})*({1+10^{BLACK ELO-WHITE ELO\over 400}})}} $$

$$ P(Black Win) = 1 - P(White Win) $$

The way these formulas were used in the simulation were as weighted odds of outcomes. Weights in simulations do NOT have to add up to exactly 1. Just wanted to put that out there in case of confusion. 

To add just a little bit more math, each simulated match is 25,000 games, and there were 80,000 simulated matches. This included that Hikaru could have any ELO (integer) from 3150 all the way up to 3350. The opponent can have any (integer) ELO from 2700 up to 3100. The controversy seemed to include little to no players rated above 3100, so I capped it there. Multiply the number of matches by the number of games in each match. (80,000)*(25,000) = 2,000,000,000 total games simulated.

## Chess Simulation Analysis.ipynb
- This is the file that is used to analyze the resulting spreadsheet from Chess Simulation.py
- Loading Dataset
  - This section of the project is just loading the dataset into the notebook and importing several Python libraries used in both data science and data analysis
- Extra Functions
  - This section contains various bits of code that will be used several times, and is saved as a single function for easy access later instead of excess copy and pasting
  - The function rmse gives the value called the Reduced Mean Squared Error which is short for Mean/Average Error in future predictions
  - The get_scores function will be used later on in machine learning prediction analysis and will return a list of various metrics used to measure the effectiveness of different machine learning models. These metrics include the following:
    - Mean Squared Error
    - Reduced Mean Squared Error
    - Mean Absolute Error
    - Median Absolute Error
    - R2 Score
  - The full_stats function is a way to display several stats about the numerical data in a more organized way
    - Statistics included in the function are the following:
      - Minimum
      - Lower Quartile
      - Median
      - Mean
      - Upper Quartile
      - Maximum
      - Inner Quartile Range
      - Large Outliers
      - Small Outliers
      - Standard Deviation
      - Variance
### Exploratory Data Analysis:
  - This section includes all the analytical and graphical analysis performed on the spreadsheet. Everything explained in this section will be regarding scenarios in the dataset, and may not apply to what really happened. Also, there will be no account for the psychological effects chess may have on either Hikaru, or his opponents. I understand that beating the same player 10 times in a row has a different feeling than beating 10 random players in a row. All information provided can be found in the spreadsheet called <b>Hikaru Simulation Analytical Stats.csv</b>
  - Analytical Analysis
     - When looking at Hikaru's score, his lowest score achieved out of 13,878. This accounts for 55.5% of the points meaning that even when Hikaru had his worst performance, he still has more wins than losses. At his lowest, scores, his winning streaks went as high as 10 wins in a row. That may be a long way from 40, or 45, or 55, but this shows that Hikaru is likely to go on winning streaks often.
     - Hikaru's median score was 21,158 out of 25,000 which accounts for 84.6% of the points. In that same median performance, his longest expected winning streak is 40 wins. The ELO difference between Hikaru and his opponent in these matches was 350. This means that if Hikaru were to play 25,000 chess games against a person rated 350 below him, there is a 50% chance that at some point during the match, he will go on a 40 game winning streak. The expected number of 40 game win streaks to occur during that 25,000 game match was only one. To briefly put this in real time Hikaru, let's say his median rating during his record breaking streaks was 3300. If Hikaru was playing players with a median ELO of 2950, he could play 25,000 games against them and expect one single 40 game win streak in that time.
     - That may be a deceiving image in some way though. Let's take a look at the mean values as opposed to the medians. Hikaru's mean score was 20,727 which accounts for 82.9% of the points. When a mean is smaller than the median, that means that the data may be skewed by smaller numbers. In this case, notice that any Hikaru score below 14,026 is considered an outlier. However, Hikaru's minimum score is only 13,878 which is smaller than the statistical outlier. This means that on one or more occasions, Hikaru had a shockingly bad performance that skews the data. However, this goes both ways. The median number of 40 game win streaks is 1, but the mean number of 40 game win streaks is 15.45. This means that when Hikaru is on the top of his game, he goes on several 40 game winning streaks. Also, his mean longest winning streak is 48 which means his winning streaks are skewed towards larger numbers. When Hikaru is playing poorly, his score is affected, but when he is performing well, his winning streaks become large and frequent.
     - Hikaru's longest winning streak in a 25,000 game match was 274. In those incredibly long runs, he could also expect to go on as many as 196 separate 40 game winning streaks. This is an incredible feat, however it comes with a major drawback that is not super realistic. The ELO difference between Hikaru and his opponent in these scenarios is 600+. It is overwhelmingly unlikely that Hikaru will be matched in a rated game with players 600 ELO lower than him. A better and more plausible number to investigate comes from the median to upper quartile region. Let's take a closer look at the upper quartile.
     - Hikaru's upper quartile score is 22,601 which accounts for 90.4% of points. In these games, the ELO difference between Hikaru and his opponent is 450. Given Hikaru's astronomical real life blitz rating, this is a little more feasible to see. If Hikaru is rated 3250, then he would be getting matched up with players that have an ELO of about 2800. Given that situation, if Hikaru were to play 25,000 games against 2800s, you could expect him to go on a 63 game winning streak at some point, and go on about 14 separate 40 game winning streaks. That is an average of one long winning streak per 1785 games.
