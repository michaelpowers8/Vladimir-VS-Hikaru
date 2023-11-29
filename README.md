# Vladimir-VS-Hikaru
This is a detailed analysis on the interesting posts regarding Hikaru Nakamura's recent success on chess.com, and his achieving of 3336 blitz rating. The data acquired was NOT from Hikaru's account. Rather, I took the time to create a simulation of results of varying ELO's of Hikaru versus other opponents. The results are incredibly fascinating.
# How to Navigate the Project
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
 - Exploratory Data Analysis:
   - This section includes all the analytical and graphical analysis performed on the spreadsheet. Everything explained in this section will be regarding scenarios in the dataset, and may not apply to what really happened
   - Analytical Analysis
     - The first thing found is
