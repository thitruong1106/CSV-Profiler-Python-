from profiler import profile_columns, load_csv

def main():
    path = input("Enter CSV path: ")
    rows = load_csv(path)
    if rows:
        profile_columns(rows)

if __name__ == "__main__":
    main()
