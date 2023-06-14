CREATE KEYSPACE market
WITH
    replication = { -- Create cycling keyspace on a single node evaluation cluster
        'class': 'SimpleStrategy',
        'replication_factor': '1'
    } AND
    durable_writes = true
;
