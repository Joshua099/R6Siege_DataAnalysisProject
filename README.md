# R6Siege_DataAnalysisProject

**Special thanks to R6Tab for their unofficial Rainbow Six Siege API**

**https://github.com/Tabwire/R6Tab-API**

This is a passion project related to a video game I enjoy playing called Rainbow Six Siege. Rainbow Six Siege has a competitive ranked  5v5 mode that gives players a matchmaking rating (MMR) based on variables such as games won/lost. Many of the game's players feel that the game's current rating system is flawed. R6Tab is a 3rd party stat tracker website created by hardcore fans of the game. They created a new rating system based on R6's MMR system, but also included other variables into the calculation, such as a kills to deaths ratio. In a video game where victory is possible simply by killing your opponents, K:D ratio is crucial in determining how skilled an individual is.

"The new r6tab ranking system gives you a rank based on your skill level rather than a rank purely based on winning games."

However, many fans of R6Tab have complained that the website's new skill rating is too heavily influenced by just Kill:Death ratio, and is easily exploited by players whose playstyles are based on getting absurd amounts of kills. Rainbow Six Siege is a very complicated team-based game. There are more variables that lead to victory than just how many kills an individual gets. Many top-tier players find themselves in the top of the leaderboards by being good at the game in other ways. Some examples include being a good captain and calling out important information, or being a good support by setting up a good defense for their teammates.

I decided to get some insight into just how much K:D ratio affects R6Tab's new skill rating and do some analysis. I wanted to achieve this using popular data analysis tools:

1) **Python** - for data scraping, screening, and analysis scripts
2) **SQL** - for data table storage (mySQL server) and easy query aggregates of important statistical data

Thanks to this project, I am a lot more experienced in both these languages. 

**"WHAT AM I LOOKING AT HERE?"**

- The entire project process from start to finish is documented in the Jupyter Notebook named " ". Start here.

- The Practice Files Folder are there just for those curious to see all my attempts to get things to work. It's a mess and is intended to stay that way.

- r6-leaderboard-functions.py are the python functions I coded to interact with R6TAB's API.

- Anything not labeled as practice are scripts that are basically compiled into the Jupyter Notebook. 

- **SOON:** Dashboard application that streamlines the data real time. Analysis and all. (WIP)


**LIMITATIONS:**
This analysis has a very small sample size. R6TAB's API had a leaderboard call parameters that made it easy to pull information on up to 300 players. I decided to code with this in mind. With that said, there is certainly low statistical power and bias present. The variables R6TAB's API provides is also a bit of limitation. I formed by analysis based on the variables given to me. I talk a bit more about limitations in the report.

**DISCLAIMER:**
The PUBLIC version of this REPO will not have any of the commits I worked on. The reason being that since this was my first time working on a full project in GitHub, i accidently uploaded some login credentials that are present in some of the scripts into the PRIVATE version of this REPO thinking I could permanently delete them through commits. I was wrong... (:


*Leaderboard Stat data current as of 5/14/2019*


