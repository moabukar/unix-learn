# IPv4

So we know that network hosts have a unique address they can be found at. These addresses are known as IP addresses. An IPv4 address looks something like this:

<pre>204.23.124.23</pre>

This address actually contains two parts, the network portion that tells us know network it's on and the host portion that tells us which host on that network it is. For this course we will mostly be discussing IPv4 addresses, which are what you commonly will see when referring to IP addresses. 

An IP address is separated into octets by the periods. So there are 4 octets in an IPv4 address. If you know a bit of computer science, an octet is 8 bits and 8 bits actually equal 1 byte, so we also refer to an IPv4 address as having 4 bytes. We use bits frequently when dealing with subnets and IP addresses.

You can view your IP address with the ifconfig -a command:

<pre>
mo:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce  
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
</pre>

As you can see my IPv4 address is: 192.168.1.129

### Packet structure of IPv4 vs IPv6

#### IPv4

- Every packet has a source and destination IP address
- Protocol field (which is layer 4) like ICMP, TCP, UDP
  - If you're storing TCP data inside a packet, this value will be 6
  - If you're storing UDP data inside a packet, this value will be 17
  - If you're storing ICMP data inside a packet, this value will be 1
- Bulk of the field within a packet is taken up by the data. 
- A field called TTL

## Exercise

Find your IP address with ifconfig.

## Quiz Questions 

Click the right arrow to view the answers

<details>
<summary>How many bytes are in an IPv4 address?</summary>
4
</details>
