D = input()

if D == "N":
    D = "S"
elif D == "S":
    D = "N"
elif D == "W":
    D = "E"
elif D == "E":
    D = "W"
elif D == "NE":
    D = "SW"
elif D == "NW":
    D = "SE"
elif D == "SE":
    D = "NW"
elif D == "SW":
    D = "NE"

print(D)
