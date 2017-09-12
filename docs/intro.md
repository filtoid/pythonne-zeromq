#Getting Started
The following commands can be sent to the server from the client

Single word commands
details    -> This returns details about the server, version and port number etc
examine    -> Return the details of the current room (ie. the description)

Commands with extra content
enact_verb -> Process the verb and object if we can, pass verb and object
    example: enact_verb pickup spade
move       -> Move rooms, if we can, provide direction (compass direction)
