class Board(object):

    #Dictionary containing adjacencies
    ADJACENCY = {"a1": ["d1", "a4"],
        "d1": ["a1", "d2", "g1"], "g1": ["d1", "g4"], "b2": ["b4", "d2"],
        "d2": ["b2", "d1", "d3", "f2"], "f2": ["d2", "f4"],
        "c3": ["c4", "d3"], "d3": ["c3", "d2", "e3"], "e3": ["d3", "e4"],
        "a4": ["a1", "a7", "b4"], "b4": ["a4", "b2", "b6", "c4"],
        "c4": ["b4", "c3", "c5"], "e4": ["e3", "e5", "f4"],
        "f4": ["e4", "f2", "f6", "g4"], "g4": ["f4", "g1", "g7"],
        "c5": ["c4", "d5"], "d5": ["c5", "d6", "e5"], "e5": ["d5", "e4"],
        "b6": ["b4", "d6"], "d6": ["b6", "d5", "d7", "f6"],
        "f6": ["d6", "f4"], "a7": ["a4", "d7"], "d7": ["a7", "d6", "g7"],
        "g7": ["d7", "g4"]}
    
    #List of mills
    MILLS = [["a1", "d1", "g1"], ["b2", "d2", "f2"],
        ["c3", "d3", "e3"], ["a4", "b4", "c4"], ["e4", "f4", "g4"],
        ["c5", "d5", "e5"], ["b6", "d6", "f6"], ["a7", "d7", "g7"],
        ["a1", "a4", "a7"], ["b2", "b4", "b6"], ["c3", "c4", "c5"],
        ["d1", "d2", "d3"], ["d5", "d6", "d7"], ["e3", "e4", "e5"],
        ["f2", "f4", "f6"], ["g1", "g4", "g7"]]
        
    def __init__(self):
        #Initializes points to be spaces
        self.points = {"a1": " ", "d1": " ", "g1": " ",
        "b2": " ", "d2": " ", "f2": " ", "c3": " ", "d3": " ",
        "e3": " ", "a4": " ", "b4": " ", "c4": " ", "e4": " ",
        "f4": " ", "g4": " ", "c5": " ", "d5": " ", "e5": " ",
        "b6": " ", "d6": " ", "f6": " ", "a7": " ", "d7": " ",
        "g7": " "}
        
    def assign_piece(self,player,destination):
        # assigns a player to a point
        self.points[destination] = player
        
    def clear_place(self,destination):
        # clears a point place, effectively removing a player
        self.points[destination] = " "

    def __str__(self):
        """
        Display everything nice and pretty-like.
        This is an ugly function.
        """
        s = "\n"
        s+= "    7 [" + self.points["a7"] + "]------[" + self.points["d7"] + \
              "]------[" + self.points["g7"] + "] \n"
        s+= "    6  | [" + self.points["b6"] + "]---[" + self.points["d6"] + \
              "]---[" + self.points["f6"] + "] |\n"
        s+= "    5  |  | [" + self.points["c5"] + "][" + self.points["d5"] + \
              "][" + self.points["e5"] + "] |  |\n"
        s+= "    4 [" + self.points["a4"] + "][" + self.points["b4"] + "][" + \
              self.points["c4"] + "]   [" + self.points["e4"] + "][" + \
              self.points["f4"] + "][" + self.points["g4"] + "]\n"
        s+= "    3  |  | [" + self.points["c3"] + "][" + self.points["d3"] + \
              "][" + self.points["e3"] + "] |  |\n"
        s+= "    2  | [" + self.points["b2"] + "]---[" + self.points["d2"] +\
              "]---[" + self.points["f2"] + "] |\n"
        s+= "    1 [" + self.points["a1"] + "]------[" + self.points["d1"] + \
              "]------[" + self.points["g1"] + "]\n"
        s+= "       a  b  c  d  e  f  g\n"
        s+= "\n"
        return (s)
    
    
    
