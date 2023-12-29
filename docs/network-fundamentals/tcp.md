# TCP

### TCP ✅ (Layer 4)

- Transmission control protocol
- “Controls” the transmission unlike UDP which is a firehose
- Connection
- Requires handshake
- 20 bytes headers segment
- Stateful
- TCP >> Reliable comms, Remote shell (SSH), database connections, web comms, any bidirectional comms
- TCP Connection
    - Connection is layer (because its a session)
    - Connection is an AGREEMENT between client and server
    - Must create connection to send data
    - Connection is identified by 4 properties
        - SourceIP-SourcePort
        - DestinationIP-DestinationPort
    - Can’t send data outside connection
    - Sometimes called socket or file descriptor
    - Requires 3 way TCP handshake (ACK. SYN-ACK, ACK)
    - Segments are sequenced and ordered
    - Segments are acknowledge
    - Lost segments are retransmitted
- Multiplexing and demultiplexing
    - *Sender multiplexes all its apps into TCP connections*
    - R*eceiver demultiplex TCP segments to each app based on connection pairs*
- Connection Establishment
    - *App1 on 10.0.0.1 want to send data to AppX on 10.0.0.2*
    - *App1 sends SYN to AppX to synchronous sequence numbers*
    - *AppX sends SYN/ACK to synchronous its sequence number*
    - *App1 ACKs AppX SYN.*
    - *Three way handshake*
- Sending data
    - App1 sends data to App 2
    - App1 encapsulates the data in a segment and send it
    - App 2 acknowledges the segment
    - Hint:*: Can App1 send new segment before ack of old segment arrives?*
- Lost data >> App1 sends segment 1,2 and 3 to App 2, Seg 3 is lost, App 2 acknowledge 3, App1 resend seq 3
- Closing connection
    - App 1 wants to close the connection
    - App1 sends FIN, App2 ACK
    - App2 sends FIN, App1 ACK
    - 4 way handshake > >FIN, ACK, FIN, ACK
- Summary
    - Layer 4
    - “Controls” the transmission unlike UDP which is a firehose
    - Introduces connection concept
    - Retransmission, acknowledgement, guaranteed delivery
    - Stateful, connection has a state
- Pros & Cons of TCP
    - Pros
        - Guaranteed delivery
        - No one can send data without prior knowledge
        - Flow control and congestion control
        - Ordered packets, no corruption or app level work
        - More secure than UDP and can’t easily be spoofed
    - Cons
        - large overhead compared to UDO
        - more bandwith
        - stateful: consumes memory on server and client
        - considered high latecny for certain workloads (slow start/congestion/acks)
        - Does too much at a low level (hence QUIC protocol intro)
            - Single connection to send multiple streams of data (HTTP reqs)
            - Stream 1 has nothing to do with stream 2
            - Both steam 1 and steam 2 packets must arrive)
        - TCP meltdown
            - Not a good candidate for VPN
  
## Summary

TCP is a transport layer protocol like UDP but it guarantees reliability, flow control and congestion control.
TCP guarantees reliable delivery by using sequence numbers. A TCP connection is established by a three way handshake.

1. Initiation: The client begins by sending a SYN (synchronize) packet with a sequence number to the server.
   
2. Response: The server acknowledges (ACK) this packet, sends back its SYN packet with a different sequence number.

3. Final Acknowledgment: The client sends an ACK for the server's SYN, completing the handshake and establishing the connection.

After this, data transfer is reliable. Each packet sent is tracked with sequence numbers and acknowledgments. Missing packets trigger retransmissions, ensuring reliability.

<!-- ![3-way handshake](img/established.png) -->

```bash
#To understand handshake run packet capture on one bash session
tcpdump -S -i any port 80
#Run curl on one bash session
curl www.google.com
```

<!-- ![tcpdump-3way](img/pcap.png) -->

## TCP Architecture

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


## Flow Control and Congestion Control:

Flow Control: Managed through the 'win size' field in each TCP segment, indicating the available buffer size for incoming data. It prevents issues where the sender is faster than the receiver.
Congestion Control: Governs the number of unacknowledged segments in transit to avoid network congestion.
<!-- ![Connection tearing](img/closed.png) -->

Armed with our TCP and HTTP knowledge lets see how this is used by SREs in their role

## Connection Termination:

Closing a TCP connection involves:

The client or server initiates closure with a FIN (finish) packet.
The recipient acknowledges with an ACK, sends its FIN packet.
The initiator responds with an ACK, entering a 'time-wait' state to avoid confusion from delayed packets. This state lasts for a period like 2*MSS (120 seconds).

## Applications in DevOps & Software Engineering

1. Load Balancing: Knowledge of TCP and HTTP is crucial for implementing load balancers, which can vary in method (like L4 or L7 load balancing).

2. Throughput Optimization: Adjusting sysctl variables for rmem and wmem can enhance throughput.

3. Connection Handling: Variables like tcp_max_syn_backlog and somax_conn influence how many connections can be processed before acceptance by an application, crucial for single-threaded apps.

4. Managing Connections: Avoiding file descriptor exhaustion involves strategies like tweaking tcp_reuse and tcp_recycle, or using connection pools.

5. Performance Analysis: Differentiating between application and network issues, like identifying socket states (e.g., Close_wait) or retransmissions, is essential for pinpointing performance bottlenecks.
