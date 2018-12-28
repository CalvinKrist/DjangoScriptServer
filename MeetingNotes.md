# Goals:
Client: 
* receive commands to run, return result of commands
* persistent on computer
* patching mechanism
		
Server:
* manage clients
* send commands to run
* store and display command results
* NOT MAKE CLIENT MACHINES VULNERABLE
* encrypt commands and command results
* secure login to C&C server
		
## Stretch Goals:
* becoming a rootkit
* being a fileless application
* having reverse shells
* streaming their screen
	
	
# Design:
Protocls:
* REST API
* Initial connection supported with TokenAuthentication
	
Server:
* Django Python server
* Public facing website, C&C in the background
			
Rest API:

	/rest/clients
		-GET enumerates all clients by name. No other information is given.
	
	/rest/client
		-PUT creates a client. Requires MAC address and public key.
		-GET gets command list for a user. Requires MAC address and public key.
		-POST updates command results for a user. Requires MAC address and public key.
		
	/rest/versions 
		-GET enumerates all versions
		
	/rest/versions/latest 
		-GET returns the code of the latest version
		
	/rest/publickey
		-GET returns public RSA key
		
DAVID STUFF TO DO:	

CPP application that launches, uses TokenAuthentication with server, checks to see if there's commands to be run, runs commands, returns command results, close
* find MAC address
* do asymetric encryption
* run system commands and get results even if they crash
* do REST requetss in CPP
* store commands to disk so they can be sent to server if server unavailable