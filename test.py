import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_line():
    """Get a line from user input."""
    start = input("Enter the start point (x, y, z) of the line: ")
    end = input("Enter the end point (x, y, z) of the line: ")
    x = [float(start.split(",")[0]), float(end.split(",")[0])]
    y = [float(start.split(",")[1]), float(end.split(",")[1])]
    z = [float(start.split(",")[2]), float(end.split(",")[2])]
    return x, y, z

def plot_lines(line1, line2, intersect=False):
    """Plot two lines in 3D."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(line1[0], line1[1], line1[2], marker='o', label='Line 1')
    ax.plot(line2[0], line2[1], line2[2], marker='o', label='Line 2')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('User Input Lines')
    ax.legend()
    if intersect:
        ax.text(0.5, 0.5, 0.5, 'Change of elevation needed', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color='red', fontsize=14)
    plt.show()

def on_segment(p, q, r):
    """Given three colinear points p, q, r, the function checks if point q lies on line segment 'pr'"""
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False

def orientation(p, q, r):
    """To find orientation of ordered triplet (p, q, r).
    The function returns following values
    0 --> p, q and r are colinear
    1 --> Clockwise
    2 --> Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # colinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counter clockwise

def do_intersect(p1, q1, p2, q2):
    """Main function to check whether two given line segments intersect"""
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if ((o1 != o2 and o3 != o4) or (o1 == 0 and on_segment(p1, p2, q1)) or
        (o2 == 0 and on_segment(p1, q2, q1)) or (o3 == 0 and on_segment(p2, p1, q2)) or
        (o4 == 0 and on_segment(p2, q1, q2))):
        return True
    return False

# Get two lines from user input
line1 = get_line()
line2 = get_line()

# Check for intersection
intersect = do_intersect((line1[0][0], line1[1][0]), (line1[0][1], line1[1][1]), (line2[0][0], line2[1][0]), (line2[0][1], line2[1][1]))

# Plot the lines
plot_lines(line1, line2, intersect)

if intersect:
    print("Lines intersect.")
else:
    print("Lines do not intersect.")