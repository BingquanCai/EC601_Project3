import Twitter_Google_NLP_API_analyzer as tga
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_cred.json"


# Test if a tweet contains at least one specific keyword
# Test if there are specific numbers of tweets
def test_search_tweets():
    search_tweets_keyword = "BostonUniversity"
    search_tweets_total_tweets = 5
    keyword_counter = 0
    search_tweets_result = tga.search_tweets(keyword=search_tweets_keyword, total_tweets=search_tweets_total_tweets)
    for tweet in search_tweets_result:
        cleaned_tweet = tga.clean_tweets(tweet.text.encode('utf-8'))
        for words in cleaned_tweet:
            if tweet == search_tweets_keyword:
                keyword_counter += 1
    assert keyword_counter >= search_tweets_total_tweets, 'Each tweet should at least have one keyword'


# Test if tweets were cleaned up to specific format
def test_clean_tweets():
    search_tweets_keyword = "BostonUniversity"
    search_tweets_total_tweets = 5
    alpha_sign = 1
    search_tweets_result = tga.search_tweets(keyword=search_tweets_keyword, total_tweets=search_tweets_total_tweets)
    for tweet_words in search_tweets_result:
        cleaned_tweet = tga.clean_tweets(tweet_words.text.encode('utf-8'))
        for tweet_alpha in cleaned_tweet:
            if tweet_alpha.isalpha() == 0:
                alpha_sign = 0
                break
    assert alpha_sign == 1, 'Tweets should only be letters after clean_tweets()'


# Test the sentiment part
def test_get_sentiment_score_positive():
    assert tga.get_sentiment_score('I really like the book') >= 0.25


def test_get_sentiment_score_negative():
    assert tga.get_sentiment_score('I really hate the book') <= -0.25


def test_get_sentiment_score_neutral():
    assert (-0.25 <= tga.get_sentiment_score('It is a book') <= 0.25)
