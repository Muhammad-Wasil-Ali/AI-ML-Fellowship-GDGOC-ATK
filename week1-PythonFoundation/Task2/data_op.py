"""
Data Manipulation Practice
Remove duplicates, Sort data, Find max/min/average
"""


def remove_duplicates_list(data):
    """
    Remove duplicates from a list while preserving order
    
    Args:
        data (list): List with potential duplicates
    
    Returns:
        list: List without duplicates
    """
    seen = set()
    result = []
    
    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result


def remove_duplicates_simple(data):
    """Remove duplicates using set (doesn't preserve order)"""
    return list(set(data))


def remove_duplicates_dict(data, key):
    """
    Remove duplicate dictionaries based on a key
    
    Args:
        data (list): List of dictionaries
        key (str): Key to check for duplicates
    
    Returns:
        list: List without duplicates
    """
    seen = set()
    result = []
    
    for item in data:
        if item[key] not in seen:
            seen.add(item[key])
            result.append(item)
    
    return result


def sort_numbers(data, reverse=False):
    """
    Sort a list of numbers
    
    Args:
        data (list): List of numbers
        reverse (bool): Sort in descending order if True
    
    Returns:
        list: Sorted list
    """
    return sorted(data, reverse=reverse)


def sort_strings(data, reverse=False, case_sensitive=False):
    """
    Sort a list of strings
    
    Args:
        data (list): List of strings
        reverse (bool): Sort in descending order if True
        case_sensitive (bool): Consider case when sorting
    
    Returns:
        list: Sorted list
    """
    if case_sensitive:
        return sorted(data, reverse=reverse)
    else:
        return sorted(data, key=str.lower, reverse=reverse)


def sort_dict_by_key(data, key, reverse=False):
    """
    Sort list of dictionaries by a specific key
    
    Args:
        data (list): List of dictionaries
        key (str): Key to sort by
        reverse (bool): Sort in descending order if True
    
    Returns:
        list: Sorted list
    """
    return sorted(data, key=lambda x: x[key], reverse=reverse)


def find_max(data):
    """
    Find maximum value in a list
    
    Args:
        data (list): List of numbers
    
    Returns:
        float: Maximum value
    """
    if not data:
        return None
    return max(data)


def find_min(data):
    """
    Find minimum value in a list
    
    Args:
        data (list): List of numbers
    
    Returns:
        float: Minimum value
    """
    if not data:
        return None
    return min(data)


def find_average(data):
    """
    Calculate average of numbers in a list
    
    Args:
        data (list): List of numbers
    
    Returns:
        float: Average value
    """
    if not data:
        return None
    return sum(data) / len(data)


def find_median(data):
    """
    Find median value in a list
    
    Args:
        data (list): List of numbers
    
    Returns:
        float: Median value
    """
    if not data:
        return None
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 0:
        # Even number of elements
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        # Odd number of elements
        return sorted_data[n//2]


def find_mode(data):
    """
    Find most common value(s) in a list
    
    Args:
        data (list): List of values
    
    Returns:
        list: Most common value(s)
    """
    if not data:
        return None
    
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    
    max_freq = max(frequency.values())
    return [key for key, value in frequency.items() if value == max_freq]


def calculate_statistics(data):
    """
    Calculate comprehensive statistics for a list of numbers
    
    Args:
        data (list): List of numbers
    
    Returns:
        dict: Dictionary containing various statistics
    """
    if not data:
        return None
    
    sorted_data = sorted(data)
    
    stats = {
        'count': len(data),
        'sum': sum(data),
        'min': min(data),
        'max': max(data),
        'range': max(data) - min(data),
        'mean': sum(data) / len(data),
        'median': find_median(data),
        'mode': find_mode(data)
    }
    
    # Calculate standard deviation
    mean = stats['mean']
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    stats['std_dev'] = variance ** 0.5
    
    return stats


def filter_data(data, condition):
    """
    Filter data based on a condition function
    
    Args:
        data (list): List of data
        condition (function): Function that returns True/False
    
    Returns:
        list: Filtered list
    """
    return [item for item in data if condition(item)]


def group_by(data, key):
    """
    Group list of dictionaries by a key
    
    Args:
        data (list): List of dictionaries
        key (str): Key to group by
    
    Returns:
        dict: Dictionary with grouped data
    """
    groups = {}
    
    for item in data:
        group_key = item[key]
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(item)
    
    return groups


def merge_lists(*lists):
    """
    Merge multiple lists into one
    
    Args:
        *lists: Variable number of lists
    
    Returns:
        list: Merged list
    """
    result = []
    for lst in lists:
        result.extend(lst)
    return result


def chunk_list(data, chunk_size):
    """
    Split a list into chunks of specified size
    
    Args:
        data (list): List to split
        chunk_size (int): Size of each chunk
    
    Returns:
        list: List of chunks
    """
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]


# ============= DEMONSTRATION =============

def demo_remove_duplicates():
    """Demonstrate duplicate removal"""
    print("\n" + "=" * 60)
    print("  REMOVE DUPLICATES DEMO")
    print("=" * 60)
    
    # Numbers with duplicates
    numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
    print(f"\nOriginal list: {numbers}")
    print(f"Without duplicates (ordered): {remove_duplicates_list(numbers)}")
    print(f"Without duplicates (simple): {remove_duplicates_simple(numbers)}")
    
    # Strings with duplicates
    words = ["apple", "banana", "apple", "cherry", "banana"]
    print(f"\nOriginal list: {words}")
    print(f"Without duplicates: {remove_duplicates_list(words)}")
    
    # Dictionaries with duplicates
    students = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 1, "name": "Alice Duplicate"},
        {"id": 3, "name": "Charlie"}
    ]
    print(f"\nOriginal students: {students}")
    print(f"Without duplicates (by id): {remove_duplicates_dict(students, 'id')}")


def demo_sorting():
    """Demonstrate sorting"""
    print("\n" + "=" * 60)
    print("  SORTING DEMO")
    print("=" * 60)
    
    # Sort numbers
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal: {numbers}")
    print(f"Ascending: {sort_numbers(numbers)}")
    print(f"Descending: {sort_numbers(numbers, reverse=True)}")
    
    # Sort strings
    names = ["Charlie", "alice", "Bob", "diana"]
    print(f"\nOriginal: {names}")
    print(f"Sorted (case-insensitive): {sort_strings(names)}")
    print(f"Sorted (case-sensitive): {sort_strings(names, case_sensitive=True)}")
    
    # Sort dictionaries
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92},
        {"name": "Charlie", "grade": 78}
    ]
    print(f"\nOriginal: {students}")
    print(f"Sorted by grade: {sort_dict_by_key(students, 'grade', reverse=True)}")


def demo_statistics():
    """Demonstrate statistical functions"""
    print("\n" + "=" * 60)
    print("  STATISTICS DEMO")
    print("=" * 60)
    
    numbers = [23, 45, 67, 45, 89, 12, 45, 78, 90, 23]
    
    print(f"\nData: {numbers}")
    print(f"Max: {find_max(numbers)}")
    print(f"Min: {find_min(numbers)}")
    print(f"Average: {find_average(numbers):.2f}")
    print(f"Median: {find_median(numbers)}")
    print(f"Mode: {find_mode(numbers)}")
    
    print("\n--- Comprehensive Statistics ---")
    stats = calculate_statistics(numbers)
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"{key.capitalize()}: {value:.2f}")
        else:
            print(f"{key.capitalize()}: {value}")


def demo_filtering():
    """Demonstrate data filtering"""
    print("\n" + "=" * 60)
    print("  FILTERING DEMO")
    print("=" * 60)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"\nOriginal: {numbers}")
    print(f"Even numbers: {filter_data(numbers, lambda x: x % 2 == 0)}")
    print(f"Numbers > 5: {filter_data(numbers, lambda x: x > 5)}")
    print(f"Numbers divisible by 3: {filter_data(numbers, lambda x: x % 3 == 0)}")


def demo_grouping():
    """Demonstrate data grouping"""
    print("\n" + "=" * 60)
    print("  GROUPING DEMO")
    print("=" * 60)
    
    students = [
        {"name": "Alice", "grade": "A", "age": 20},
        {"name": "Bob", "grade": "B", "age": 21},
        {"name": "Charlie", "grade": "A", "age": 20},
        {"name": "Diana", "grade": "B", "age": 22}
    ]
    
    print("\nGrouping by grade:")
    grouped = group_by(students, 'grade')
    for grade, students_list in grouped.items():
        print(f"\nGrade {grade}:")
        for student in students_list:
            print(f"  - {student['name']} (Age: {student['age']})")


def demo_list_operations():
    """Demonstrate list operations"""
    print("\n" + "=" * 60)
    print("  LIST OPERATIONS DEMO")
    print("=" * 60)
    
    # Merge lists
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]
    print(f"\nLists: {list1}, {list2}, {list3}")
    print(f"Merged: {merge_lists(list1, list2, list3)}")
    
    # Chunk list
    long_list = list(range(1, 21))
    print(f"\nOriginal: {long_list}")
    print(f"Chunked (size 5): {chunk_list(long_list, 5)}")


# ============= PRACTICAL EXAMPLES =============

def example_student_grades():
    """Practical example: Analyzing student grades"""
    print("\n" + "=" * 60)
    print("  PRACTICAL EXAMPLE: STUDENT GRADES ANALYSIS")
    print("=" * 60)
    
    grades = [85, 92, 78, 92, 88, 76, 92, 95, 88, 82]
    
    print(f"\nGrades: {grades}")
    
    # Remove duplicates
    unique_grades = remove_duplicates_list(grades)
    print(f"Unique grades: {unique_grades}")
    
    # Sort
    sorted_grades = sort_numbers(grades, reverse=True)
    print(f"Sorted (high to low): {sorted_grades}")
    
    # Statistics
    print(f"\nStatistics:")
    print(f"  Highest: {find_max(grades)}")
    print(f"  Lowest: {find_min(grades)}")
    print(f"  Average: {find_average(grades):.2f}")
    print(f"  Median: {find_median(grades)}")
    print(f"  Most common: {find_mode(grades)}")
    
    # Filter
    passing_grades = filter_data(grades, lambda x: x >= 80)
    print(f"\nPassing grades (>=80): {passing_grades}")
    print(f"Pass rate: {len(passing_grades)/len(grades)*100:.1f}%")


def main():
    """Run all demonstrations"""
    print("\n" + "=" * 60)
    print("  DATA MANIPULATION PRACTICE")
    print("=" * 60)
    
    while True:
        print("\n" + "=" * 50)
        print("  Choose a demo:")
        print("=" * 50)
        print("  1. Remove Duplicates")
        print("  2. Sorting")
        print("  3. Statistics (Max/Min/Average)")
        print("  4. Filtering")
        print("  5. Grouping")
        print("  6. List Operations")
        print("  7. Practical Example (Student Grades)")
        print("  8. Run All Demos")
        print("  9. Exit")
        print("=" * 50)
        
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == '1':
            demo_remove_duplicates()
        elif choice == '2':
            demo_sorting()
        elif choice == '3':
            demo_statistics()
        elif choice == '4':
            demo_filtering()
        elif choice == '5':
            demo_grouping()
        elif choice == '6':
            demo_list_operations()
        elif choice == '7':
            example_student_grades()
        elif choice == '8':
            demo_remove_duplicates()
            demo_sorting()
            demo_statistics()
            demo_filtering()
            demo_grouping()
            demo_list_operations()
            example_student_grades()
        elif choice == '9':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()


