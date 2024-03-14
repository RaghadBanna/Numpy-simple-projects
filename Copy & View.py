
import numpy as np

# Creating a 2D NumPy array
original_array = np.array([[1, 2, 3], [4, 5, 6]])

# Creating a copy of the original array
copied_array = original_array.copy()

# Creating a view of the original array
view_array = original_array.view()

# Modifying the original array
original_array[0, 0] = 99

# Displaying the arrays
print("Original Array:")
print(original_array)

print("\nCopied Array:")
print(copied_array)

print("\nView Array:")
print(view_array)