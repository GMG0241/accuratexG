# accuratexG
This repository aims to provide a better way to understand how to interpret the xG statistic commonly seen on TV. My reasoning for this repository is as follows:

Suppose 2 teams are playing against each other, Team A and Team B. Team A had 2 shots with an xG of 0 and 1. Team B also had 2 shots, but with an xG of 0.5 and 0.5.
If we were to sum the xG for both teams, we would see that both teams had an xG of 1. However, if we asked what was the probability for both teams to score exactly 1, we see that Team A has a 100% chance of scoring 1, but Team B only has 50% chance of scoring 1 (Team B has a 50% chance of scoring EXACTLY 1). If we also asked what is the probability of both teams scoring exactly 2 goals, we see that Team A has a 0% chance of scoring 2 goals, and Team B has a 25% chance to score 2 goals. We can also notice, therefore, that Team B has a 25% chance to not score any goals. These facts are impossible to see by simply summing the xG and hence why I made this repository

# How to use the tool
Simply run 'probabilityCalc.py' using a python interpreter. You can either manually enter your values or use a file.

If you plan on using a file, please see the exampleFileinput.txt file, or the SOULIV2425.txt file for how to accurately format your file. SOULIV2425.txt is the actual xG as according to Opta for the Southampton vs Liverpool Premier League game during the 24/25 season.

If you plan on manually entering the data, the prompts should be fairly self explanitory, but you should input how many entries you plan to make with team 0, and then input the xG values for each shot. If you've entered too many just enter 0 to skip. Do the same for team 1.

# scrapeOptaXGData.js

scrapeOptaXGData.js provides an easy way to collect the xG data from Opta's website (see 'Other'). You need to navigate to a fixture and click on xG map and then follow the instructions below. The javascript file provided should create an output which enables you to collect all of the data in the expected file format. It can be a bit finicky, but after navigating to the xG map: 
1. Inspect the page (Right click and inspect, or Ctrl+Shift+I)
2. VERY IMPORTANT - Ctrl+Shift+C and click on any of the xG 'Bubbles' you can see 
3. Click on 'Console' - it is a tab within the inspect pane which you've opened (this can be either at the top of the page, bottom of the page, or both)
4. Paste the contents of the .js file into the console (you may need to type 'allow pasting' before it allows you to do this)
5. Copy and paste the output into a file on your computer.
6. Save the file and use it in the program


# How does the maths work?

TODO :)

# Other

xG doesn't take into account own goals or potential for own goals. If you want to change the model behind generating probabilities (e.g. xGoT, or something completely different) that is fine, as the maths will work so long as they are genuine probabilities i.e. between 0 and 1 (the model can even be garbage! For example, 1 for on target shots and 0 for off target, and the maths will still work, just don't expect any useful results!). 

To see where to collect data of your own, I would recommend the Opta website: https://theanalyst.com/competition/premier-league/fixtures where you can select a fixture, and see stats, including an xG map. 

Feel free to use this tool for non-commercial use