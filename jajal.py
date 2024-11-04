import numpy as np
import matplotlib.pyplot as plt
import copy

from algorithm.HillClimbingSearchSteepestAscent import *

random_cube = HillClimbingSearchSteepestAscent(5)


initial_cube_data = np.arange(1, 126).reshape((5, 5, 5))
final_cube_data = np.arange(125, 0, -1).reshape((5, 5, 5))

# # Generate two 5x5x5 arrays with numbers from 1 to 125
# initial_cube_data = copy.deepcopy(random_cube.cube.data)

# random_cube.solve()


# final_cube_data = random_cube.cube.data  # Example for final configuration, reversed order

cube_size = 3

fig = plt.figure(figsize=(12, 6))

def plot_number_cube(ax, cube_data, title):
    for i in range(5):
        for j in range(5):
            for k in range(5):
                ax.text(i * cube_size + cube_size / 2, 
                        j * cube_size + cube_size / 2, 
                        k * cube_size + cube_size / 2,
                        str(cube_data[i, j, k]), 
                        color='black', fontsize=8, ha='center', va='center', alpha=1.0)
    
    ax.set_xlim([0, 5 * cube_size])
    ax.set_ylim([0, 5 * cube_size])
    ax.set_zlim([0, 5 * cube_size])

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title(title)

ax1 = fig.add_subplot(121, projection='3d')
plot_number_cube(ax1, initial_cube_data, "Initial Configuration")

ax2 = fig.add_subplot(122, projection='3d')
plot_number_cube(ax2, final_cube_data, "Final Configuration")

ax1.view_init(elev=30, azim=30)
ax2.view_init(elev=30, azim=30)

plt.tight_layout()
plt.show()
