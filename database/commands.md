# Frequent commands

Commands ready to be copied and pasted into the container terminal.

### CQLSH

Request timeout is in seconds, 7200 is 2h

```bash
cqlsh --request-timeout=7200
```

### Info

```bash
nodetool status
```

```bash
nodetool tablestats market.market
```

### Flush

Flush in-memory MemTables to SSTables

```bash
nodetool flush market
```

### Edit conf

After editing conf file

```PowerShell
docker exec -it marketdb supervisorctl restart scylla
```

This restarts Scylla without restarting the container

## Shutdown

How to properly shut down Scylla (reference [scylla docs](https://docs.scylladb.com/stable/operating-scylla/procedures/cluster-management/safe-shutdown.html) and and article on Cassandra [packtpub](https://subscription.packtpub.com/book/data/9781789131499/1/ch01lvl1sec08/shutting-down-cassandra))

Disable interactions with other nodes

```bash
nodetool disablegossip
```

Disable client requests

```bash
nodetool disablebinary
```

Force all in-memory data to be written to disk, and prevents all kind of writes meanwhile

```bash
nodetool drain
```

Check the node status is listed as `DN` (`?N` should be ok). Similarly, at node start check the node status is `UN` before doing any operation ([status descriptions](https://docs.scylladb.com/stable/operating-scylla/nodetool-commands/status.html)).

```bash
nodetool status
```

```bash
exit
```

Now the container can be shut down safely and properly
