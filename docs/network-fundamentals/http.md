# HTTP

Till this point we have only got the IP address of google.com. The HTML page of google.com is served by HTTP protocol which the browser renders. Browser sends a HTTP request to the IP of the server determined above.

Request has a verb GET, PUT, POST followed by a path and query parameters and lines of key value pair which gives information about the client and capabilities of the client like contents it can accept and a body (usually in POST or PUT)

```bash
# Eg run the following in your machine and have a look at the headers 
curl google.com -v
```
```bash
❯ curl google.com -v
*   Trying [2a00:1450:4009:815::200e]:80...
* Connected to google.com (2a00:1450:4009:815::200e) port 80 (#0)
> GET / HTTP/1.1
> Host: google.com
> User-Agent: curl/8.1.2
> Accept: */*
>
< HTTP/1.1 301 Moved Permanently
< Location: http://www.google.com/
< Content-Type: text/html; charset=UTF-8
< Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-FTv-58qMVTd49N-ysFjcQA' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
< Date: Mon, 04 Dec 2023 19:36:43 GMT
< Expires: Wed, 03 Jan 2024 19:36:43 GMT
< Cache-Control: public, max-age=2592000
< Server: gws
< Content-Length: 219
< X-XSS-Protection: 0
< X-Frame-Options: SAMEORIGIN
<
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
* Connection #0 to host google.com left intact
```

Here, in the first line GET is the verb, / is the path and 1.1 is the HTTP protocol version. Then there are key value pairs which give client capabilities and some details to the server. The server responds back with HTTP version, Status Code & Status Message. Status codes 2xx means success, 3xx denotes redirection, 4xx denotes client side errors and 5xx server side errors.

We will now jump in to see the difference between HTTP/1.0 and HTTP/1.1. 

```bash
#On the terminal type
telnet  www.google.com 80
#Copy and paste the following with an empty new line by pressing enter at last in the telnet STDIN
GET / HTTP/1.1
HOST:google.com
USER-AGENT: curl
# then press enter
----
Output:
❯ telnet  www.google.com 80
Trying 2a00:1450:4009:820::2004...
Connected to www.google.com.
Escape character is '^]'.
GET / HTTP/1.1
HOST:google.com
USER-AGENT: curl

HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-T1jINmYahlhXaA-iSQDRMw' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
Date: Mon, 04 Dec 2023 19:40:14 GMT
Expires: Wed, 03 Jan 2024 19:40:14 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>

```


This would get server response and waits for next input as the underlying connection to www.google.com can be reused for further queries. While going through TCP, we can understand the benefits of this. But in HTTP/1.0 this connection will be immediately closed after the response meaning new connection has to be opened for each query. HTTP/1.1 can have only one inflight request in an open connection but connection can be reused for multiple requests one after another. One of the benefits of HTTP/2.0 over HTTP/1.1 is we can have multiple inflight requests on the same connection. We are restricting our scope to generic HTTP and not jumping to the intricacies of each protocol version but they should be straight forward to understand post the course.

HTTP is  called **stateless protocol**. This section we will try to understand what stateless means. Say we logged in to google.com, each request to google.com from the client will have no context of the user and it makes no sense to prompt user to login for each page/resource. This problem of HTTP is solved by *COOKIE*. A user is created a session when a user logs in. This session identifier is sent to the browser via *SET-COOKIE* header. The browser stores the COOKIE till the expiry set by the server and sends the cookie for each request from hereon for google.com. More details on cookies are available [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies). Cookies are a critical piece of information like password and since HTTP is a plain text protocol, any man in the middle can capture either password or cookies and can breach the privacy of the user. Similarly as discussed during DNS a spoofed IP of google.com can cause a phishing attack on users where an user can give google’s password to login on the malicious site. To solve both problems HTTPs came in place and HTTPs has to be mandated.

HTTPS has to provide server identification and encryption of data between client and server. The server administrator has to generate a private public key pair and certificate request. This certificate request has to be signed by a certificate authority which converts the certificate request to a certificate. The server administrator has to update the certificate and private key to the webserver. The certificate has details about the server (like domain name for which it serves, expiry date), public key of the server. The private key is a secret to the server and losing the private key loses the trust the server provides. When clients connect, the client sends a HELLO. The server sends its certificate to the client. The client checks the validity of the cert by seeing if it is within its expiry time, if it is signed by a trusted authority and the hostname in the cert is the same as the server. This validation makes sure the server is the right server and there is no phishing. Once that is validated, the client negotiates a symmetrical key and cipher with the server by encrypting the negotiation with the public key of the server. Nobody else other than the server who has the private key can understand this data. Once negotiation is complete, that symmetric key and algorithm is used for further encryption which can be decrypted only by client and server from thereon as they only know the symmetric key and algorithm. The switch to symmetric algorithm from asymmetric encryption algorithm is to not strain the resources of client devices as symmetric encryption is generally less resource intensive than asymmetric. 

```bash
#Try the following on your terminal to see the cert details like Subject Name(domain name), Issuer details, Expiry date
curl https://www.google.com -v 
```
```bash
*   Trying [2a00:1450:4009:820::2004]:443...
* Connected to www.google.com (2a00:1450:4009:820::2004) port 443 (#0)
* ALPN: offers h2,http/1.1
* (304) (OUT), TLS handshake, Client hello (1):
*  CAfile: /etc/ssl/cert.pem
*  CApath: none
* (304) (IN), TLS handshake, Server hello (2):
* (304) (IN), TLS handshake, Unknown (8):
* (304) (IN), TLS handshake, Certificate (11):
* (304) (IN), TLS handshake, CERT verify (15):
* (304) (IN), TLS handshake, Finished (20):
* (304) (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / AEAD-CHACHA20-POLY1305-SHA256
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=www.google.com
*  start date: Oct 23 11:24:57 2023 GMT
*  expire date: Jan 15 11:24:56 2024 GMT
*  subjectAltName: host "www.google.com" matched cert's "www.google.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1C3
*  SSL certificate verify ok.
* using HTTP/2
* h2 [:method: GET]
* h2 [:scheme: https]
* h2 [:authority: www.google.com]
* h2 [:path: /]
* h2 [user-agent: curl/8.1.2]
* h2 [accept: */*]
* Using Stream ID: 1 (easy handle 0x141812e00)
> GET / HTTP/2
> Host: www.google.com
> User-Agent: curl/8.1.2
> Accept: */*
>
< HTTP/2 200
< date: Mon, 04 Dec 2023 19:42:48 GMT
< expires: -1
< cache-control: private, max-age=0
< content-type: text/html; charset=ISO-8859-1
< content-security-policy-report-only: object-src 'none';base-uri 'self';script-src 'nonce-_C5r_wmr6-1XyYckXKee2A' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
< p3p: CP="This is not a P3P policy! See g.co/p3phelp for more info."
< server: gws
< x-xss-protection: 0
< x-frame-options: SAMEORIGIN
< set-cookie: SOCS=CAAaBgiArbSrBg; expires=Thu, 02-Jan-2025 19:42:48 GMT; path=/; domain=.google.com; Secure; SameSite=lax
< set-cookie: AEC=Ackid1RiFR-Q29PANCR-68dY5VmhSq-zMoXpMnL-oZtSAvcXXhfTlSCd2lk; expires=Sat, 01-Jun-2024 19:42:48 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax
< set-cookie: __Secure-ENID=16.SE=AMen4HvAgOZLjmCBwEqVt59PxlCr5qh_7lodjFuSo67JBEjjIff9YK9rvet25lsW-E_Vh-ZJurnQQYpzrkBQHCM31JAiZNEp6cILxzPo1u8WmODpg2THMMMjFxBzhLTdih7zgUQbGlg_xZxIwK6S0ypWsQxFnTGsVShkcCoRD58; expires=Fri, 03-Jan-2025 12:01:06 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax
< set-cookie: CONSENT=PENDING+497; expires=Wed, 03-Dec-2025 19:42:48 GMT; path=/; domain=.google.com; Secure
< alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
< accept-ranges: none
< vary: Accept-Encoding
```

Here my system has a list of certificate authorities it trusts in this file  /etc/ssl/cert.pem. Curl validates the certificate is for www.google.com by seeing the CN section of the subject part of the certificate. It also makes sure the certificate is not expired by seeing the expire date. It also validates the signature on the certificate by using the public key of issuer Digicert in  /etc/ssl/cert.pem. Once this is done, using the public key of www.google.com it negotiates cipher TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 with a symmetric key. Subsequent data transfer including first HTTP request uses the same cipher and symmetric key.


