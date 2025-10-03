import csv

# Define messy data with intentional type issues
data = [
    {'student_id': 1, 'major': 'Math', 'GPA': 3, 'is_cs_major': 'No', 'credits_taken': '12.5'},
    {'student_id': 2, 'major': 'Computer Science', 'GPA': 3.7, 'is_cs_major': 'Yes', 'credits_taken': '15'},
    {'student_id': 3, 'major': 'Physics', 'GPA': 4, 'is_cs_major': 'No', 'credits_taken': '9.5'},
    {'student_id': 4, 'major': 'Engineering', 'GPA': 2.8, 'is_cs_major': 'No', 'credits_taken': '18.0'},
    {'student_id': 5, 'major': 'Computer Science', 'GPA': 3, 'is_cs_major': 'Yes', 'credits_taken': '20'}
]

# Write to CSV
filename = 'raw_survey_data.csv'

with open(filename, mode='w', newline='') as csvfile:
    fieldnames = ['student_id', 'major', 'GPA', 'is_cs_major', 'credits_taken']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"CSV file '{filename}' has been created.") 

import json

# Define hierarchical course data
courses = [
    {
        "course_id": "DS2002",
        "section": "001",
        "title": "Data Science Systems",
        "level": 200,
        "instructors": [
            {"name": "Austin Rivera", "role": "Primary"},
            {"name": "Heywood Williams-Tracy", "role": "TA"}
        ]
    },
    {
        "course_id": "ENGL3050",
        "section": "002",
        "title": "Literary Translation Workshop",
        "level": 300,
        "instructors": [
            {"name": "Claire Fontaine", "role": "Primary"}
        ]
    },
    {
        "course_id": "PHIL2400",
        "section": "001",
        "title": "Ethics and Technology",
        "level": 200,
        "instructors": [
            {"name": "Dr. Omar Singh", "role": "Primary"},
            {"name": "Jules Tan", "role": "TA"}
        ]
    }
]

# Write to JSON file
json_filename = 'raw_course_catalog.json'

with open(json_filename, 'w') as jsonfile:
    json.dump(courses, jsonfile, indent=2)

print(f"JSON file '{json_filename}' has been created.")

import pandas as pd

# Load raw CSV data
df = pd.read_csv('raw_survey_data.csv')

# Convert 'Yes'/'No' to True/False in is_cs_major
df['is_cs_major'] = df['is_cs_major'].replace({'Yes': True, 'No': False})

# Ensure GPA and credits_taken are floats
df = df.astype({'GPA': 'float64', 'credits_taken': 'float64'})

# Save cleaned data
df.to_csv('clean_survey_data.csv', index=False)

print("Cleaned CSV file 'clean_survey_data.csv' has been created.")

# Load raw JSON data
with open('raw_course_catalog.json', 'r') as jsonfile:
    course_data = json.load(jsonfile)

# Normalize nested instructors list
normalized_df = pd.json_normalize(
    course_data,
    record_path=['instructors'],
    meta=['course_id', 'title', 'level']
)

# Save normalized data
normalized_df.to_csv('clean_course_catalog.csv', index=False)

print("Normalized CSV file 'clean_course_catalog.csv' has been created.")

