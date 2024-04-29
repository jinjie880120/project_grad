import math
#start_longitude = 120.288289
#start_latitude = 22.733552
#theta=180
#R=200
#print GPSP(120.288289,22.733552,180,200)
def GPSP(start_point,theta,R):
    start_longitude=start_point[0]
    start_latitude=start_point[1]
    dx = R*math.cos(math.radians(theta))
    dy = R*math.sin(math.radians(theta))
    delta_longitude = dx/(111320*math.cos(start_latitude))
    delta_latitude = dy/110540
    Final_longitude = start_longitude + delta_longitude
    Final_latitude = start_latitude + delta_latitude
    return "%f,%f" %(Final_latitude,Final_longitude)
#print GPSP((120.288289,22.733552),180,200)
