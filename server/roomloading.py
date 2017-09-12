from room import Room

def load_start():
    room = Room()
    room.name = "Class Room"
    room.desc = "We are in a classroom. There are some other people here but they are concentrating hard on the dojo and don't look too talkative. There is a strange goon standing at the front talking. You are thirsty and need a beer, but you'll need to find the fridge with the beer in first."
    room.pickups = []
    room.exits = ['South']
    room.exit_ref = [1]

    return room

def load_south():
    room = Room()
    room.name = "Hallway"
    room.desc = "It's a hallway, it stretches off into the distance. You can hear the faint sound of people typing."
    room.pickups = ["key"]
    room.verbs = ["pickup"]
    room.exits = ['North', "West"]
    room.exit_ref = [0,2]

    return room

def load_west():
    room = Room()
    room.name = "Main Room"
    room.desc = "You find yourself in a big room. There is a fridge here but it looks locked. You'll need a key to open it"
    room.pickups = []
    room.verbs = ["use"]
    room.exits = ["East"]
    room.exit_ref = [1]
    return room