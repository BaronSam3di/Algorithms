"""
----- TournamentWinner  : Easy -----
------ BRIEF ------
There is  an Algorithms tournament taking place in which teams of programmers compete against each other to 
solve algorithmic problems as fast as possible. Teams compete in a round robin, where each team faces off against allother teams.
Only two teams compete against each other at a time, and for each competition, one team is designated the  home team, while the other team is the away team.

In each competition there's always one winner ans one looser; there are no ties. A team receives 3 points if it wins and 0 points if it loses. 
The winner of the tournament is the team that receives the most amount of points.

Given an array of pairs of representing the teams that have competed against each other and an array contains the results of each compettition, write a function tht returns the winner of the tournament. 
The Input arrays are named `competitions` and `results`, respectively. The competitions array has elements in the form  of [ homeTeam, awayTeam], 
where each team is a string of at most 30 characters representing the name of the team.

The results array contains information about the winner of each corresponding competition in the competitions array. Specifically, results[i] denotes the winner of competitions[i], 
where 1 in the results array means that the home team in the corresponding competitions won and a 0 means that the away team won.


It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once. 
It's also guaranteed that the tournament will always have at least two teams. 

------ Hints ------


------ Complexity ------ 

"""
HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam:0}                                        # keep track of al scores of all teams

    for idx, competition in enumerate(competitions):                    # loop through the entire competitions array to get hte index and each competition
        result = results[idx]                                           # with the index we get the corresponding result
        homeTeam , awayTeam = competition                               # based in the competition , we get the two teams 

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam # from the results we can tell if it was the home team or the away team

        updateScores(winningTeam, 3 , scores)                           # update the scores 

        if scores[winningTeam] > scores[currentBestTeam]:               # has the winning team beaten the current best score?
            currentBestTeam = winningTeam                               # swap values

    return currentBestTeam                                               

def updateScores(team, points, scores):
    if team not in scores:                                              # if the team is not known to the scores
        score[team] = 0                                                 # initialise he team with a 0 

    scores[team] += points                                              # and then give that team 3 points