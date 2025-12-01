# US Bikeshare Data Analysis

## Project Overview

This Python project analyzes bike share system data from three major US cities: Chicago, New York City, and Washington, DC. The interactive command-line tool computes descriptive statistics and reveals usage patterns across these bike-sharing systems.

## About the Data

### Data Source
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.
The Datasets

### Core Data Fields
All datasets include:
- **Start Time** - Trip start timestamp (e.g., 2017-01-01 00:07:57)
- **End Time** - Trip end timestamp (e.g., 2017-01-01 00:20:53)
- **Trip Duration** - Duration in seconds (e.g., 776)
- **Start Station** - Starting location (e.g., Broadway & Barry Ave)
- **End Station** - Ending location (e.g., Sedgwick St & North Ave)
- **User Type** - Subscriber or Customer

### Additional Fields (Chicago & NYC only)
- **Gender**
- **Birth Year**

## Analysis Features

The script computes the following statistics:

### 1. Popular Travel Times
- Most common month
- Most common day of week
- Most common hour of day

### 2. Station & Trip Analysis
- Most popular start station
- Most popular end station
- Most frequent trip route (start-end station combination)

### 3. Trip Duration Metrics
- Total travel time
- Average travel time

### 4. User Demographics
- User type distribution
- Gender distribution (Chicago & NYC only)
- Birth year statistics: earliest, most recent, and most common (Chicago & NYC only)

## Project Files

### Required Files
- `bikeshare.py` - Main Python script with template code
- `chicago.csv` - Chicago dataset
- `new_york_city.csv` - New York City dataset
- `washington.csv` - Washington, DC dataset

## Getting Started

Run the interactive script from your terminal to explore the data and view statistics for your chosen city.

---

**Acknowledgments**  
Project and data provided by [Udacity](https://www.udacity.com/)