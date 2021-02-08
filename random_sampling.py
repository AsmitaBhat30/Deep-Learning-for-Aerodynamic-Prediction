import numpy as np
import matplotlib.pyplot as pl

N = 100
xmax = 1.
v_sigma = 2.5 / 2. # 95% of the samples contained within 0, 5
v_mean  = 2.5      # mean at 2.5

N_sub = 10
v_sub_index = np.random.randint(0, N, N_sub)

particle_position = np.random.rand (N) * xmax
particle_velocity = np.random.randn(N)

particle_position_sub   = np.array(particle_position[v_sub_index])
particle_velocity_sub   = np.array(particle_velocity[v_sub_index])
particle_position_nosub = np.delete(particle_position, v_sub_index)
particle_velocity_nosub = np.delete(particle_velocity, v_sub_index)

pl.scatter(particle_position_nosub, particle_velocity_nosub, color='b', marker='o')
pl.scatter(particle_position_sub  , particle_velocity_sub  , color='r', marker='^')
pl.show()