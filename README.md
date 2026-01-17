# ADHOC Python Task – Data Filtering & JSON Processing

## Overview
This repository contains Python scripts written to solve a set of adhoc tasks involving:

- Data type checking and filtering in Python lists  
- Controlled error handling (graceful bypass vs intentional failure)  
- JSON data extraction and conditional filtering  

The tasks demonstrate understanding of **Python data types, control flow, exception handling, and JSON manipulation**.

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Lorreta-Anyika/adhock_tasks_mayor_engineering.git
```

### 2. Navigate into the project directory
```bash
cd adhock_tasks_mayor_engineering
```

### 3. Run the Python scripts
Make sure Python is installed, then run the scripts individually:
```bash
python script_name.py
```

## PART 1 – Python List Processing

### 1. Filtering Strings with Specific Patterns

**Task:**  
Write a script that:
- Iterates through a list containing mixed data types
- Checks the data type of each element
- Filters out only the strings that:
  - Start with **"Republic"**
  - End with **"Nigeria"**

**Input List:**
```python
data = [
    "8",
    8,
    "Republic of Ireland",
    "Federal Republic of Nigeria",
    "Federal Republic of Germany",
    "Federal Republic of Somalia"
]
```
### 2. Gracefully Bypass String Data in a List

Task:
Write a script that:

- Iterates through a list
- Performs an operation only on non-string elements
- Gracefully skips any string-related data without crashing

#### Key Concept Used:
- pass
- Conditional logic (if/else)
  
This approach ensures the program continues running even when strings are present.

### 3. Intentionally Break When String Data Is Found
Task:
Write a script that:
- Iterates through a list
- Raises an error immediately when a string is detected

#### Key Concept Used:
- Explicit exception raising (raise TypeError)
  
This approach is useful in strict data validation pipelines, where invalid data should halt execution.

## PART 2 – JSON Processing
### 4. JSON File Handling & Data Extraction

Task Workflow:

- Download a JSON file from the provided link
- Save it locally in the working directory
- Extract the following fields for each entry: name, title, attack, defence
- Filter the data to include only entries where: attack > 5 and defence > 5
- Save the filtered output into a new JSON file
  
## Tools & Technologies

1. Python 3.x
2. Built-in Libraries:
- json
- os
- requests

No external dependencies are required.
