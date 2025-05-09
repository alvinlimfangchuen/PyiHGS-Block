import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load .mat file
mat_data = scipy.io.loadmat('Sample_Signature_One.mat')
print(mat_data.keys())

# Get the 3D data
img_sequence = mat_data['sign_depth_palmfilter']

# Display a specific frame (for example, the first frame)
frame_index = 0  # Change this to view different frames
plt.imshow(img_sequence[:, :, frame_index])
plt.title(f'Frame {frame_index}')
plt.show()