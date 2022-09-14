bus_stops = [[10,0],[3,5],[5,8]]


def number(bus_stops):
    pplinto = 0
    for stop in bus_stops:
        pplinto += stop[0] - stop[1]
    
    return pplinto


def number1(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


print(number(bus_stops))
