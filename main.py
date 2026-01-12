from profiler import profile_columns, load_csv, print_profile

def main():
    path = input("Enter path: ")
    rows = load_csv(path)
    report = profile_columns(rows)
    print_profile(report)

if __name__ == "__main__":
    main()
