## ARP (Address Resolution Protocol)

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

## Quiz Questions

Click the right arrow to view the answers

<details>
<summary>1. What is the primary function of ARP in a network?</summary>
ARP (Address Resolution Protocol) is used to map an IP address to its corresponding MAC address.
</details>

<details>
<summary>2. How does ARP handle the communication when a device wants to communicate with another device on the same local network?</summary>
ARP broadcasts a request to the local network to find the MAC address associated with the destination IP address. The device with the matching IP address responds with its MAC address.
</details>

<details>
<summary>3. What is the role of ARP when dealing with Layer 3 packets?</summary>
ARP (Address Resolution Protocol) is used to find the MAC address corresponding to a given IP address, allowing a Layer 3 packet to be encapsulated inside a frame for transmission.
</details>

<details>
<summary>4. In the context of ARP, what happens when a device needs to communicate with a destination within the same local network?</summary>
ARP broadcasts a request within the local network to find out the MAC address associated with the destination IP address. The device holding that IP address responds with its MAC address, enabling direct communication.
</details>

<details>
<summary>5. Describe the process of ARP in the scenario where Laptop A (IP: 133.33.3.7) wants to send data to Laptop B (IP: 133.33.3.10) on the same network.</summary>
Laptop A, using ARP, broadcasts a request to find the MAC address of Laptop B. Laptop B, recognizing its IP in the request, responds with its MAC address. Laptop A then encapsulates the packet in a frame with Laptop B's MAC address and sends it over the network. Laptop B receives the frame, recognizes the MAC address, processes the frame, and sends the packet to its Layer 3 for further handling.
</details>
