# EC601_Project3
- 2021 Fall Boston University Class EC601 Project 3
- Bingquan Cai

## Test 1
The function of `search_tweets()` will come out with the tweets we want. The number of tweets should be equal to the number we set and these tweets should contain the keyword that we set.

Therefore, the function of `test_search_tweets()` will test `search_tweets()`. It will test if the total number of keywords in all tweets was bigger than or equal to the number we set before, for each tweet we get must have at least one keyword in it.

## Test 2
The function of `clean_tweets()` can clean up tweets into specific format. It will remove the username, links and numbers in every tweets. It will also convert all of the characters into lower space and remove every unnecessary space.

The function of `test_clean_tweets()` is going to test if tweets were cleaned up to specific format which should only be letters after `clean_tweets()`.

# Test 3
The function of `test_get_sentiment_score_positive()`, `test_get_sentiment_score_negative()` and `test_get_sentiment_score_neutral()` is going to test the sentiment part.
