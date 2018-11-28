# The Idea

At some point, when your friends learn you are studying cybersecurity theu innevitably ask "Can you hack my computer?" to which the answer is "Sure, give me a couple of weeks". So our goal is to infect their computers ahead of time so when they ask that question you can say "Sure give me a few minutes" and look cool AF.

How do we accomplish this?

1. Create a bot that can check for commands, execute the commands, and return the result, all without making our friends' machines vulnerable to real bad guys.
2. Create a command and control (C&C) server to manage the bots, send them commands, and recieve the results of the commands. This is what we use to look cool when we "hack" them.
3. Get physical access to their computer. Install a script on the computer that installs a bot. Yeah, we're not good enough at this hacking business to do it all without physical access.  
4. Seem like a genius hacker.

You should note, this does not need to be nearly as complicated as a real botnet. We don't need P2P connections, persistance hidden from anti-viruses, the ability to spread to other machines, or the ability to exfiltrate additional information. Of course, it would be a fantastic learning opportunity of we developed our bot application to be well hidden and persistant.

# Useful Readings

(What is a botnet)[https://encyclopedia.kaspersky.com/glossary/botnet/].
(Here is an open source simple botnet)[https://github.com/TreeHacks/botnet-hackpack].
(The Mirai Botnet source code)[https://github.com/jgamblin/Mirai-Source-Code].
(What the Mirai BotNet is if you'd forgotten . . .)[https://krebsonsecurity.com/tag/mirai-botnet/]