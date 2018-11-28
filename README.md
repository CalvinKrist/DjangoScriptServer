# The Idea

At some point, when your friends learn you are studying cybersecurity they inevitably ask "Can you hack my computer?" to which the answer is "Sure, give me a couple of weeks". So our goal is to infect their computers ahead of time so when they ask that question you can say "Sure give me a few minutes" and look cool AF.

How do we accomplish this?

1. Create a bot that can check for commands, execute the commands, and return the result, all without making our friends' machines vulnerable to real bad guys.
2. Create a command and control (C&C) server to manage the bots, send them commands, and recieve the results of the commands. This is what we use to look cool when we "hack" them.
3. Get physical access to their computer. Install a script on the computer that installs a bot. Yeah, we're not good enough at this hacking business to do it all without physical access.  
4. Seem like a genius hacker.

You should note, this does not need to be nearly as complicated as a real botnet. We don't need P2P connections, persistance hidden from anti-viruses, the ability to spread to other machines, or the ability to exfiltrate additional information. Of course, it would be a fantastic learning opportunity of we developed our bot application to be well hidden and persistent.

# Useful Readings

## Botnets
(What is a botnet)[https://encyclopedia.kaspersky.com/glossary/botnet/].
(Here is an open source simple botnet)[https://github.com/TreeHacks/botnet-hackpack].
(The Mirai Botnet source code)[https://github.com/jgamblin/Mirai-Source-Code].
(What the Mirai BotNet is if you'd forgotten . . .)[https://krebsonsecurity.com/tag/mirai-botnet/]

## Persistance Methods
Persistence is the ability of malware to stay on your machine even when restarted or when its process is turned off. It can also be used to describe its ability to hide from detection.

(Great overview of Windows persistance. It's rather technical and gives concrete examples.)[http://www.fuzzysecurity.com/tutorials/19.html]

## Advanced Stuff
(Running malware in memory only)[https://www.cyberscoop.com/kaspersky-fileless-malware-memory-attribution-detection/]
(Fileless malware tutorial)[https://www.varonis.com/blog/understanding-malware-free-hacking-part/]
(Summary of malware obfuscation techniques)[https://www.profsandhu.com/cs5323_s18/yk_2010.pdf]

## PowerShell
(PowerShell basics)[https://docs.microsoft.com/en-us/previous-versions/system-center/developer/dn529004(v=cmsdk.12)]
(A stealthy persistance mechanism using PowerShell and WMI)[https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html]

## CPP
(A library for interacting with REST APIs in CPP)[https://github.com/Microsoft/cpprestsdk]
(A library for pasring JSON I've used. It has issues but works.)[https://github.com/open-source-parsers/jsoncpp/wiki]
