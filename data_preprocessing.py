from scipy.io import loadmat
import numpy as np

sdf_data=loadmat('SDF_values.mat')['SDF_values']
#print(sdf_data)

sdf_data = np.expand_dims(sdf_data,axis=3)
print(len(sdf_data))