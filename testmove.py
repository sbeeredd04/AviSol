import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def create_drone_path(start, end, num_frames):
    # Calculate distance
    d = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)

    # Generate path
    t = np.linspace(0, 1, num_frames)
    x = np.concatenate([np.full(num_frames//3, start[0]), np.linspace(start[0], end[0], num_frames//3), np.full(num_frames//3, end[0])])
    y = np.concatenate([np.full(num_frames//3, start[1]), np.linspace(start[1], end[1], num_frames//3), np.full(num_frames//3, end[1])])
    
    # z-values start from 0, increase to d/2, stay at d/2, and then decrease back to 0
    z_up = np.linspace(0, d/2, num_frames//3)
    z_flat = np.full(num_frames//3, d/2)
    z_down = np.linspace(d/2, 0, num_frames//3)
    z = np.concatenate([z_up, z_flat, z_down])

    return x, y, z, t
# Take 4 x,y values as inputs for two curves start and end point
start1 = [float(input("Enter x1 for curve 1: ")), float(input("Enter y1 for curve 1: "))]
end1 = [float(input("Enter x2 for curve 1: ")), float(input("Enter y2 for curve 1: "))]
start2 = [float(input("Enter x1 for curve 2: ")), float(input("Enter y1 for curve 2: "))]
end2 = [float(input("Enter x2 for curve 2: ")), float(input("Enter y2 for curve 2: "))]

# Calculate the number of frames for each curve based on its length
frames1 = int(100 * np.sqrt((end1[0] - start1[0]) ** 2 + (end1[1] - start1[1]) ** 2))
frames2 = int(100 * np.sqrt((end2[0] - start2[0]) ** 2 + (end2[1] - start2[1]) ** 2))

# Generate semi-circular curves with different number of frames
x1, y1, z1, t1 = create_drone_path(start1, end1, frames1)
x2, y2, z2, t2 = create_drone_path(start2, end2, frames2)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot curves
ax.plot(x1, y1, z1, label='Curve 1')
ax.plot(x2, y2, z2, label='Curve 2')

# Initialize points
point1, = ax.plot([x1[0]], [y1[0]], [z1[0]], 'go', markersize=20)
point2, = ax.plot([x2[0]], [y2[0]], [z2[0]], 'ro', markersize=20)

# Update function for animation
def update(i):
    if i < len(t1):
        point1.set_data(x1[i], y1[i])
        point1.set_3d_properties(z1[i])
    if i < len(t2):
        point2.set_data(x2[i], y2[i])
        point2.set_3d_properties(z2[i])
    return point1, point2,
# Create animation with the maximum number of frames
ani = FuncAnimation(fig, update, frames=max(frames1, frames2), interval=100/15, blit=True)

plt.show() 