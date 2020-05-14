# -*- coding: utf-8 -*-
#created by rsreetech
from twitterscraper import query_tweets
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import datetime as dt
import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from wordcloud import WordCloud
import matplotlib.pyplot as plt


#Use twitterscraper to scrape tweets on a topic within a specific date range
list_of_tweets = query_tweets("#mi10",None, begindate=dt.date(2020, 5, 7),enddate=dt.date.today(), poolsize=9, lang='')

tweetDf = pd.DataFrame()





#Extract only id,timestamp and text fields and created a pandas dataframe
for tweet in list_of_tweets:
    identity = tweet.tweet_id
    date = tweet.timestamp
    text = tweet.text
    data =[{ 'id': identity ,'date': date,'text':text }]
    tweetDf = tweetDf.append( data,ignore_index=True)
    
#search tweets mentioning India
regex= '.*[i/I]ndia.*'

tweetsIndiaDf = tweetDf[tweetDf['text'].str.contains(regex)]


    
print(tweetsIndiaDf.head(10))

#method to clean the tweet text
def clean_Text(text ): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|\
                           (\w+:\/\/\S+)", " ", text).split()) 

stop_words = set(stopwords.words('english')) 
stop_words.add('xiaomi')
stop_words.add('mi')
stop_words.add('10')
stop_words.add('launch')
stop_words.add('india')
stop_words.add('phone')
stop_words.add('mi10')
stop_words.add('twitter')
stop_words.add('https')
stop_words.add('com')
stop_words.add('status')
stop_words.add('smartphone')

#method to remove stopwords from clean text
def remove_Stopwords(text ):
    words = word_tokenize( text.lower() ) 
    sentence = [w for w in words if not w in stop_words]
    return " ".join(sentence)
    
# method to assign sentiment class based on compound score from VADER
def sent_Class(x ):
    if x['compound'] >= 0.05:
        return 'positive'
    elif  (x['compound'] > -0.05) and (x['compound'] < 0.05):
        return 'neutral'
    elif x['compound'] <= -0.05  :
        return 'negative'
 
#Intialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

#method to compute sentiment score for tweet
def sentiment(x ):
    
    return analyzer.polarity_scores(x)

# clean text, remove stopwords, do sentiment analysis
tweetsIndiaDf['text'] = tweetsIndiaDf['text'].apply(clean_Text)
tweetsIndiaDf['text'] = tweetsIndiaDf['text'].apply(remove_Stopwords)
tweetsIndiaDf['sentiment'] = tweetsIndiaDf['text'].apply(sentiment)
tweetsIndiaDf['sentimentCat'] = tweetsIndiaDf['sentiment'].apply(sent_Class)



#Group tweets by sentiment

tweetsCategories = tweetsIndiaDf.groupby('sentimentCat')

positiveTweets = pd.DataFrame()
negativeTweets = pd.DataFrame()

for catName,tweetCategory in tweetsCategories:
    if catName == 'positive':
        positiveTweets = tweetCategory
    elif catName == 'negative':
        negativeTweets = tweetCategory
        
#Create word cloud for both positive and negative tweets
        
positiveText = ' '.join(positiveTweets['text'].tolist())

wordcloud = WordCloud(background_color="white",width=1600, height=800).generate(positiveText)
# Open a plot of the generated image.

plt.figure( figsize=(20,10), facecolor='k')
plt.imshow(wordcloud)
plt.axis("off")
#save the image
plt.savefig('Positivewordcloud.png', facecolor='k', bbox_inches='tight')


negativeText = ' '.join(negativeTweets['text'].tolist())

wordcloud = WordCloud(background_color="white",width=1600, height=800).generate(negativeText)
# Open a plot of the generated image.

plt.figure( figsize=(20,10), facecolor='k')
plt.imshow(wordcloud)
plt.axis("off")
#save the image
plt.savefig('Negativewordcloud.png', facecolor='k', bbox_inches='tight')




