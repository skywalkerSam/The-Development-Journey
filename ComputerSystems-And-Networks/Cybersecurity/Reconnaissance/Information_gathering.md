
# Information Gathering & Reconnaissance;
    >_ It's the first step of hacking.
    >_ Collecting Information about the target, Active or Passive..
    >_ 



# Obtaining IP Addresses;
    >_ ping google.com   ; IP address of the target

    >_ nslookup facebook.com   \  ping facebook.com

    >_ https://ipinfo.info/html/ip_checker.php   ; A website which gives Information about the target

    >_ whois facebook.com   ; More Information about the target, Physical address included

    >_



# Whatweb Stealthy Scan;
    >_ whatweb   ; Initial command with some help

    >_ whatweb -h   ; Get help with whatweb tool

    >_ whatweb facebook.com \  whatweb facebook.com -v   ; Normal scan, can be done on any website, prefer verbose command

    >_ 



# Aggressive Website Technology Discovering on IP Range;
    >_ Permission required

    >_ ifconfig   ; Range of IP address

    >_ whatweb 192.168.43.1-192.168.43.255 --aggression 3 -v   ; Attack with aggression level 3

    >_ whatweb 192.168.43.1-192.168.43.255 -a 3 -v --no-errors   ; Attack with aggression level 3 with verbose with no-errors 

    >_ whatweb -h   ; Get help with more commands

    >_ whatweb 192.168.43.1-192.168.43.255 -a 3 -v --no-errors --log-verbose=whatweb1scan   ; Attack with aggression level 3 with verbose with no-errors & save the logs into desired file

    >_ 



# Getting Emails/Usernames with theHarvester and hunter.io;
    >_ theHarvester   ; Initial command with some help

    >_ theHarvester -h   ; Help with theHarvester tool

    >_ theHarvester -d facebook.com -b all/twitter/github/etc   ; Search for domain facebook.com from source (all plateforms or google.com or linkedin.com)  

    >_ hunter.io   ; A Website, to get email addresses from its domain name

    >_ 



# How to download tools online;
    >_ git clone https://github.com/sherlock-project/sherlock / URL   ; clone any program/software from github repository in to desired folder of your PC

    >_ 



# Finding Usernames With Sherlock;
    >_ python3 sherlock.py murlidhar1319   ; Search this username on web

    >_ python3 sherlock.py -h    ; Get help with sherlock tool

    >_ 



# Bonus - Email Scraper Tool In Python3;
        >_ just an email extractor tool






