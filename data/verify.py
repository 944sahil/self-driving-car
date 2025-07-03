import numpy as np
import cv2
from collections import Counter

# Load the data
DATA_FILE = 'training_data.npy'
data = np.load(DATA_FILE, allow_pickle=True)

print(f"Total samples: {len(data)}")
print(f"Type of first sample: {type(data[0])}")

# Show a few samples
for i in range(5):
    img, output = data[i]
    print(f"Sample {i}: Output vector: {output}")
    cv2.imshow(f"Sample {i}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Count occurrences of each output vector
outputs = [tuple(sample[1]) for sample in data]
counts = Counter(outputs)

print("Output vector counts:")
for output_vec, count in counts.items():
    print(f"{output_vec}: {count}")