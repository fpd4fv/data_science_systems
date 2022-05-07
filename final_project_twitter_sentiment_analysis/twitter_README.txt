About this folder with the repo:
- this folder contains files related to my project for the final exam where I ingest tweets and conduct sentiment analysis on them.
- this folder includes the program which performs these operations (textblob_tweepy_sent_analysis.py)
- this folder also includes two .csv files that are examples of the program working


About textblob_tweepy_sent_analysis.py

This program (textblob_tweepy_sent_analysis.py) uses the twitter API to gather tweets from a particular user, and then it conducts sentiment analysis on the tweets using TextBlob and returns the tweets and their sentiment analysis scores in a dataframe.

This program was inspired by a project I worked on last semester with a scholar from a foreign affairs think tank as he was trying to scrape tweets for understanding the opinions of politicians.
There are two functions in this program
1. user_tweets() gathers tweets (excluding retweets) in a user's timeline and returns them in a dataframe with sentiment analysis scores attached (polarity and subjectivity scores.)


2. user_tweets_about_US() is more targeted towards my application of submitting to my former manager at the thinktank as this function specifically examines tweets that mention the United States. I have set this function to examine the tweets from China's state media Frontline twitter account


When the program is run, I have programmed it to produce a dataframe of sentiment analysis of Dave Portnoy, the CEO of Barstool Sports, and then I included a line that will allow the user to input an account that they want to see sentiment analysis conducted on. For demonstrating the general sentiment analysis function, I picked Dave Portnoy, the CEO of Barstool Sports as he is one of the most opinionated people I could think of. 

The program will also use the user_tweets_about_US() function to conduct sentiment analysis on tweets from China's state media Frontline twitter account

Within each function, I have provided a line of code that will save the df to a csv file on the user's local device if they edit the line and provide a specific filepath. Sometimes, it is easier to view the dataframes on excel.
