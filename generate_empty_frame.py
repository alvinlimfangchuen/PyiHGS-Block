import scipy.io
import numpy as np
import matplotlib.pyplot as plt


# Create an empty 3D array with dimensions 480x640x10
empty_frames = np.zeros((480, 640, 10), dtype=np.float32)
print(f"Shape of empty frames: {empty_frames.shape}")

# Display empty frames
plt.figure()
plt.imshow(empty_frames[:, :, 0], cmap='gray')
plt.title("Empty Frame")
plt.colorbar()

