# ssi-jmx-telegraf

## Usage

```
docker-compose up -d
```

Confirm the following containers are running:

```
[root@server-286663899-1-287463268 telegraf]# docker ps
CONTAINER ID        IMAGE                                    COMMAND                  CREATED             STATUS              PORTS                                                  NAMES
3e894ebcafd3        telegraf                                 "/entrypoint.sh teleg"   2 minutes ago       Up 5 seconds        8092/udp, 0.0.0.0:6280->6280/tcp, 8125/udp, 8094/tcp   telegraf_ind1-ng
9e824cbff9af        telegraf                                 "/entrypoint.sh teleg"   2 minutes ago       Up 5 seconds        8092/udp, 0.0.0.0:7031->7031/tcp, 8125/udp, 8094/tcp   telegraf_gsp1-ng
c8a9a506ae4d        telegraf                                 "/entrypoint.sh teleg"   2 minutes ago       Up 6 seconds        8092/udp, 8125/udp, 8094/tcp, 0.0.0.0:9273->9273/tcp   telegraf_wildfly
f1cd376e6cc9        telegraf                                 "/entrypoint.sh teleg"   2 minutes ago       Up 4 seconds        8092/udp, 0.0.0.0:7853->7853/tcp, 8125/udp, 8094/tcp   telegraf_mco1-ng
135215667d2a        telegraf                                 "/entrypoint.sh teleg"   2 minutes ago       Up 4 seconds        8092/udp, 8125/udp, 8094/tcp, 0.0.0.0:8103->8103/tcp   telegraf_lax1-ng
1edb376b799f        telegraf                                 "/entrypoint.sh teleg"   2 minutes ago       Up 3 seconds        8092/udp, 0.0.0.0:7356->7356/tcp, 8125/udp, 8094/tcp   telegraf_phl1-ng
612992e88e8d        telegraf                                 "/entrypoint.sh teleg"   2 minutes ago       Up 4 seconds        8092/udp, 8125/udp, 8094/tcp, 0.0.0.0:8240->8240/tcp   telegraf_atl1-ng
```
