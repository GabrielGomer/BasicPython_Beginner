# First Class Example
class TopSongs(object):

    def __init__(self, name):
        self.name = name

    def artist(self):
        for line in self.name:
            print(line)


print("Hip Hop and Electronic Artist's: ")
hip_hop = TopSongs(["Future",
                    "Migos",
                    "Kanye West"])
electronic = TopSongs(["Marshmellow",
                       "Def Jam"])

hip_hop.artist()
electronic.artist()