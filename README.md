# Data analysis from market data

Recommendation for new users based on aggregated interest profiles.

This is a university project based on analyzing a dataset containing per-user anonymized interest profiles. The main goal of our analysis is to get a general interest profile given one interest. This can be used to make relevant suggestions to new users visiting a page for the first time (do not have an interest profile yet), given that the page is an article with a related interest category.

## Dataset

The original dataset is a big `csv` file of 22078467 (~22 million) records and 1103 columns divided in the following groups. Each column except `userid` has a numerical percent value that should sum to 100% inside the same column group for every row.

- `time1`: relative number of articles seen divided in workday or weekend and for each of the two options divided in morning, afternoon, evening, night
- `time2`: relative number of articles seen divided in morning early, morning, launch, afternoon, evening, night, sleep
- `L`: relative number of articles seen divided by text length 00 to 50, 51 to 100, 101 to 250, 251 to 500, 501 to 1000, 1001 to 2500, 2501 to 5000, 5001 to 10000, 10001 and more
- `categories1`: relative number of articles seen divided into 31 categories, it's the first category granularity level
- `categories2`: relative number of articles seen divided into 360 categories, it's the second category granularity level
- `categories2`: relative number of articles seen divided into 575 categories, it's the third category granularity level
- `sentiments1`: sentiment analysis of the text by a prototype model, we ignore this columns
- `feelings1`: sentiment analysis of the text by a prototype model, we ignore this columns
- `userid`: anonymized user identifier, every row has a different value since each row is an already computed profile of interest

Note that we do not have the total number of visits `impressions` for every user.
