from ipaddress import *

# ip = "195.227.196.12"
# net0 = "195.227.192.0"
# for mask in range(1, 31):
#     net = ip_network(f"{ip}/{mask}", 0)
#     if str(net.network_address) == net0:
#         print(net.netmask)

#8

ip1 = "84.77.95.123"
ip2 = "84.77.96.123"

for mask in range(30, 1, -1):
    net1 = ip_network(f"{ip1}/{mask}", 0)
    net2 = ip_network(f"{ip2}/{mask}", 0)
    if net1 == net2:
        if ip_address(ip1) in net1.hosts() and ip_address(ip2) in net2.hosts():
            print(net1.netmask)

#10

ip = "226.185.90.162"
mask = "255.255.252.0"
ip = bin(int(ip_address(ip)))[2:]
print(ip)
mask = bin(int(ip_address(mask)))[2:]
print(mask)
k = mask.count('0')
ip = ip[-k:]
s = int(ip, 2)
print(s)

#12

mask = "255.255.224.0"
ip = "206.158.124.67"
mask = bin(int(ip_address(mask)))[2:]
ip = bin(int(ip_address(ip)))[2:]
k = mask.count('0')
ip = ip[-k:]
print(int(ip, 2))

#14

ip1 = "118.187.59.255"
ip2 = "118.187.65.115"
ip1 = ip_address(ip1)
ip2 = ip_address(ip2)

for mask in range(1, 31):
    net1 = ip_network(f"{ip1}/{mask}", 0)
    net2 = ip_network(f"{ip2}/{mask}", 0)
    if net1 != net2:
        if ip_address(ip1) in net1.hosts() and ip_address(ip2) in net2.hosts():
            print(mask)
    
#15

ip1 = "151.172.115.121"
ip2 = "151.172.115.156"
ip1 = ip_address(ip1)
ip2 = ip_address(ip2)

for mask in range(1, 31):
    net1 = ip_network(f"{ip1}/{mask}", 0)
    net2 = ip_network(f"{ip2}/{mask}", 0)
    if net1 != net2:
        if ip_address(ip1) in net1.hosts() and ip_address(ip2) in net2.hosts():
            print(mask)

#22

ip = "101.157.240.0"
mask = "255.255.252.0"
net = ip_network(f"{ip}/{mask}", 0)
k = 0
for x in net:
    a = bin(int(x))[2:]
    i1 = a[:len(a)//2]
    i2 = a[len(a)//2:]
    if i1.count("1") > i2.count("1"):
        k += 1
print(k)

#23

ip = "171.128.0.0"
mask = "255.128.0.0"
net = ip_network(f"{ip}/{mask}", 0)
k = 0
for x in net:
    a = bin(int(x))[2:]
    i1 = a[:len(a)//2]
    i2 = a[len(a)//2:]
    if i1.count("1") < i2.count("1"):
        k += 1
print(k)