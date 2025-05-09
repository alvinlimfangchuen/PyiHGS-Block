import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Store a specific frame in a variable
mat_data = scipy.io.loadmat('Sample_Signature_One.mat')
img_sequence = mat_data['sign_depth_palmfilter']
frame_index = 0  # The index of the frame you want to store
single_frame = img_sequence[:, :, frame_index]

# Now you can use this single_frame variable
print(f"Shape of the single frame: {single_frame.shape}")

# Display the single frame
plt.imshow(single_frame)
plt.title(f"Frame {frame_index}")
plt.colorbar()
plt.show()


# Create an empty 3D array with dimensions 480x640x10
empty_frames = np.zeros((480, 640, 10), dtype=np.float32) 


print(f"Shape of empty frames: {empty_frames.shape}")

# Display  empty frames
plt.figure()
plt.imshow(empty_frames[:, :, 0])
plt.title("Empty Frame")
plt.colorbar()
plt.show()