from ipaddress import *

#1

ip = "172.16.160.0"
mask = "255.255.240.0"
net = ip_network(f"{ip}/{mask}", 0)
k = 0
for x in net.hosts():
    x = bin(int(x))[2:]
    if x.count("1") % 4 != 0:
        k += 1
print(k)    

#2

ip = "172.17.167.18"
mask = "255.255.240.0"
net = ip_network(f"{ip}/{mask}", 0)
for x in net.hosts():
    print(x)

#3

ip = "137.219.220.63"
for mask in range(30, 1, -1):
    net = ip_network(f"{ip}/{mask}", 0)
    if ip_address(ip) in net.hosts():
        print(mask)

#4

ip1 = "61.58.73.42"
ip2 = "61.58.75.136"
for mask in range(30, 1, -1):
    net1 = ip_network(f"{ip1}/{mask}", 0)
    net2 = ip_network(f"{ip2}/{mask}", 0)
    if net1 == net2:
        a = mask
        print(a)
        break
b = 2**(32-a) // 2 - 2 
print(b)


#5

ip = "172.30.0.0"
mask = "255.254.0.0"
net = ip_network(f"{ip}/{mask}", 0)
k = 0
for x in net:
    x = bin(int(x))[2:]
    if x.count('1') % 12 != 0:
        k += 1
print(k)

#6

ip = "172.16.168.0"
mask = "255.255.248.0"
net = ip_network(f"{ip}/{mask}", 0)
k = 0
for x in net:
    x = bin(int(x))[2:]
    if x.count('1') % 5 != 0:
        k += 1
print(k)

#7

ip = "192.168.0.0"
mask = "255.255.192.0"
net = ip_network(f"{ip}/{mask}", 0)
k = 0
for x in net:
    x = bin(int(x))[2:]
    if x.count('1') > x.count('0'):
        k += 1
print(k)

#8

ip1 = "121.171.5.70"
ip2 = "121.171.5.107"
for mask in range(30, 1, -1):
    net1 = ip_network(f"{ip1}/{mask}", 0)
    net2 = ip_network(f"{ip2}/{mask}", 0)
    if net1 == net2:
        if ip_address(ip1) in net1.hosts() and ip_address(ip2) in net2.hosts():
            break
k = 0
for x in net1:
    k += 1
print(k)
    

#9

ip1 = "151.172.115.121"
ip2 = "151.172.115.156"
for mask in range(1, 31):
    net1 = ip_network(f"{ip1}/{mask}", 0)
    net2 = ip_network(f"{ip2}/{mask}", 0)
    if net1 != net2:
        print(mask)

#10

ip = "192.168.32.160"
ip = ip_address(ip)
mask = "255.255.255.240"
mask = ip_address(mask)
net = ip_network(f"{ip}/{mask}", 0)
k = 0
for x in net:
    x = bin(int(x))[2:]
    if x.count('0') > 21:
        k += 1
print(k)

#11

ip1 = "192.168.56.192"
mask1 = "255.255.255.192"
ip2 = "192.168.56.208"
mask2 = "255.255.255.240"
net1 = ip_network(f"{ip1}/{mask1}", 0)
net2 = ip_network(f"{ip2}/{mask2}", 0)
k = 0
for x in net1:
    if ip_address(x) not in net2:
        k += 1
print(k)

#12

ip1 = "134.181.67.112"
ip2 = "134.181.94.117"
for mask in range(1, 31):
    net1 = ip_network(f"{ip1}/{mask}", 0)
    net2 = ip_network(f"{ip2}/{mask}", 0)
    if net1 == net2:
        print(net1.netmask)

#13

ip = "192.168.160.0"
mask = "255.255.224.0"
net = ip_network(f"{ip}/{mask}", 0)
mask = ip_address(mask)
mask = bin(int(mask))[2:]
k = 0
for x in net:
    x = bin(int(x))[2:]
    if x.count("1") == mask.count("1"):
        k += 1
print(k)