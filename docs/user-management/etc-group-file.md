# /etc/group

Another file that is used in user management is the /etc/group file. This file allows for different groups with different permissions. 

<pre>$ cat /etc/group

root:*:0:pete
</pre>

Very similar to the /etc/password field, the /etc/group fields are as follows:

<ol>
<li>Group name</li>
<li>Group password - there isn't a need to set a group password, using an elevated privilege like sudo is standard. A "*" will be put in place as the default value.</li>
<li>Group ID (GID)</li>
<li>List of users - you can manually specify users you want in a specific group</li>
</ol>

## Exercise

Run the command <b>groups</b>. What do you see?

## Quiz Questions 

Click the right arrow to view the answers

<details>
<summary>What is the GID of root?</summary>
0
</details>
