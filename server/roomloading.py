from room import Room

def load_start():
    room = Room()
    room.name = "Class Room"
    room.desc = "We are in a classroom. There are some other people here but they are concentrating hard on the dojo and don't look too talkative. There is a strange goon standing at the front talking. You are thirsty and need a beer, but you'll need to find the fridge with the beer in first."
    room.pickups = []
    room.exits = ['South']
    room.exit_ref = [1]
    room.auto_responses = {
        "talk to goon": "He ignores you. One of the other drones turns around and says 'ssh'",
        "get beer": "Ha Ha nice try, you'll need to get one yourself"
    }
    return room

def load_south():
    room = Room()
    room.name = "Hallway"
    room.desc = "It's a hallway, it stretches off into the distance. You can hear the faint sound of people typing."
    room.pickups = ["key"]
    room.verbs = ["pickup", "get"]
    room.exits = ['North', "West"]
    room.exit_ref = [0,2]

    room.auto_responses = {
        "pick up key": "try using pickup as a single word",
        "look at key": "It's a key, what do you want, a picture?"
    }

    return room

def load_west():
    room = Room()
    room.name = "Main Room"
    room.desc = "You find yourself in a big room. There is a fridge here but it looks locked. You'll need a key to open it"
    room.pickups = []
    room.verbs = ["use"]
    room.exits = ["East"]
    room.exit_ref = [1]

    room.auto_responses = {
        "open fridge": "It's locked - perhaps you have a key, if not maybe try and find one",
        "smash fridge": "As easy as it would be for me to just let you smash the place up that's hardly a nice way to go about things",
        "look at fridge": "It's a fridge, there is beer inside. It is locked though so currently 'no beer for you'"
    }

    return room