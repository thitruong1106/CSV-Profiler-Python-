import csv 

def load_csv(path: str):
    try: 
        with open(path, 'r', encoding='utf-8', newline='') as file: 
            reader = csv.DictReader(file)
            rows = list(reader)
            if not rows: 
                print("File is empty (no rows can be found)")
            return rows
    except FileNotFoundError: 
        print("File can not be found at path: {path}")
        return []
    except Exception as e: 
        print("Error {e}")
        return [] 