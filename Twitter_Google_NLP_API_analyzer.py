import tweepy #https://github.com/tweepy/tweepy
import re
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from datetime import datetime, timedelta
from nltk.tokenize import WordPunctTokenizer

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_cred.json"

consumer_key = 'your consumer_key'
consumer_secret = 'your consumer_secret'
access_token = "your access_token"
access_token_secret = "your access_token_secret"

def authentication(cons_key, cons_secret, acc_token, acc_secret):
    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(acc_token, acc_secret)
    api = tweepy.API(auth)
    return api

# Search tweets from the last 24 hours with maximum tweets of 20
def search_tweets(keyword, total_tweets):
    today_datetime = datetime.today().now()
    yesterday_datetime = today_datetime - timedelta(days=1)
    #today_date = today_datetime.strftime('%Y-%m-%d')
    yesterday_date = yesterday_datetime.strftime('%Y-%m-%d')
    api = authentication(consumer_key,consumer_secret,access_token,access_token_secret)
    search_result = tweepy.Cursor(api.search,q=keyword,since=yesterday_date,result_type='recent',lang='en').items(total_tweets)
    return search_result

# Clean tweets before analyzing in Google NLP API
def clean_tweets(tweet):
    user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet.decode('utf-8'))
    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
    number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)
    lower_case_tweet= number_removed.lower()
    tok = WordPunctTokenizer()
    words = tok.tokenize(lower_case_tweet)
    clean_tweet = (' '.join(words)).strip()
    return clean_tweet

def get_sentiment_score(tweet):
    client = language.LanguageServiceClient()
    document = types.Document(content=tweet,type=enums.Document.Type.PLAIN_TEXT)
    sentiment_score = client.analyze_sentiment(document=document).document_sentiment.score
    return sentiment_score

def analyze_tweets(keyword, total_tweets):
    score = 0
    tweets = search_tweets(keyword,total_tweets)
    for tweet in tweets:
        cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))
        sentiment_score = get_sentiment_score(cleaned_tweet)
        score += sentiment_score
        print('Tweet: {}'.format(cleaned_tweet))
        print('Score: {}\n'.format(sentiment_score))
    final_score = round((score / float(total_tweets)),2)
    return final_score

def main():
    keyword = input("Enter a keyword: ")
    final_score = analyze_tweets(keyword, 20)
    if final_score <= -0.25:
        status = 'NEGATIVE'
    elif final_score <= 0.25:
        status = 'NEUTRAL'
    else:
        status = 'POSITIVE'
    print('Average score for '+str(keyword)+' is '+str(final_score)+' -> '+status)

if __name__ == '__main__':
    main()