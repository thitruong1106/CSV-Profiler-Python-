# CSV Profiler (Python)

A lightweight CSV profiling tool written in Python to quickly assess data quality and value distribution at the column level.

This tool is designed to help analysts understand a dataset **before** performing analysis, writing SQL queries, or building dashboards by highlighting missing values, common categories, and potential data quality issues.

---

## Features 

- Safe CSV loading using csv.DictReader 
- Per-column statistic 
    - Total rows 
    - Missing / empty values 
    - Non missing values 
    - Percentage missing 
    - Top 3 most frequent values 
    - Total unique values 
- Handles empty / missing data 
- Clean, readable console output 

---

## Wehn to use this tool 

This tool is useful at the **early stage of data analysis**, for example: 
- Before exploring a new dataset 
- Before loading data into SQL table 
- Before building reports and dashboards 
- When validating data received from external sources 

It helps surface data issues early so they can be addressed before data analysis. 

## Technologies 
- Python 3 
- csv module 

---
