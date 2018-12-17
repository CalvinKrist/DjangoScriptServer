# Progress

## Scripts

### [PowerShellInstaller](scripts/PowerShellInstaller.ps1)

Installs the Client on the host machine such that it is hard to uninstall and will periodically run.

### [USBInstaller](scripts/USBInstaller.txt)

A Ducky script that is then loaded onto a (MalDuino Lite)[https://malduino.com/wiki/doku.php?id=start] for physical installation. It downloads the PowerShellInstaller script and then runs it in a hidden Powershell window with administrator permissions. Required administrator access for the script to work.

# Useful Readings

## Botnets
[What is a botnet](https://encyclopedia.kaspersky.com/glossary/botnet/).
[Here is an open source simple botnet](https://github.com/TreeHacks/botnet-hackpack).
[The Mirai Botnet source code](https://github.com/jgamblin/Mirai-Source-Code).
[What the Mirai BotNet is if you'd forgotten . . .](https://krebsonsecurity.com/tag/mirai-botnet/)

## Persistance Methods
Persistence is the ability of malware to stay on your machine even when restarted or when its process is turned off. It can also be used to describe its ability to hide from detection.

[Great overview of Windows persistance. It's rather technical and gives concrete examples.](http://www.fuzzysecurity.com/tutorials/19.html)

## Advanced Stuff
[Running malware in memory only](https://www.cyberscoop.com/kaspersky-fileless-malware-memory-attribution-detection/)
[Fileless malware tutorial](https://www.varonis.com/blog/understanding-malware-free-hacking-part/)
[Summary of malware obfuscation techniques](https://www.profsandhu.com/cs5323_s18/yk_2010.pdf)

## PowerShell
[PowerShell basics](https://docs.microsoft.com/en-us/previous-versions/system-center/developer/dn529004(v=cmsdk.12))
[A stealthy persistance mechanism using PowerShell and WMI](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)
[More hands-one examples of using WMI for persistence.](https://www.blackhat.com/docs/us-15/materials/us-15-Graeber-Abusing-Windows-Management-Instrumentation-WMI-To-Build-A-Persistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf)

## CPP
[A library for interacting with REST APIs in CPP](https://github.com/Microsoft/cpprestsdk)
[A library for pasring JSON I've used. It has issues but works.](https://github.com/open-source-parsers/jsoncpp/wiki)
