#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv("dataset-3.csv")


# In[12]:


def calculate_distance_matrix(data):
    # Create a DataFrame with unique IDs
    unique_ids = sorted(set(data['id_start'].unique()) | set(data['id_end'].unique()))
    distance_matrix = pd.DataFrame(0, index=unique_ids, columns=unique_ids)

    # Populate the matrix with cumulative distances along known routes
    for _, row in data.iterrows():
        id_start, id_end, distance = row['id_start'], row['id_end'], row['distance']
        # Update both directions since distances are bidirectional
        distance_matrix.loc[id_start, id_end] += distance
        distance_matrix.loc[id_end, id_start] += distance

    return distance_matrix

# Example usage:
# Create a sample DataFrame
data=pd.read_csv("dataset-3.csv")

df = pd.DataFrame(data)

# Call the function with the correct DataFrame
result = calculate_distance_matrix(df)
print("Distance Matrix:")
print(result)


# Question 2

# In[13]:


def unroll_distance_matrix(distance_matrix):
    # Get the upper triangular part of the distance matrix (excluding the diagonal)
    upper_triangle = distance_matrix.where(np.triu(np.ones(distance_matrix.shape), k=1).astype(bool))

    # Reset the index and rename columns
    unrolled_df = upper_triangle.stack().reset_index()
    unrolled_df.columns = ['id_start', 'id_end', 'distance']

    return unrolled_df


distance_matrix = calculate_distance_matrix(df)

result = unroll_distance_matrix(distance_matrix)
print("Unrolled Distance Matrix:")
print(result)


# Question 3
# 

# In[18]:


def find_ids_within_ten_percentage_threshold(data, reference_value):
    # Filter rows for the reference value
    reference_data = data[data['id_start'] == reference_value]

    # Calculate the average distance for the reference value
    average_distance = reference_data['distance'].mean()

    # Calculate the threshold values
    lower_threshold = average_distance * 0.9
    upper_threshold = average_distance * 1.1

    # Filter rows within the 10% threshold
    within_threshold = data[(data['id_start'] != reference_value) & (data['distance'] >= lower_threshold) & (data['distance'] <= upper_threshold)]

    # Get unique values from the 'id_start' column and sort them
    result_list = sorted(within_threshold['id_start'].unique())

    return result_list


data=pd.read_csv("dataset-3.csv")

df = pd.DataFrame(data)

reference_value = 'A'  

result = find_ids_within_ten_percentage_threshold(df, reference_value)
print("IDs within 10% threshold:", result)


# QUESTION 4

# In[19]:


def calculate_toll_rate(data):
    # Add columns for toll rates based on vehicle types
    data['moto'] = 0.8 * data['distance']
    data['car'] = 1.2 * data['distance']
    data['rv'] = 1.5 * data['distance']
    data['bus'] = 2.2 * data['distance']
    data['truck'] = 3.6 * data['distance']

    return data

# Example usage:
# Assuming 'unrolled_df' is the DataFrame created in the previous step
# Replace it with your actual DataFrame
data=pd.read_csv("dataset-3.csv")
df = pd.DataFrame(data)

result = calculate_toll_rate(df)
print("DataFrame with Toll Rates:")
print(result)

