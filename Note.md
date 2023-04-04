
# Configuration of device

## Router

The IPv4 address of the router is `85.26.49.187`
The IPv6 address of the router is `2a02:2788:11c4:6a8:7408:f594:c000:d8`

## Laptop who used wireshark the packet

```bash
2: wlp1s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether ac:ed:5c:cc:cd:42 brd ff:ff:ff:ff:ff:ff
    inet 192.168.10.158/24 brd 192.168.10.255 scope global dynamic noprefixroute wlp1s0
       valid_lft 85729sec preferred_lft 85729sec
    inet6 2a02:2788:11c4:6a8:7408:f594:c000:d8/64 scope global temporary dynamic 
       valid_lft 604131sec preferred_lft 85217sec
    inet6 2a02:2788:11c4:6a8:1e8a:1795:3a14:b995/64 scope global dynamic mngtmpaddr noprefixroute 
       valid_lft 1209599sec preferred_lft 604799sec
    inet6 fe80::a5cd:5a1d:db3a:5572/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```
The IPv6 use for this device is `2a02:2788:11c4:6a8:1e8a:1795:3a14:b995/64`

## Laptop who received the communication
   
``` bash
2: wlp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 7c:50:79:40:0d:e4 brd ff:ff:ff:ff:ff:ff
    inet 192.168.10.140/24 brd 192.168.10.255 scope global dynamic noprefixroute wlp4s0
       valid_lft 86302sec preferred_lft 86302sec
    inet6 2a02:2788:11c4:6a8:59a4:62d2:2b55:8794/64 scope global temporary dynamic 
       valid_lft 604704sec preferred_lft 85842sec
    inet6 2a02:2788:11c4:6a8:df1a:b803:c261:990b/64 scope global dynamic mngtmpaddr noprefixroute 
       valid_lft 1209599sec preferred_lft 604799sec
    inet6 fe80::a6be:75bc:cbc9:63ac/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```
The IPv6 use for this device is `2a02:2788:11c4:6a8:df1a:b803:c261:990b/64`