# Skillcraft1 Dataset Analysis

## Starcraft II: Wings of Liberty

It is a multiplayer, strategy video game. It was released in 2010.
Online players are distributed into 7 leagues according to their level.

## The Dataset

### Composition:
- 20 attributes
- 3 395 instances

### Collection of Data:
- Telemetry from 3 340 players of 7 leagues contacted through social media and online gaming communities
- Replays of 35 professional players found on gaming websites

## Problem: League Prediction
### Why?
- By analyzing games, we will be able to assess gamers' level and allocate them to a concording league so that the enjoyment maximum: no boredom nor frustration
- Better train game's AI so that players can feel the same challenge even offline

## Results
Our study of the SkillCraft1 dataset led to the implementation of a logistic regression classifier. We tuned its parameters thanks to grid searching and got an accuracy of 49 % when a simple decision tree only had a 42 % accuracy.
Also, by using principal components analysis and ANOVA testing, we were able to identify the most influential features when it comes to predicting a league. These results are useful to modify the game's AI to better simulate a human player. They also provide information to gamers to evaluate their level, identify their strength and weaknesses so that they can improve.

