import sys;

def ArrayFileRead(link):
    with open(link, 'r') as file:
        lst = file.readlines()
    lst = [[float(n) for n in x.split()] for x in lst]
    return lst

def IsPointInCircle(x, y, xc, yc, r):
    math = (x - xc) ** 2 + (y - yc) ** 2
    if math < r * r:
        return (1)
    elif math == r * r: 
        return (0)
    else:
       return(2)
     
def PointRelativeToCircle(files):
    circle_parameters_input, point_options_input = map(str, files[1:3])
    circle_parameters = ArrayFileRead(circle_parameters_input)
    point_options =  ArrayFileRead(point_options_input)
    for i in range(len(point_options)):
        print(IsPointInCircle(x = point_options[i][0], y = point_options[i][1] , xc = circle_parameters[0][0], yc = circle_parameters[0][1], r = circle_parameters[1][0]))
    
    


if __name__ == "__main__":
    PointRelativeToCircle(sys.argv)