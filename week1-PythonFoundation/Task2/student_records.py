"""
Student Record System
Manage student records using dictionaries and lists
"""

from utils import safe_float_input, safe_int_input, confirm_action


# Global storage for students
students = []


def generate_student_id():
    """Generate unique student ID"""
    if not students:
        return 1001
    return max(student['id'] for student in students) + 1


def add_student():
    """Add a new student record"""
    print("\n--- Add New Student ---")
    
    try:
        # Get student details
        name = input("Enter student name: ").strip()
        if not name:
            print("❌ Name cannot be empty!")
            return
        
        age = safe_int_input("Enter age: ", min_val=5, max_val=100)
        if age is None:
            return
        
        grade = input("Enter grade/class: ").strip()
        
        # Get subjects and marks
        print("\nEnter marks for subjects (or press Enter to finish):")
        subjects = {}
        
        while True:
            subject = input("Subject name (or Enter to finish): ").strip()
            if not subject:
                break
            
            marks = safe_float_input(f"Marks for {subject} (0-100): ", min_val=0, max_val=100)
            if marks is None:
                continue
            
            subjects[subject] = marks
        
        # Create student dictionary
        student = {
            'id': generate_student_id(),
            'name': name.title(),
            'age': age,
            'grade': grade,
            'subjects': subjects
        }
        
        students.append(student)
        print(f"\n✅ Student added successfully! ID: {student['id']}")
        
    except Exception as e:
        print(f"❌ Error adding student: {e}")


def display_all_students():
    """Display all student records"""
    if not students:
        print("\n📭 No students found!")
        return
    
    print("\n" + "=" * 80)
    print(f"{'ID':<8} {'Name':<20} {'Age':<6} {'Grade':<10} {'Subjects':<15}")
    print("=" * 80)
    
    for student in students:
        subjects_str = ", ".join(student['subjects'].keys()) if student['subjects'] else "None"
        print(f"{student['id']:<8} {student['name']:<20} {student['age']:<6} "
              f"{student['grade']:<10} {subjects_str:<15}")
    
    print("=" * 80)
    print(f"Total students: {len(students)}")


def display_student_details(student):
    """Display detailed information for a single student"""
    print("\n" + "=" * 60)
    print(f"  Student ID: {student['id']}")
    print("=" * 60)
    print(f"  Name: {student['name']}")
    print(f"  Age: {student['age']}")
    print(f"  Grade: {student['grade']}")
    
    if student['subjects']:
        print(f"\n  Subjects and Marks:")
        print("  " + "-" * 40)
        
        total_marks = 0
        for subject, marks in student['subjects'].items():
            print(f"  {subject:<25} {marks:>6.2f}")
            total_marks += marks
        
        print("  " + "-" * 40)
        average = total_marks / len(student['subjects'])
        print(f"  {'Average':<25} {average:>6.2f}")
        print(f"  {'Total':<25} {total_marks:>6.2f}")
        
        # Calculate grade
        if average >= 90:
            letter_grade = "A+"
        elif average >= 80:
            letter_grade = "A"
        elif average >= 70:
            letter_grade = "B"
        elif average >= 60:
            letter_grade = "C"
        elif average >= 50:
            letter_grade = "D"
        else:
            letter_grade = "F"
        
        print(f"  {'Grade':<25} {letter_grade:>6}")
    else:
        print("\n  No subjects recorded")
    
    print("=" * 60)


def search_student():
    """Search for a student by ID or name"""
    if not students:
        print("\n📭 No students to search!")
        return
    
    search_type = input("\nSearch by (1) ID or (2) Name? ").strip()
    
    try:
        if search_type == '1':
            student_id = safe_int_input("Enter student ID: ")
            found = [s for s in students if s['id'] == student_id]
        elif search_type == '2':
            name = input("Enter student name: ").strip().lower()
            found = [s for s in students if name in s['name'].lower()]
        else:
            print("❌ Invalid search type!")
            return
        
        if not found:
            print("❌ No students found!")
            return
        
        if len(found) == 1:
            display_student_details(found[0])
        else:
            print(f"\n✅ Found {len(found)} students:")
            for student in found:
                print(f"  ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")
    
    except Exception as e:
        print(f"❌ Error searching: {e}")


def update_student():
    """Update a student's record"""
    if not students:
        print("\n📭 No students to update!")
        return
    
    try:
        student_id = safe_int_input("\nEnter student ID to update: ")
        
        student = next((s for s in students if s['id'] == student_id), None)
        
        if not student:
            print("❌ Student not found!")
            return
        
        print(f"\nUpdating: {student['name']}")
        print("(Press Enter to keep current value)")
        
        # Update name
        new_name = input(f"Name [{student['name']}]: ").strip()
        if new_name:
            student['name'] = new_name.title()
        
        # Update age
        new_age_input = input(f"Age [{student['age']}]: ").strip()
        if new_age_input:
            new_age = int(new_age_input)
            if 5 <= new_age <= 100:
                student['age'] = new_age
        
        # Update grade
        new_grade = input(f"Grade [{student['grade']}]: ").strip()
        if new_grade:
            student['grade'] = new_grade
        
        # Update subjects
        update_subjects = input("Update subjects? (y/n): ").strip().lower()
        if update_subjects == 'y':
            print("\nCurrent subjects:")
            for subject, marks in student['subjects'].items():
                print(f"  {subject}: {marks}")
            
            print("\nOptions:")
            print("1. Add new subject")
            print("2. Update existing subject")
            print("3. Remove subject")
            
            choice = input("Choose option (1-3): ").strip()
            
            if choice == '1':
                subject = input("New subject name: ").strip()
                marks = safe_float_input(f"Marks for {subject}: ", min_val=0, max_val=100)
                student['subjects'][subject] = marks
            
            elif choice == '2':
                subject = input("Subject to update: ").strip()
                if subject in student['subjects']:
                    marks = safe_float_input(f"New marks for {subject}: ", min_val=0, max_val=100)
                    student['subjects'][subject] = marks
                else:
                    print("❌ Subject not found!")
            
            elif choice == '3':
                subject = input("Subject to remove: ").strip()
                if subject in student['subjects']:
                    del student['subjects'][subject]
                    print(f"✅ {subject} removed!")
                else:
                    print("❌ Subject not found!")
        
        print("✅ Student updated successfully!")
        display_student_details(student)
    
    except Exception as e:
        print(f"❌ Error updating student: {e}")


def delete_student():
    """Delete a student record"""
    if not students:
        print("\n📭 No students to delete!")
        return
    
    try:
        student_id = safe_int_input("\nEnter student ID to delete: ")
        
        student = next((s for s in students if s['id'] == student_id), None)
        
        if not student:
            print("❌ Student not found!")
            return
        
        display_student_details(student)
        
        if confirm_action(f"\nDelete student {student['name']}?"):
            students.remove(student)
            print("✅ Student deleted successfully!")
        else:
            print("❌ Deletion cancelled")
    
    except Exception as e:
        print(f"❌ Error deleting student: {e}")


def calculate_class_statistics():
    """Calculate and display class statistics"""
    if not students:
        print("\n📭 No students for statistics!")
        return
    
    print("\n" + "=" * 60)
    print("  📊 CLASS STATISTICS")
    print("=" * 60)
    
    # Total students
    print(f"\n  Total Students: {len(students)}")
    
    # Average age
    avg_age = sum(s['age'] for s in students) / len(students)
    print(f"  Average Age: {avg_age:.2f}")
    
    # Grade distribution
    grades = {}
    for student in students:
        grade = student['grade']
        grades[grade] = grades.get(grade, 0) + 1
    
    print(f"\n  Grade Distribution:")
    for grade, count in sorted(grades.items()):
        print(f"    {grade}: {count} students")
    
    # Subject-wise statistics
    all_subjects = {}
    for student in students:
        for subject, marks in student['subjects'].items():
            if subject not in all_subjects:
                all_subjects[subject] = []
            all_subjects[subject].append(marks)
    
    if all_subjects:
        print(f"\n  Subject-wise Average Marks:")
        for subject, marks_list in sorted(all_subjects.items()):
            avg = sum(marks_list) / len(marks_list)
            print(f"    {subject:<20} {avg:>6.2f}")
    
    # Top performer
    students_with_avg = []
    for student in students:
        if student['subjects']:
            avg = sum(student['subjects'].values()) / len(student['subjects'])
            students_with_avg.append((student, avg))
    
    if students_with_avg:
        top_student, top_avg = max(students_with_avg, key=lambda x: x[1])
        print(f"\n  🏆 Top Performer:")
        print(f"    {top_student['name']} - Average: {top_avg:.2f}")
    
    print("=" * 60)


def save_to_file():
    """Save student records to file"""
    try:
        import json
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)
        print("✅ Students saved to students.json!")
    except Exception as e:
        print(f"❌ Error saving to file: {e}")


def load_from_file():
    """Load student records from file"""
    try:
        import json
        with open("students.json", "r") as file:
            global students
            students = json.load(file)
        print(f"✅ Loaded {len(students)} students from file!")
    except FileNotFoundError:
        print("📁 No saved file found. Starting fresh!")
    except Exception as e:
        print(f"❌ Error loading from file: {e}")


def main():
    """Main function for student record system"""
    load_from_file()
    
    while True:
        print("\n" + "=" * 50)
        print("  📚 STUDENT RECORD SYSTEM")
        print("=" * 50)
        print("  1. Add Student")
        print("  2. Display All Students")
        print("  3. Search Student")
        print("  4. Update Student")
        print("  5. Delete Student")
        print("  6. Class Statistics")
        print("  7. Save to File")
        print("  8. Exit")
        print("=" * 50)
        
        try:
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                add_student()
            elif choice == '2':
                display_all_students()
            elif choice == '3':
                search_student()
            elif choice == '4':
                update_student()
            elif choice == '5':
                delete_student()
            elif choice == '6':
                calculate_class_statistics()
            elif choice == '7':
                save_to_file()
            elif choice == '8':
                save_to_file()
                print("\n👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice! Please enter 1-8")
        
        except KeyboardInterrupt:
            print("\n\n⚠️ Interrupted! Saving data...")
            save_to_file()
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()