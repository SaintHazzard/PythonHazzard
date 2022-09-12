class_points = [2,3]
your_points = 5

def better_than_average(class_points, your_points):
    class_points.append(your_points)
    total_points = sum(class_points) / len(class_points)
    # '''evaluo mi nota con respecto al promedio del grupo''' 
    return your_points > total_points



print(better_than_average(class_points, your_points))
    