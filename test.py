import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Generate random 2D data
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Create a scatter plot using Matplotlib
fig, ax = plt.subplots()
ax.scatter(x, y, c='blue', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Random 2D Data Scatter Plot')

# Display the plot in Streamlit
st.pyplot(fig)

# Optionally, display some data summary
st.write(f"Displaying {num_points} random data points.")
