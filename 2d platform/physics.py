from math import *

"""*********************************************************************"""
""" RAYCASTING """

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def onSegment(p, q, r):
    if q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]):
        if q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]):
            return True
    return False

def doIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and onSegment(p1, p2, q1):
        return True
    if o2 == 0 and onSegment(p1, q2, q1):
        return True
    if o3 == 0 and onSegment(p2, p1, q2):
        return True
    if o4 == 0 and onSegment(p2, q1, q2):
        return True

    return False


def Raycast(start_pos, dir, magnitude, layer):
    ownLine = (start_pos, start_pos+dir)

    hit = False

    for line in layer:
        if doIntersect(ownLine[0], ownLine[1], line[0], line[1]):
            hit = True

"""*********************************************************************"""
