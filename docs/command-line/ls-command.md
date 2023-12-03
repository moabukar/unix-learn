# ls (list directories)

Now that we know how to move around the system, how do we figure out what is available to us? Right now it’s like we are moving around in the dark. Well, we can use the wonderful ls command to list directory contents. The ls command will list directories and files in the current directory by default, however you can specify which path you want to list the directories of.

<pre>$ ls
$ ls /home/mo</pre>

ls is a quite useful tool, it also shows you detailed information about the files and directories you are looking at.

Also note that not all files in a directory will be visible. Filenames that start with . are hidden, you can view them however with the ls command and pass the -a flag to it (a for all). 

<pre>$ ls -a</pre>

There is also one more useful ls flag, -l for long, this shows a detailed list of files in a long format. This will show you detailed information, starting from the left: file permissions, number of links, owner name, owner group, file size, timestamp of last modification, and file/directory name. 

<pre>$ ls -l</pre>

<pre>mo:~$ ls -l
total 19592
drwx------@   8 mohameda  staff      256  1 Jun  2023 Applications
-rw-r--r--    1 mohameda  staff     1093 14 Sep  2022 Brewfile
-rw-r--r--@   1 mohameda  staff     7015  6 Jul 16:35 CHANGELOG.md
drwx------@   8 mohameda  staff      256 28 Nov 00:38 Desktop
drwx------@  60 mohameda  staff     1920 27 Nov 18:15 Documents
drwx------@ 342 mohameda  staff    10944  3 Dec 19:45 Downloads
-rw-r--r--    1 mohameda  staff        0 27 Nov 20:19 JO.txt
-rw-r--r--    1 mohameda  staff        0 27 Nov 20:19 L.txt
-rw-r--r--    1 mohameda  staff     1084  6 Oct  2021 LICENSE
drwx------@  94 mohameda  staff     3008 28 Nov 00:16 Library
drwx------    8 mohameda  staff      256 28 Nov 00:23 Movies
drwx------+   5 mohameda  staff      160 28 Nov 00:23 Music

Commands have things called flags (or arguments or options, whatever you want to call it) to add more functionality. See how we added -a and -l, well you can add them both together with -la. The order of the flags determines which order it goes in, most of the time this doesn’t really matter so you can also do ls -al and it would still work.

<pre>$ ls -la</pre>

## Exercise

Run ls with different flags and see the output you receive.

## Quiz Questions 

Click the right arrow to view the answers

<details>
<summary>What command would you use to see hidden files?</summary>
ls -a
</details>
