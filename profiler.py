import csv

def load_csv(path: str):
    try: 
        with open(path, 'r', encoding='utf-8', newline='') as file: 
            reader = csv.DictReader(file)
            rows = list(reader)
            if not rows: 
                print("Empty file")
                return None 
            return rows
    except FileNotFoundError: 
        print(f"File not found error: {path}")
        return None 
    except Exception as e: 
        print(f"Error: {e}")

def profile_columns(rows):
    """
    Print summary statistic for each column in the dataset. 

    For each column, the function prints the following: 
        - Column name 
        - Total numbers of rows 
        - Count of missing values (None OR "")
        - Count of non-missing vlaues 
        - Percentage of missing values 
        - Top 3 most frequent non-missing values 
        - Number of unique non-missing values 

    Args: 
        rows (list[dict]): List of row dictionaries (already cleaned)
    
    Returns: 
        None    
    """
    if not rows: 
        print("No rows found")
        return
    columns = list(rows[0].keys())
    for column in columns: 
        print("-" * 30)
        print(f"Column: {column}")
        total_rows = len(rows) 
        missing_count = 0 
        non_missing = 0 
        counts = {}
        for row in rows:
            value = row.get(column)
            if value is None or value == "":
                missing_count += 1
            else: 
                non_missing += 1 
                if value in counts:
                    counts[value] += 1 
                else: 
                    counts[value] = 1 

        missing_percent = (missing_count / total_rows) * 100
        print(f"Total: rows: {total_rows}")
        print(f"Missing counts: {missing_count}")
        print(f"Non Missing counts: {non_missing}")
        print(f"Missing% : {missing_percent:.1f}%")
        if counts: 
            sorted_items = [] 

            for value, count in counts.items(): 
                sorted_items.append((count, value))
            sorted_items.sort(reverse=True)

            for i in range(min(3, len(sorted_items))):
                count, value = sorted_items[i]
                print(f"{i+1}. '{value}' : {count} times")
            print(f"- Total unique values: {len(counts)}")
        else: 
            print("Values are missing or empty")