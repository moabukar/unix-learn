# DNS Deep Dive

You're trying to access www.google.com from your computer, but it's the first time you're visiting the site, and there's no relevant entry in your local DNS cache or hosts file. Describe the sequence of steps taken by the DNS resolver to find the authoritative IP address for www.google.com.

<details>
<summary>Solution: (BASIC) </summary>

1. **Query to Resolver:** The query for www.google.com is sent to the DNS resolver, typically running on a home router or within an ISP.
2. **Root Zone Query:** The resolver, finding no cached entry, queries the root zone servers for .com TLD information.
3. **.com TLD Nameservers:** The root zone directs the resolver to the .com TLD nameservers, managed by Verisign.
4. **Query to .com TLD Nameservers:** The resolver queries one of the .com TLD nameservers for information about google.com.
5. **google.com Nameservers:** The .com TLD nameserver provides the DNS resolver with the nameservers for google.com (e.g., `ns-81.awsdns-10.com`, `ns-659.awsdns-18.net`).
6. **Authoritative Response:** The resolver then queries these nameservers for www.google.com, receiving an authoritative response with the IP address(es).
7. **Caching the Response:** The resolver caches this response for future queries.
8. **Final Step:** The resolver returns the IP address to the local machine, allowing the computer to access www.google.com.

This sequence is known as "walking the DNS tree," and it demonstrates how DNS queries progressively narrow down to the specific zone holding the required records.
</details>


<details>
<summary>Solution: (DEEP DIVE)</summary>

- So in simple, we have a client and it wants to access [google.com](http://google.com). and we need the IP address or addresses which we can connect to in order to access google. Somewhere in the world there is a DNS zone for google.com which has these and contains the records, which links [www.google.com](http://www.google.com) to 1 or more IPs .How do we find this zone
    - That’s what DNS does. It’s the job of DNS which allows you to locate the specific DNS zone and get a query response from the authoritative zone which hosts the DNS records you need
- DNS is huge global distributed database containing lots of DNS records and the function of DNS is to allow you to locate the specific zone which can give you an authoritative answer.
- **Example of a query within DNS:** >> like the Google.com question
    - Imagine we are querying www.google.com. First thing to check is the local DNS cache and hostsfile on the local machine. The hosts file is a static mapping of names to IPs and overrides DNS. Assuming the local client isn’t aware of the DNS name, then next step:
    - A resolver comes in here. A resolver is a type of DNS server often running  on a home router or within an ISP and it will do the query on our behalf. So we send the query to the DNS resolve and it will query for you. The resolver also has a local cache which is used to speed up DNS queries. So if someone has queried [google.com](http://google.com) before, it might be able to return a non-authoritative answer aka local cached response. Assume now there is no cached entry for google.com, then the resolve queries the root zone via one of the root servers. Every DNS server will have these IPs hardcoded and this list is maintained by the OS vendor. The DNS root won’t be able to answer us coz it isn’t aware of google.com but it can help us get closer
    - The root zone contains the records of a .com specifically nameserver records which point at the nameservers for the .com TLD and it returns .com NS
    - So now the DNS resolver can now query one of the .com TLD NS for [www.google.com](http://www.google.com). Assuming that the google.com domain has been registered, the .com zone will contain entries for google.com. Then the details of google.com NS are returned to the DNS resolver. The resolver can now move on:
    - The DNS resolve now queries the [google.com](http://google.com) NS for [www.google.com](http://www.google.com) and because these NS are authoritative for this domains as they host the zone and zonefile for this domain and they’re pointed at by the .com TLD zone, they can return an authoritative response back to the resolver.
    - Now the DNS resolver caches the result in order to improve performance
    - Now the DNS resolver caches the result in order to improve performance for future queries.
    - And this DNS resolver returns the result to our local machine. This is how every DNS query works.
    - Note: No one single Nameserver has all the answers, not even the root NS. But, every query gives you the next step and takes you closer to your query.
        - The root gives you the .com NS, the .com NS gives you the [google](http://google.com)x.com NS, and the google.com NS can give you an authoritative answer
    - This DNS process is also known as “Walking the (”DNS”) tree”
    - This process is on a high level.
- **A bit deeper**
    - Start with root zone when the DNS resolver is querying the root zone. The root zone doesn’t have the info needed but it does know which NS handles .com NS so it can provide this. These NS are run by Verisign which manages the .com TLD. These NS host the .com zone file.
    - We can now query the .com zone. We can’t get answer directly from here but it does know which NS are authoritative for [google.com](http://google.com). These are the network addresses of the servers which host the google.com zone and this is authoritative. This gives us what we need (they look like `[ns-81.awsdns-10.com](http://ns-81.awsdns-10.com)` , `[ns-659.awsdns-18.net](http://ns-659.awsdns-18.net)` etc
    - The above are not IPs, they are another DNS name. This is a CNAME record. To get the IP address for this, you follow the same process again.
</details>
