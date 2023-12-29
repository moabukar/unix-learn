# Famous WWW question

## Question

You are tasked with explaining how a client computer communicates with a web server, specifically accessing "google.com".Consider the entire journey of a request from a client to the server step by step. 

<details>
<summary>Solution</summary>

### **DNS Resolution Expanded:**

- **Initial Client Query**: The process begins with the client (your computer) checking its local DNS cache to see if it already knows the IP address for "google.com". If not, the DNS query process starts.
- **/etc/resolv.conf and Local DNS Resolver**: The query is directed to the DNS server specified in the client's **`/etc/resolv.conf`** file, typically the local router or a DNS server provided by the ISP (e.g., Comcast).
- **Recursive and Non-Recursive Queries**: The ISP's DNS resolver performs a recursive query, contacting root servers, then TLD servers for ".com", and finally the authoritative name servers for "google.com". These authoritative servers are specified by Google when registering the domain.
- **Zone Files and Record Types**: The authoritative servers check their zone files for a forward lookup (hostname to IP address) and respond with the appropriate A or AAAA record.
- **Caching and TTL**: Each DNS server along the path may cache the response based on the TTL to expedite future queries.

### **2. Network Communication with TCP and BGP:**

- **Routing Table and Default Gateway**: The client's routing table is consulted. If there's no direct route to the destination network, the packet is sent to the default gateway.
- **ARP and MAC Address Resolution**: For local network communication, ARP (Address Resolution Protocol) is used to find the MAC address of the next hop, typically the router.
- **BGP and Internet Routing**: As the packet moves beyond the local network, BGP at the ISP's Internet gateway determines the best path across various Autonomous Systems to reach the destination IP.
- **TCP 3-Way Handshake**: Once the correct route is established, a TCP 3-way handshake (SYN, SYN-ACK, ACK) is executed to establish a reliable connection with the server.

### **3. HTTPS, SSL, and Load Balancers:**

- **TLS/SSL Handshake**: For secure HTTP (HTTPS), a TLS/SSL handshake occurs, involving encryption algorithm negotiation, key exchange, and certificate verification.
- **Load Balancing**: If the server, such as "google.com", is behind a load balancer, the load balancer distributes incoming requests to prevent bottlenecks. It may operate in either in-line mode (handling both incoming and outgoing connections) or DSR (Direct Server Return) mode, where responses bypass the load balancer.
- **Server Processing and HTTP**: The web server (e.g., Apache running in pre-fork or worker mode) processes the HTTP request. Pre-fork uses separate processes for each request, while worker mode uses threads.

### **4. HTTP Request and Response:**

- **Client HTTP Request**: The browser sends an HTTP GET request for "google.com".
- **Server Response**: The server processes the request and sends back an HTTP response with the webpage content.

### **5. Rendering and Further Requests:**

- **Web Content Rendering**: The browser renders the webpage from the HTML, CSS, and JavaScript content.
- **Additional Resource Requests**: For additional resources (images, scripts, etc.), the browser makes further HTTP(S) requests.

### **6. Persistent Connections and HTTP/2:**

- **TCP Keep-Alive**: TCP connections might be kept open for a short period for efficiency.
- **HTTP/2 Features**: Parallel resource loading and multiplexing over the same connection are utilized for better performance.

### **7. Connection Closure:**

- **TCP Teardown**: The connection is eventually closed through a TCP four-way handshake or by timeout.

### **8. Additional Networking Concepts:**

- **TCP/UDP Differences**: TCP is used for reliable, connection-oriented transmissions, while UDP is used for simpler, connectionless communication.
- **Other Routing Protocols**: Besides BGP, interior routing protocols like RIP and OSPF are used within Autonomous Systems for routing decisions.

### **9. Advanced DNS and HTTP Topics:**

- **DNS SOA Records**: The Start of Authority (SOA) record in DNS holds important administrative information about a zone.
- **Apache and SSL Configuration**: Setting up Apache for web hosting and configuring SSL for secure communication are advanced topics in HTTP and web server management.

</details>
