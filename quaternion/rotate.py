import numpy as np
import quaternion

def new_position(pos, quat):
    #pos' = q*q^-1*pos
    quat_inverse = quat.inverse()
    
    new_pos = quat*pos*quat_inverse
    return new_pos


def rotate_point(rotation_angle, point):
    pos = np.quaternion(point[0], point[1], point[2], point[3])
    q = np.quaternion(np.cos(rotation_angle/2), 0, 0, np.sin(rotation_angle/2))

    rotated_point = new_position(pos, q)
    return rotated_point


point = [0.0, 0.3, 0.5, 0.1]
print(rotate_point(np.pi/2, point))
