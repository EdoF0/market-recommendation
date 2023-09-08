-- COPY can be only executed through command line - cqlsh
-- COPY documentation is at the bottom of this page https://docs.scylladb.com/stable/cql/cqlsh.html

COPY market.market (
    userid,
    time1_workday_morning,
    time1_workday_afternoon,
    time1_workday_evening,
    time1_workday_night,
    time1_weekend_morning,
    time1_weekend_afternoon,
    time1_weekend_evening,
    time1_weekend_night,
    time2_morning_early,
    time2_morning,
    time2_launch,
    time2_afternoon,
    time2_evening,
    time2_night,
    time2_sleep,
    L00_50,
    L51_100,
    L101_250,
    L251_500,
    L501_1000,
    L1001_2500,
    L2501_5000,
    L5001_10000,
    L10001_more,
    categories1_artandentertainment,
    categories1_automotive,
    categories1_business,
    categories1_careers,
    categories1_education,
    -- categories1_emotions,
    categories1_famigliaegenitorialita,
    categories1_famigliaegenitorialitaother,
    categories1_familyandparenting,
    categories1_finance,
    categories1_foodanddrink,
    categories1_healthandfitness,
    categories1_hobbiesandinterests,
    categories1_homeandgarden,
    categories1_intentions,
    categories1_lavoro,
    categories1_lawgovtandpolitics,
    categories1_news,
    categories1_pets,
    categories1_realestate,
    categories1_religionandspirituality,
    categories1_science,
    -- categories1_sentiment,
    categories1_shopping,
    categories1_societa,
    categories1_society,
    categories1_sports,
    categories1_styleandfashion,
    categories1_technologyandcomputing,
    categories1_travel,
    categories1_uncategorized,
    sum_time1,
    sum_time2,
    sum_length,
    sum_categories1
)
FROM '/home/marketraw/market.csv'
WITH
    DELIMITER=',' AND
    HEADER=TRUE AND
    -- stability and performance options for large rows, keep in mind that the underlying disk is an SSD
    MINBATCHSIZE=1 AND
    MAXBATCHSIZE=1 AND -- rows are very large, so keep batch size small
    CHUNKSIZE=2 AND -- and lower the chunk size too, keep this >= MAXBATCHSIZE
    --INGESTRATE=1000 AND
    --NUMPROCESSES=2 AND
    -- stats and errors
    REPORTFREQUENCY=1 AND
    MAXATTEMPTS=10 AND
    ERRFILE='/home/marketraw/market-failed.scylla-error.csv' -- all rows that could not be imported are saved here
;

-- Tests
-- min batch | max batch | chunk
-- 1 4 8+(8, 16, 32, ...): fail
-- 1 4 4: 1570 row/s, with some fails at around 10 millions (falied attempt 1 of 10)
-- 1 2 4+(4, 8, 16, 32, ...): fail
-- 1 2 2: 1200 row/s, without any fails
