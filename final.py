class Node:
    def __init__(self, question):
        self.question = question
        self.edges = []

class Edge:
    def __init__(self, to, answer):
        self.to = to
        self.answer = answer

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes


print("Welcome to the vacation picker \n ")

start = Node("Would you prefer to travel internationally or within the United States?")
International = Node("International")
UnitedStates = Node("United States")


edge_ITN = Edge(International, "International")
edge_US = Edge(UnitedStates, "United States")

start.edges += [edge_ITN]
start.edges += [edge_US]
print (start.edges)
q2 = Node("Are you planning an adult only trip or a family friendly trip?")
adult = Node("Adult Only")
child = Node("Family Friendly")

edge_adult = Edge(adult, "Adult Only")
edge_child = Edge(child, "Family Friendly")

q2.edges += [edge_adult]
q2.edges += [edge_child]

q3 = Node("When are you planning on going on this trip Spring/Summer or Fall/Winter")
spring = Node("Spring/Summer")
fall = Node("Fall/Winter")

edge_spring = Edge(spring, "Spring/Summer")
edge_fall = Edge(fall, "Fall/Winter")

q3.edges += [edge_spring]
q3.edges += [edge_fall]

q4 = Node("Do you prefer warmer or colder weather?")
warm = Node("Warmer")
cold = Node("Colder")

edge_warm = Edge(warm, "Warmer")
edge_cold = Edge(cold, "Colder")

q4.edges += [edge_warm]
q4.edges += [edge_cold]

q5 = Node("Would you rather stay in an all inclusive resort or stay in a local hotel?")
resort = Node("All inclusive resort")
hotel = Node("Local Hotel")

edge_resort = Edge(resort, "resort")
edge_hotel = Edge(hotel, "Hotel")

q5.edges += [edge_resort]
q5.edges += [edge_hotel]

q6 = Node("Do you prefer staying in the mountains or on a beach?")
mountain = Node("Mountains")
beach = Node("Beach")

edge_ITN = Edge(International, "International")
edge_US = Edge(UnitedStates, "United States")

start.edges += [edge_ITN]
start.edges += [edge_US]

q7 = Node("Do you prefer a big tourist city or a smaller less known location ")
city = Node("Large tourist City")
local = Node("Smaller local area")

edge_city = Edge(city, "Large Tourist City")
edge_local = Edge(local, "Smaller local area")

start.edges += [edge_city]
start.edges += [edge_local]

q8 = Node("Do you prefer staying in the mountains or on a beach?")
mountain = Node("Mountains")
beach = Node("The Beach")

edge_mountain = Edge(mountain,"Mountains")
edge_beach = Edge(beach, "Beach")

q8.edges += [edge_mountain]
q8.edges += [edge_beach]

q9 = Node("Do you prefer outdoor activities like hiking and exploring or visiting indoor attractions?")
outdoor = Node("Outdoor")
indoor = Node("Indoor")

edge_outdoor = Edge(outdoor, "Outdoor")
edge_indoor = Edge(indoor, "Indoor")

q9.edges += [edge_outdoor]
q9.edges += [edge_indoor]




# Locations
# ITN -> ADULT -> Spring -> colder -> smaller local -> mountains -> outdoor
# Lofoten Norway final result

