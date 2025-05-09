import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import os


def generateBlockForSmallSample(filename):
    print(f"Generating small sample block for {filename}")

def generateBlockForLargeSample(filename):
    print(f"Generating large sample block for {filename}")

def generate_empty_frames(height=480, width=640, num_frames=10, dtype=np.float32):
    """
    Generate empty frames and display the first frame.
    
    Parameters:
    -----------
    height : int, default=480
        Height of each frame
    width : int, default=640
        Width of each frame
    num_frames : int, default=10
        Number of frames to generate
    dtype : data type, default=np.float32
        Data type of the array
        
    Returns:
    --------
    np.ndarray
        Empty 3D array with dimensions height x width x num_frames
    """
    # Create an empty 3D array with dimensions height x width x num_frames
    empty_frames = np.zeros((height, width, num_frames), dtype=dtype)
    print(f"Shape of empty frames: {empty_frames.shape}")

    # Display empty frames
    plt.figure()
    plt.imshow(empty_frames[:, :, 0], cmap='gray')
    plt.title("Empty Frame")
    plt.colorbar()
    
    return empty_frames