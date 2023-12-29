# UDP

### **UDP ✅ (Layer 4)**

- User Diagram Protocol
- Simple protocol to send and recieve data
- Prior communication not required (yes it can be easy but also a double edged sword due to security)
- Stateless - no knowledge is stored on the host
- 8 byte header datagram
- Use cases >> video streaming, VPN, DNS, webRTC
- Mutliplexing & demultiplexing
    - >> sender multiplexes all its app into UDP
    - receiever demultideplx UDP datagrams to each app
- Source & Dest port
    - *App1 on 10.0.0.1 sends data to AppX on 10.0.0.2*
    - *Destination Port = 53*
    - *AppX responds back to App1*
    - *We need Source Port so we know how to send back data*
    - *Source Port = 5555*
- UDP Pros & Cons
    - Pros:
        - Simple protocol
        - header size is small so datagrams are small
        - uses less bandwith
        - stateless
        - consumes less memory (non state stored in server/client)
    - Cons:
        - No Ack (acknowledgement)
        - No guaranteed delivery
        - Connection-less - anyone can send data without prior knowledge
        - No flow control
        - No congestion control
        - No ordered packets
        - Security - can be easily spoofed
- Summary
    - UDP is layer 4 protocol
    - uses ports to address processes
    - Stateless

UDP is a transport layer protocol. DNS is an application layer protocol that runs on top of UDP (most of the times). Before jumping into UDP, let's try to understand what an application and transport layer is. Here's how they interact with each other:

1. Application and Transport Layers: The transport layer (UDP, in this case) ensures that data from the application layer (like a DNS request) reaches the intended destination.

2. Port Usage: DNS servers typically listen on port 53. Clients send DNS requests using a random source port number above 1024, targeting port 53 on the server.

3. Kernel's Role: The client's kernel sends the request using the sendto system call. The server's kernel receives it, checks the port number, and forwards it to the DNS server process using recvfrom. This process is known as multiplexing and demultiplexing.


## Characteristics of UDP

- UDP is designed for simplicity and low overhead, performing only multiplexing and demultiplexing.
- Unlike TCP, UDP does not provide reliable communication, flow control, or congestion control. Any additional requirements must be implemented at the application level.

## Example:

A basic example involves a UDP client/server where the client sends a "Hello World" message to a server listening on port 5005. The server receives and prints this message.

## Applications in DevOps & Software Engineering


1. Buffer Management in Slow Networks: In scenarios where the underlying network is slow, the sendto system call might hang if the UDP layer can't queue packets efficiently. Increasing sysctl variables like net.core.wmem_max and net.core.wmem_default can help manage this by providing a larger buffer, which can accommodate more data during network slowdowns, thus maintaining throughput.

2. Managing Fast Senders and Slow Receivers: If the receiving process is slower than the sending rate, the kernel may need to drop packets if its buffer gets full, since UDP doesn’t manage flow control. To mitigate this, increasing the rmem_default and rmem_max sysctl variables can provide a larger buffer on the receiving end, reducing the likelihood of packet loss in such scenarios.
