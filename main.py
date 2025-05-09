import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import os
from algorithm import *

def generateBlockForSmallSample(filename):
    print(f"Generating small sample block for {filename}")

def generateBlockForLargeSample(filename):
    print(f"Generating large sample block for {filename}")

def main():
    # Define the DATASET folder path
    dataset_path = "DATASET"
    
    # Check if directory exists
    if not os.path.exists(dataset_path):
        print(f"Error: {dataset_path} directory does not exist")
        return
    
    # Get all .mat files in the DATASET folder
    mat_files = [f for f in os.listdir(dataset_path) if f.endswith('.mat')]
    
    print(f"Found {len(mat_files)} .mat files in {dataset_path}")
    
    # Process each .mat file
    for mat_file in mat_files:
        file_path = os.path.join(dataset_path, mat_file)
        print(f"\nProcessing {mat_file}...")
        
        try:
            # Load .mat file
            mat_data = scipy.io.loadmat(file_path)
            
            # Get the 3D data (assuming 'sign_depth_palmfilter' is the key in all files)
            if 'sign_depth_palmfilter' in mat_data:
                img_sequence = mat_data['sign_depth_palmfilter']
                
                # Get the dimensions of the 3D array
                shape = img_sequence.shape
                print(f"Dimensions of img_sequence: {shape}")
                
                # To specifically get the third dimension (number of frames/depth)
                num_frames = shape[2]
                print(f"Number of frames: {num_frames}")
                
                # Generate Block based on the number of frames
                if num_frames < 100:
                    generateBlockForSmallSample(mat_file)
                else:
                    generateBlockForLargeSample(mat_file)
            else:
                print(f"Warning: 'sign_depth_palmfilter' key not found in {mat_file}")
                print(f"Available keys: {mat_data.keys()}")
        
        except Exception as e:
            print(f"Error processing {mat_file}: {str(e)}")

if __name__ == "__main__":
    main()