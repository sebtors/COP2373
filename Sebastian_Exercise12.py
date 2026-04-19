import numpy as np

# Function to load only numeric exam columns (ignores names)
def load_data(filename):
    try:
        data = np.genfromtxt(
            filename,
            delimiter=',',
            skip_header=1,
            usecols=(2, 3, 4)  # Only Exam1, Exam2, Exam3
        )
        return data
    except Exception as e:
        print("Error loading file:", e)
        return None

# Function to preview dataset
def preview_data(data):
    print("First 5 rows of the dataset:")
    print(data[:5])
    print()

# Function for per-exam statistics
def exam_statistics(data):
    print("=== Per Exam Statistics ===")
    print("Mean:", np.mean(data, axis=0))
    print("Median:", np.median(data, axis=0))
    print("Standard Deviation:", np.std(data, axis=0))
    print("Minimum:", np.min(data, axis=0))
    print("Maximum:", np.max(data, axis=0))
    print()

# Function for overall statistics
def overall_statistics(data):
    print("=== Overall Statistics ===")
    print("Mean:", np.mean(data))
    print("Median:", np.median(data))
    print("Standard Deviation:", np.std(data))
    print("Minimum:", np.min(data))
    print("Maximum:", np.max(data))
    print()

# Function to calculate pass/fail
def pass_fail_counts(data):
    print("=== Pass/Fail Per Exam ===")

    passing = data >= 60

    for i in range(data.shape[1]):
        passed = np.sum(passing[:, i])
        failed = data.shape[0] - passed
        print(f"Exam {i+1}: Passed = {passed}, Failed = {failed}")

    total_passed = np.sum(passing)
    total_grades = data.size
    pass_percentage = (total_passed / total_grades) * 100

    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")
    print()

# Main function
def main():
    filename = "grades.csv"

    data = load_data(filename)

    if data is None:
        print("Could not load data.")
        return

    preview_data(data)
    exam_statistics(data)
    overall_statistics(data)
    pass_fail_counts(data)

if __name__ == "__main__":
    main()