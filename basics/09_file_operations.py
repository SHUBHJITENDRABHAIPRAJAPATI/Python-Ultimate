"""
File Operations in Python
==========================
This file demonstrates reading and writing files.
"""

import os

# Writing to a file
print("=== Writing to a File ===")
# Create a temporary file for demonstration
filename = "sample.txt"

# Writing mode ('w') - overwrites existing content
with open(filename, 'w') as file:
    file.write("Hello, Python!\n")
    file.write("This is a sample file.\n")
    file.write("Learning file operations is fun!\n")
print(f"Written to {filename}")

# Reading from a file
print("\n=== Reading from a File ===")
with open(filename, 'r') as file:
    content = file.read()
    print("File content:")
    print(content)

# Reading line by line
print("\n=== Reading Line by Line ===")
with open(filename, 'r') as file:
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")

# Appending to a file
print("\n=== Appending to a File ===")
with open(filename, 'a') as file:
    file.write("This line was appended!\n")
print(f"Appended to {filename}")

# Read updated content
with open(filename, 'r') as file:
    print("\nUpdated content:")
    print(file.read())

# Reading lines into a list
print("\n=== Reading Lines into a List ===")
with open(filename, 'r') as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")
    print(f"First line: {lines[0].strip()}")

# Check if file exists
print("\n=== Checking File Existence ===")
if os.path.exists(filename):
    print(f"{filename} exists")
else:
    print(f"{filename} does not exist")

# Get file information
print("\n=== File Information ===")
if os.path.exists(filename):
    file_size = os.path.getsize(filename)
    print(f"File size: {file_size} bytes")

# Clean up - delete the file
print("\n=== Cleaning Up ===")
if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} has been deleted")

# Working with CSV-like data
print("\n=== Working with Structured Data ===")
# Create a CSV-like file
csv_file = "data.txt"
with open(csv_file, 'w') as file:
    file.write("Name,Age,City\n")
    file.write("Alice,25,New York\n")
    file.write("Bob,30,London\n")
    file.write("Charlie,35,Paris\n")

# Read and parse CSV-like data
with open(csv_file, 'r') as file:
    header = file.readline().strip().split(',')
    print(f"Header: {header}")
    print("\nData:")
    for line in file:
        data = line.strip().split(',')
        print(f"  {data[0]}: {data[1]} years old, lives in {data[2]}")

# Clean up
os.remove(csv_file)
print(f"\n{csv_file} has been deleted")

print("\n✅ File Operations demonstration complete!")
