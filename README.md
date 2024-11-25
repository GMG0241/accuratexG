# accuratexG
This repository aims to provide a better way to understand how to interpret the xG statistic commonly seen on TV. My reasoning for this repository is as follows:

Suppose 2 teams are playing against each other, team A and team B. Team A had 2 shots with an xG of 0 and 1. Team B also had 2 shots, but with an xG of 0.5 and 0.5.
If we were to sum the xG for both teams, we would see that both teams had an xG of 1. However, if we asked what was the probability for both teams to score exactly 1, we see that Team A has a 100% chance of scoring 1, but team B only has 50% chance of scoring 1 (team B has a 50% chance of scoring exactly 1). If we also asked what is the probability of both teams scoring exactly 2 goals, we see that Team A has a 0% chance of scoring 2 goals, and team B has a 25% chance to score 2 goals. We can also notice therfore that Team B has a 25% chance to not score any goals. These facts are impossible to see by simply summing the xG and hence why I made this repository

# How to use the tool
Simply run 'probabilityCalc.py' using a python interpreter. You can either manually enter your values or use a file.

If you plan on using a file, please see the exampleFileinput.txt file, or the SOULIV2425.txt file for how to accurately format your file. SOULIV2425.txt is the actual xG as according to Opta for the Southampton vs Liverpool game during the 24/25 season.

If you plan on manually entering the data, the prompts should be fairly self explantiory, but you should input how many entries you plan to make with team 0, and then input the xG values for each shot. If you've entered too many just enter 0 to skip. Do the same for team 1.

# Caveats
1. Currently, part of the probability calculation is inefficient as it takes a lot of memory. I was planning to make this a matrix calculation, but I found it difficult so went with the inefficient method for now. Maybe I'll come back to this and turn it into a matrix calculation, but I expect that for most games this will be fine. The SOU-LIV game has 27 shots from Liverpool and the algorithm takes about 30s to run on my Computer. 27 tends to be near the high side of shots in a game, so we'll see.

2. xG doesn't take into account own goals or potential for own goals. If you want to change the model behind generating probabilities (e.g. xGoT, or something completely different) that is fine, as the maths will work so long as they are genuine probabilities i.e. between 0 and 1 (the model can even be garbage! For example, 1 for on target shots and 0 for off target, and the maths will still work, just don't expect any useful results!). 

# Further
To see where to collect data of your own, I would recommend the Opta website: https://theanalyst.com/competition/premier-league/fixtures where you can select a fixture, and see stats, including an xG map. 

Feel free to use this tool for non-commercial use