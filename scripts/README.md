# Scripts

## (PowerShellInstaller)[PowerShellInstaller]

Installs the Client on the host machine such that it is hard to uninstall and will periodically run.

## (USBInstaller)[USBInstaller.txt]

A Ducky script that is then loaded onto a (MalDuino Lite)[https://malduino.com/wiki/doku.php?id=start] for physical installation. It downloads the PowerShellInstaller script and then runs it in a hidden Powershell window with administrator permissions. Required administrator access for the script to work.