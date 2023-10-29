# Data analysis from market data

This is a market analysis which starts from a dataset of user profiles based on categories of interest. The aim of the project is not only to extract useful information for a market analysis, but to find a method that allows users visiting the website for the first time to have meaningful suggestions. To suggest categories different from the article the new user is reading, we created a formula that exploits the category of that article to find the most interesting different categories. The formula core is a weighted mean, the weight is a value representing the current category, and the subject is a value of the future category at the net of the first. The result is a matrix of dimension categories × categories with both unexpected and predictable values. The procedure is also expanded to include the time of the day and has much room for enhancement.

This is a university project.

## Dataset

The provided dataset is the output of an aggregation process: we have one record per user.
All the statistics provided are percentages that are simply computed as accesses to the website under a certain condition (described by the column name) divided by the total accesses multiplied by 100.

The analysed dataset comprises 22,078,467 rows and 1,104 columns.
For the sake of synthesis, they have been grouped into 8 macro-categories:

- `time1`: it contains the per-user percentage of accesses divided by time, in particular, there is a distinction between work days or weekend days and among daytime intervals (it comprises 8 columns);
- `time2`: it contains the per user percentage of accesses divided by 7 time intervals in a day (does not distinguish the weekend);
- `length`: it contains the per-user percentage of web pages read with the content having the specified length in characters (it comprises 9 columns);
- `categories1`: it contains the per user percentage of articles read with the specified field of interest, that is a category like Cars, Food, Work... (it comprises 31 columns);
- `categories2`: it contains the per-user percentage of articles read with the specified field of interest at a higher level of granularity; every category in categories2 has a parent in categories1, but not every category in categories1 have children such that the sum of them is the value of the parent category (it comprises 360 columns);
- `categories3`: it contains the per-user percentage of articles read with the specified field of interest at a higher level of granularity; every category in categories3 has a parent in categories2, like between categories1 and categories2 (it comprises 575 columns);
- `sentiments1`: it contains the per user percentage of content with that type of transmitted feeling that can be neutro-neutral, negative, neutral or positive (it comprises 4 columns);
- `feelings1`: it contains the per-user percentage of content with that type of transmitted feeling like anxiety, desire or envy... (it comprises 109 columns);
- `id` (single column): unique identifier different for every row.

There are only numerical positive values in all the dataset, except for the id column which is not numerical. For each row of the dataset, summing the values of any of the columns groups should give a value of 100. We expect the sum to be not exactly 100 for approximation issues. For the categories2 group we expect the sum to be less or equal than 100, since not every value in categories1 can be computed from categories2 values. For the same reason, we expect the categories3 sum (for each row) to be less or equal than the categories2 sum for the same row.

It's important to note that we do not have the total number of visits for a user, then we cannot know if someone who has 100% interest in the automotive category is an anonymous user making just one visit to the website or a professional who only reads automotive articles with his work account.

## Paper

You can find the full paper in the releases section.
