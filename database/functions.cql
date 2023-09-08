CREATE FUNCTION market.weight(g double, r double)
    RETURNS NULL ON NULL INPUT
    RETURNS double
    LANGUAGE LUA
    AS 'return g/r*100;';

CREATE FUNCTION market.score(g double, t double, r double)
    RETURNS NULL ON NULL INPUT
    RETURNS double
    LANGUAGE LUA
    AS 'if r==g then return 0 else return t/(r-g)*100 end;';

CREATE FUNCTION market.userinterest(g double, t double, r double)
    RETURNS NULL ON NULL INPUT
    RETURNS double
    LANGUAGE LUA
    AS 'if r==g then return 0 else return (100*g*t)/(r*(r-g)) end;';

CREATE FUNCTION market.interest(a double, s double, n int)
    RETURNS NULL ON NULL INPUT
    RETURNS double
    LANGUAGE LUA
    AS 'return 100*n*(a/s);';
-- n is 10682769 for the market      table (market dataset)
-- n is 10000    for the market_test table (market dataset capped at 10000 rows)
CREATE FUNCTION market.interest(a double, s double)
    RETURNS NULL ON NULL INPUT
    RETURNS double
    LANGUAGE LUA
    AS 'return 100*10682769*(a/s);';
-- test with fixed weight sum (categories1_artandentertainment)
CREATE OR REPLACE FUNCTION market.interest(a double)
    RETURNS NULL ON NULL INPUT
    RETURNS double
    LANGUAGE LUA
    AS 'return 100*10682769*(a/80505000);';

CREATE FUNCTION market.interest_short_numerator(g double, t double, r double)
    RETURNS NULL ON NULL INPUT
    RETURNS double
    LANGUAGE LUA
    AS 'if r==g then return 0 else return (g*t)/(r*(r-g)) end;';

CREATE FUNCTION market.interest_short_denominator(g double, r double)
    RETURNS NULL ON NULL INPUT
    RETURNS double
    LANGUAGE LUA
    AS 'return g/r;';

CREATE FUNCTION market.interest_short(n double, d double)
    RETURNS NULL ON NULL INPUT
    RETURNS double
    LANGUAGE LUA
    AS 'return (n/d)*100;';

CREATE FUNCTION market.exponential_test(b double, e double)
    RETURNS NULL ON NULL INPUT
    RETURNS double
    LANGUAGE LUA
    AS 'return b^e;';

-- Test queries

SELECT market.weight(categories1_healthandfitness,sum_categories1) AS weight, userid FROM market.market LIMIT 10;

SELECT market.score(categories1_healthandfitness,categories1_science,sum_categories1) AS interest_score, userid FROM market.market LIMIT 10;

SELECT market.userinterest(categories1_healthandfitness,categories1_science,sum_categories1) AS user_interest, userid FROM market.market LIMIT 10;

SELECT categories1_healthandfitness, categories1_science, sum_categories1, userid FROM market.market WHERE userid = '';

SELECT
    market.interest(AVG(market.userinterest(categories1_healthandfitness, categories1_science, sum_categories1)), SUM(market.weight(categories1_healthandfitness, sum_categories1))) AS interest_healthandfitness_science,
    AVG(market.userinterest(categories1_healthandfitness, categories1_science, sum_categories1)) AS mean,
    SUM(market.weight(categories1_healthandfitness, sum_categories1)) AS weight_sum
FROM market.market_test;

SELECT
    market.interest_short(SUM(market.interest_short_numerator(categories1_healthandfitness, categories1_science, sum_categories1)), SUM(market.interest_short_denominator(categories1_healthandfitness, sum_categories1))) AS interest_healthandfitness_science,
    SUM(market.interest_short_numerator(categories1_healthandfitness, categories1_science, sum_categories1)) AS numerator,
    SUM(market.interest_short_denominator(categories1_healthandfitness, sum_categories1)) AS denominator
FROM market.market_test;
