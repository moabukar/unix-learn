# OSI

## Layer 1 - Physical

- Layer 1 specifications define the transmission and reception of raw BIT STREAMS between a device and a shared physical medium.
- Physical medium can be copper (electrical signals), fibre (light), wifi (radio frequencies or waves)
- Like a physical hub used to connect multiple devices together
- No device addressing, all data is processed by all devices. It's liek shouting in a room without saying any names and everyone hears it. This is a limitation and it's solved by layer 2.
- No media access control

## Layer 2 - Data Link

- Runs over layer 1 and it requires a functional layer 1 to operate
- Higher layers build on lower layers
- Frames are a format used in layer 2 to send information over a layer 2 network
- Layer 2 also introduces a new unique hardware address aka a MAC address. This address is uniquely assigned to a specific hardware.
  - MAC address is formed of 2 parts:
    - OUI (Organizationally Unique Identifier) - first 3 bytes of the MAC address (assigned to companies who manufacture network devices)
    - NIC (Network Interface Controller) - last 3 bytes of the MAC address
- Layer 2 uses layer 1: This means that a layer 2 or ethernet frame can be transmitted onto the shared physical medium by layer 1. These are converted to voltages, RF or light
- Layer 2 provides frames & Layer 1 handles the physical transmission and reception onto and from the physical medium
- So when layer 1 is transmitting a frame onto the physical medium, layer 1 doesn't understand the frame. Layer 1 simply transmits raw data onto the physical medium. 

- Layer 2 has different parts:
  - Preamble bits & start frame delimiter (the function of this is to allow devices to know that it's the start of a frame)
  - Next is the destination and source MAC address. All devices on a layer 2 network have a unique MAC address
  - And a frame can be sent to a specific device by putting its MAC address destination. Or you can put all Fs if you want to send the frame to every device on the local network. This is called a broadcast.
  -  Next is Ethertype which is a layer 3 protocol. Layer 3 uses layer 2 frames for device to device communication on a local network. So when recieving a frame at the other side, you need to know which layer 3 protocol originally put data into that frame. A common example is IP or Internet Protocol. And this is what the ethertype field is for. It tells the receiving device which layer 3 protocol put data into the frame.
  -  These 3 fields (Dest MAC address, Source MAC address, Ethertype) are called the MAC header of the frame.
  -  After the header, it's the payload. It contains the data that the frame is sending. The data is generally provided by the layer 3 protocol. This process is called encapsulation. You have something which layer 3 generates, often this is an IP packet and it's put inside an ethernet frame. It's encapsulated in that frame. The frame delivers that data to a different layer 2 destination. 
  -  At the end of the frame is the frame check sequence which is used to identify any errors in the frame. 
- Using a HUB (let's say we have 4 devices connected to a HUB) - a hub is a layer 1 device. The data can have collisions. What you need is a switch. 
  - A switch is a layer 2 device. Works the same way physically as a HUB but it understands layer 2.
  - It maintains a MAC address table. Switches over tie learn what's connected to each port. When a switch sees frames, it can interpret frames, it can intercept them and see the source and destination MAC addresses. So over time, with this network, the MAC address table will be populated with each of the devices. So the switch will store the MAC addresses it sees on a port and the port itself. 
  - Switches are intelligent. They don't just repeat the physical level. They interpret the frames and they can make decisions based on the source and destination MAC address table.
  - So switches store and forward frames. It doesn't repeat like a dumb layer 1 device. It means it wont forward collisions. In fact, each port on the switch is a separate collision domain. So if there's a collision on one port, it won't affect the other ports. The switch will not forward that corrupted data to the other ports.
  - Layer 2 is the foundation for all networks which we use day to day. It's how our wired networks work. It's how our wifi networks work. It's how the internt works which is a huge collection of interconnected layer 2 networks.
  - The name itself stands for an inter-network of networks.

### Summary of when adding layer 2

- Identifiable devices using MAC addresses. Allows for device to device comms
- Media access control (sharing) - devices can share media in a nice way - avoiding collisions and cross talk
- Collision detection (when using switches)
- Unicase 1:1, Broadcast 1:All, Multicast 1:Many
- We have switches - basically like hubs but with super powers (layer 2) which are more intelligent and can make better decisions compared to layer 1 - ability to scale and avoid collisions

## Layer 3 - Network

- Let's say you have LAN 1 and LAN 2 which are isolated networks. Devices on each local network can communicate with each other but not outside of that layer 2 network
  - Ethernet is a layer 2 protocol. Generally used for local networks. Long distance point to point connections are not possible with ethernet and will use more suitable protocols like PPP (Point to Point Protocol), MPLS (Multi Protocol Label Switching), Frame Relay, ATM (Asynchronous Transfer Mode)
  - Layer 2 is the layer of the OSI stack which moves frames. Moving frames from a local source to a local destination.
  - So to move data between different local networks, which is known as inter-networking, this is where the internet comes from, we need layer 3
- Layer 3 adds the internet protcol or IP. You get IP addresses which across networking addresses which you can assign to devices and these can be used to communicate between different local networks using routing.
- IP packets are moved source to destination across the internet through many intermediate networks. Devices called routers which are layer 3 devices are used to move IP packets across different networks.
- They encapsulate IP packets into layer 2 ethernet frames. So they take the IP packet and put it into a layer 2 frame. 
- Encapsulaton here means that an IP packet is put inside an ethernet frame for that part of the journey.

### IP & Packets

- Packets in many ways are similar to frames. They contain data to be moved and they have a source and dest address. With frames, both the source and dest address are moved across a LAN. With IP packets, the source and dest address are moved across the internet and could be on opposite sides of the planet.

### Packet structure of IPv4 vs IPv6

#### IPv4

- Every packet has a source and destination IP address
- Protocol field (which is layer 4) like ICMP, TCP, UDP
  - If you're storing TCP data inside a packet, this value will be 6
  - If you're storing UDP data inside a packet, this value will be 17
  - If you're storing ICMP data inside a packet, this value will be 1
- Bulk of the field within a packet is taken up by the data. 
- A field called TTL
- And other stuff too..

#### IPv6

- Source & IP (Bigger & therefore, larger addresses)
- Data
- Hop limit (like TTL)
  
### IP addressing (v4)

- Example: 133.33.3.7
  - 133.33 is the 'network' part
  - 3.7 is the 'host' part which represents hosts on that network
  - In this case, 3.7 is laptop on the network 133.33
- Note: If the network part of the IP address match between 2 different IP addresses, they are on the same IP network. If they don't match, they are on different IP networks.
- Each part is 8 bits. So 4 parts = 32 bits. This is why IPv4 is 32 bits. Each 8 bit part is called an octet.
- So for example: 133.33.3.7 and 133.33.33.37
  - They are on the same network because the first 2 octets match
  - They are different hosts because the last 2 octets are different
- Now IP addresses are either statically assigned by huamns which is known as static IP addressing or they are assigned dynamically/automatically by a service called DHCP (Dynamic Host Configuration Protocol). So the servers on your network running DHCP server software will automatically assign IP addresses to devices on your network. This is known as dynamic IP addressing.

#### Subnet Masks

- A subnet mask is configured on a host device in addition to an IP address e.g. 255.255.0.0 & this is the same as a /16 prefix.
- Subnet masks are used to identify the network & host part of an IP address.

### Route Tables & Routes 

- Example of packet moving between routers
  - Home > ISP >  AWS/Upstream ISP/Netflix (Remote networks)
  - Create a packet on our local device which has our IP and the source IP address
  - Default route 0.0.0.0/0 sends all packets to ISP
  - Your packet that was generated is now in the router that has multiple network interface cards connecting to all of the remote networks (AWS/Netflix/Upstream ISP)
  - The ISP uses route tables to forward packets/data to remote networks. Every router will have at least 1 route table
  - A route table is a collection of routes: Destination to Next hop/target
  - Packets are routed, hop by hop across the internet. From source to destination. Router compares packet destination IP and route table for matching destinations. The more specific prefixes are preferred (0 lowest, 32 higher). Packet is forwarded to next hop/target. This process is repeated until the packet reaches the destination.
  - Routers can be statically populate or there are protocols such as BGP (border gateway protocol) which allow routers to communicate with each other to exchange which networks they know about and this is how the core of the internet functions
  - Important note: when our ISP router is forwarding the packet through to the AWS router, it's forwarding at layer 2
  - It wraps the packet in a frame. The packet doesn't change. The frame though, it has the AWS router's MAC address as its destination. But how do we determine the MAC address of the AWS router here?
    - We use something called the ARP (Address Resolution Protocol) Continued below!

### ARP (Address Resolution Protocol)

- The ARP is used when you have a layer 3 packet and you want to encapsulate it inside a frame and send that frame to a MAC address. We don't initially know the MAC address and we need a protocol which can find the MAC address for a given IP address
- For example if you communicate with AWS, AWS will be the destination of the IP packets but we will forward via our home router which is the default gateway and so we will need the MAC address of that default gateway to send the frame to containing the packet. This is where ARP comes in
- ARP will give you the MAC address for a given IP address


Example of ARP:

- 2 laptops: Laptop A (133.33.3.7) wants to send data to Laptop B (133.33.3.10). THey are both on the same network since the IPs have same subnet masks
- Laptop A takes the data and passes it to layer 3 which creates packet. The packet has its IP address as the source and laptop B as the destination IP
- Now we need a way of being able to create a frame to put that packet in for a transmission. We need the MAC address of laptop B
- This is what ARP does for us. It’s a process which runs between layer 2 and layer 3. Because both IPs have same subnet mask and it knows they are on the same local network, this is a direct connection. Routers aren’t required here. We don’t use routers for this type of comms
- ARP broadcasts on layer 2. It sends an ARP frame to all Fs as a MAC address and it asks who has the IP address 133.33.3.10. Laptop B is also running ARP. The ARP software sees this broadcast and it responds by saying im that IP address and here is my MAC address
- Now Laptop A has the destination MAC address of laptop B, it can use it to build a frame, encapsulate the packet in this frame and once frame is ready, it can be given to layer 1 and sent across the physical network. Layer 1 receives the physical raw bit stream and hands it off to layer 2 of the laptop. Layer 2 software of the laptop B reviews the dest MAC address and knows it meant for it.
- So it strips off the frame and sends the packet to its layer 3 software. Layer 3 sees the packet and sees it is the intended destination and it de-encapsulates the data and hands it to the game.

## Layer 3 - IP routing

- Example of a packet moving from multiple routers
- ARP is used to obtain a MAC address of another target. If a packet is going from another network, it uses a router. If it’s leaving a router to another one. ARP is used to find the MAC address of the default gateway of the router. The router picks it up in a frame and strips it but realises it’s not meant for it. It encapsulates it ina frame and knows the next hop for another router. The next router picks it up and strips it but finds the destination on the same network. So it uses ARP to find the MAC address of the destination. The destination picks it up and takes the data.

## Layer 3 Summary

- IP addresses (IPv4/6) - cross network addressing
- ARP - find the MAC address for a certain IP
- Routes: where to forward packets
- Route tables: containing multiple routes
- Router: moves packets from source to destination (encapsulating in L2 frames on the way)
- This allows for device to device comms over the internet
- IP doesn’t provide method for channels of comms (SRC IP to DST IP only)
- Layer 3 provides packets and packets only have source and dest IP. So if we have 2 devices, you can only have one stream of comms. So you can’t have different apps on the devices communicating at the same time. And this limitation is solved by layer 4.
- In theory, packets can be delivered out of order. No guarantee it will take the same route


# Layer 4 - Transport Layer

## Layer 3 problems

- Each IP packet on layer 3 is routed independently and isolated from each packet
    - you might think that all IP packets arrive in proper order and good conditions but no:
        - you’re going to have intermittent network conditions
        - packets can arrive in diff conditions and they can be out of order
- Layer 3, specifically IP, providers no method to ensure the ordering of packet arrival and packets can go missing. This can be due to network outages or network conditions which cause temporary routing loops.
- This is the negative of layer and it is solved by Layer 4. With IP only, there is no reliable method of ensuring packet delivery
- Another issue with layer 3 is that if you think back to the structure of IP packets, they have a source and destination field and nothing beyond that to distinguish channels of communication like ports which are solved in layer 4. Packets have only source IP and destination IP, theres is no method of splitting by APP or CHANNEL like ports.
    - You can’t have 2 apps running on the source IP communicating with 2 apps on the destination IP as there is no method of distinguishing between the apps.
    - You could have an SSH connection open as well as a HTTP request running in the background.
- IP also has no flow control: if the source transmits faster than the destinaition can receive, it can sautrate the destination causing packet loss.

## Layer 4 - how does this solve the problem?

- In layer 3, we had IP address and routing. Routed packets across a network of networks
- Layer 4 builds on top of this: It adds 2 new protocols which are TCP & UDP
    - Both of these run on top of IP. If you have heard TCP/IP - this means TCP running on top of IP. At a high level, you would pick TCP when you want reliability and error correction and ordering of data (slower and reliable)
        - It’s used for most of the important application layer protocols such as HTTP, HTTPS, SSH etc
        - TCP is a connection-oriented protocol which means you set up a connection between 2 devices and once set up, it creates a bidirectional channel of communication
    - UDP, on the other hand, is faster, because it doesn’t have the TCP overhead required for the reliable delivery of data. It’s less reliable than TCP
        - There’s a great joke about UDP: I’d tell you about it…. but you might not get it 😁
- Both TCP and UDP run on top of IP. They use IP as transit. TCP just offers a more reliable connection oriented architecture whereas UDP is all about performance
- TCP introduces something called TCP segments. Segments are encapsulated within IP packets. TCP segments are placed inside IP packets. And the packets carry the segments.
    - Segments dont have SRC and DST IP - the packets provide device addressing
    - Inside a TCP segment, you now have SRC port and DST port in addition to SRC IP and DST IP. And this gives the combined TCP/IP protocol. Giving the ability to have multiple streams of conversation or apps running in 1 IP or machine at the same time between 2 devices
    - Inside segments you also have sequence number and is a way of uniquely identifying a particular segment and for ordering purposes
    - You also have acknowledgements. It is a way that one side can indicate it’s received. Every segment transmitted needs to be acknowledged.
    - You also have windows: this defines the number of bytes that indicate that you’re willing to receive between acknowledgements. Once reached, the sender will pause until you acknowledge that amount of data and this is how flow control is implemented. It allows the receive to control the rate at which the sender sends the data.
        - If you use a smaller window, it provides additional levels of control over how quickly you’re sent data
        - Larger windows are more efficient because the header of a TCP segment takes up an amount of space, and the smaller the window, the more headers are involved.
    - Checksums are used for error checking: it means that the TCP layer is able to detect errors and can arrange for retransmission of the data as required
    - There are more fields inside a TCP segment but the above mentioned are the most important
    - All these field together are known as the TCP header. The capacity of the TCP segment remaining is used for data.

### TCP Architecture

- TCP, like IP, is used to allow communications between 2 devices.
- TCP is a connection based protocol. A connection is established between two devices using random port on a client and a known port on the server. Once established the connection is bi-directional. The “connection” is a reliable connection, provided via the segments encapsulated in IP packets.
- You have L3 packets which have no error checking, no ordering, no association.
- Now you have a game laptop and a game server. The game server (the client) uses tcp port 23060 and communicates with the server on tcp port 443
    - This is a communication channel. TCP connections are bidirectional and this means the server will send data back to the client. To do this, it just flips the ports: so the SRC port is TCP 443 on the server and the destination port on the client is 23060.
    - And it’s why you need two sets of rules on a NACL with in AWS. One set for the initiating part (laptop to server) and one set for the response part (server to laptop)
    - This can be conceptually viewed as a channel. These channels aren’t real, they are created using segments.
    - When you hear the term ephemeral ports or high ports, this means the port range that the client picks as the source port. Often you need to add firewall rules allowing all of this range back to the client.

### TCP 3 way handshake

- In the TCP segment structure, there’s something called “Flags n things”
- Flags which can be used to set to alter the connection. e.g. FIN can be used to close, ACK for acknowledgements, syn to sync between sequence numbers

- So you have a client and a server:
    - Before any data can be transferred through TCP, a connection needs to be established and this uses a 3 way handshake
    - So in step 1, the client needs to send a segment to the server. This segment contains a random sequence number. Send a segment with SYN
    - The server responds back with another random sequence number and sends a segment called SYN & ACK.
    - The server then sends back a segment with ACK for acknowledge
    - Now a connection is established and client and server can both send data

