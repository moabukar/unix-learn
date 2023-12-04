# TCP

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
