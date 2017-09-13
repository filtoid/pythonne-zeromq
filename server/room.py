class Room(object):

    def __init__(self):
        self.name = "Room Name Has Not Been Replaced"
        self.desc = "Room Description Has Not Been Replaced"
        self.pickups = []
        self.verbs = []
        self.exits = []
        self.exit_ref = []

    def is_verb_allowed(self, verb):
        if verb in self.verbs:
            return True 
        return False

    def enact_verb(self, verb, content, user_objs):
        cont = ""
        for c in content:
            cont += " " + c
        cont = cont.strip()

        if verb == "pickup":
            if cont in self.pickups:
                new_pickups = []
                ret = "Cannot pick up that object"
                for p in self.pickups:
                    if p == cont:
                        ret = cont
                    else:
                        new_pickups.append(p)
                self.pickups = new_pickups
                return ret
            else:
                return "Cannot pickup the {}".format(cont)
        elif verb in self.verbs and verb == "use" and cont=="key with fridge" and "key" in user_objs:
            return "Congratulations you have won the game, you managed to get another beer from the locked fridge."
        else:
            return "Unable to process command {}".format(verb)

    def get_exits(self):
        if len(self.exits)==0:
            return "There are no exits"
        elif len(self.exits)==1:
            return "The only exit is to the {}".format(self.exits[0])
        else:
            ret = "There are exits to the "
            for ind, val in enumerate(self.exits):
                if ind != len(self.exits)-1:
                    ret += val
                else:
                    ret += " and {}".format(val)
            return ret

    def process_move(self, dir):
        if dir in self.exits:
            print(self.exit_ref)
            for ind,val in enumerate(self.exits):
                if dir == val:
                    return self.exit_ref[ind]
        else: 
            return None
            
    def get_objects(self):
        if len(self.pickups)==0:
            return "There is nothing here of interest."
        elif len(self.pickups)==1:
            return "There is a {} on the floor".format(self.pickups[0])
        else:
            ret = "The following objects are here: "
            for p in self.pickups:
                ret += p
               
            return ret
