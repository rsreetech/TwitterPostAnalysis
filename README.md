# TwitterPostAnalysis
Sample code for twitter posts extraction, sentiment analysis and wordcloud creation

Pre-requisites
1) https://github.com/cjhutto/vaderSentiment#installation (VADER sentinment analyzer)
2)https://github.com/nltk/nltk (NLTK)
3)https://github.com/taspinar/twitterscraper (twitterscraper)
4)https://pandas.pydata.org/(Pandas)
5)https://matplotlib.org/ (Matplotlib)
6)https://pypi.org/project/wordcloud/( wordcloud)

I have chosen the topic to be searched as Xiaomi Mi10 smartphone searched using the query:'#Mi10'
Then i filter for tweets from India
I then compute the sentiment for these tweets
Based on sentiment i classify the tweets as either positive or negative category
I then create wordcloud for these categories

In this way twitter posts can be analysed to find out what contributes to negative and positive sentiments around a product.

Caveats:
1) VADER sentiment analyzer has inaccuracies. Custom trained sentiment analyzer should give better results
2) Better to register as a twitter developer to access twitter posts


