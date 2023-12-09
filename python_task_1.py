#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


#CREATE A CAR METRICS GENERATION


# In[3]:


data=pd.read_csv("dataset-1.csv")


# In[4]:


data.head()


# In[5]:


df=pd.DataFrame(data)


# In[6]:


df.isnull().sum()


# In[7]:


pivot_df = df.pivot_table(index='id_1', columns='id_2', values='car', aggfunc=lambda x: x)


# In[8]:


pivot_df = pivot_df.fillna(0)


# In[9]:


for col in pivot_df.columns:
    pivot_df.loc[col, col] = 0


# In[10]:


print("Reshaped DataFrame:") 
print(pivot_df)


# QUESTION 2   Car Type Count Calculation
# 

# In[11]:


# Add a new categorical column 'car_type'


# In[12]:


df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                        labels=['high', 'medium', 'low'], right=False)


# In[13]:


car_type_counts = df['car_type'].value_counts().to_dict()


# In[14]:


sorted_car_type_counts = dict(sorted(car_type_counts.items()))


# In[15]:


print("Car Type Counts:")
print(sorted_car_type_counts)


# QUESTION 3 Bus Count Index Retrieval

# In[16]:


def get_bus_indexes(data):
    # Calculate the mean value of the 'bus' column
    mean_bus = data['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = data[data['bus'] > 2 * mean_bus].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes




# In[17]:


df = pd.DataFrame(data)

result = get_bus_indexes(df)
print("Bus Indexes:", result)


# QUESTION 4 

# In[18]:


def filter_routes(data):
    # Calculate the average value of the 'truck' column
    avg_truck = data['truck'].mean()

    # Filter rows where the average of 'truck' values is greater than 7
    filtered_data = data[data['truck'] > 7]

    # Get the unique values of the 'route' column and sort them
    sorted_routes = sorted(filtered_data['route'].unique())

    return sorted_routes

data=pd.read_csv("dataset-1.csv")
df = pd.DataFrame(data)

result = filter_routes(df)
print("Filtered Routes:", result)


# Question 5

# In[19]:


data=pd.read_csv("dataset-1.csv")

# Creating a DataFrame (replace this with your actual DataFrame)
df = pd.DataFrame(data)

def multiply_matrix(df):
    # Copy the DataFrame to avoid modifying the original one
    modified_df = df.copy()

    # Apply the logic to modify values in the DataFrame
    modified_df['car'] = modified_df['car'].apply(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round the values to 1 decimal place
    modified_df['car'] = modified_df['car'].round(1)

    return modified_df

modified_result = multiply_matrix(df)
print("Modified DataFrame:")
print(modified_result)


# In[20]:


data


# QUESTION 6

# In[21]:


def check_time_completeness(data):
    # Convert timestamp columns to datetime objects
    data['start_datetime'] = pd.to_datetime(data['startDay'] + ' ' + data['startTime'], errors='coerce')
    data['end_datetime'] = pd.to_datetime(data['endDay'] + ' ' + data['endTime'], errors='coerce')

    # Drop rows with missing datetime values
    data = data.dropna(subset=['start_datetime', 'end_datetime'])

    # Extract day of the week and hour for each timestamp
    data['day_of_week'] = data['start_datetime'].dt.dayofweek
    data['hour'] = data['start_datetime'].dt.hour

    # Create a mask for incorrect timestamps
    incorrect_timestamps = (
        (data['hour'] != 0) | (data['day_of_week'] < 0) | (data['day_of_week'] > 6)
    )

    # Group by (id, id_2) and check if any timestamp is incorrect for each group
    result_series = data.groupby(['id', 'id_2'])['start_datetime'].transform(lambda x: any(incorrect_timestamps.loc[x.index]))

    return result_series



data = pd.read_csv("dataset-2.csv")

result = check_time_completeness(data)
print("Boolean Series for Time Completeness:")
print(result)


# In[ ]:




