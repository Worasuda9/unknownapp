#!/usr/bin/env python3
"""
Python equivalent of the "View Course Catalog" feature from the Java Course Enrollment System.
This script displays the course catalog in a formatted table.
"""

class TimeSlot:
    def __init__(self, days, start_time, end_time):
        self.days = days
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.days} {self.start_time}-{self.end_time}"

class Course:
    def __init__(self, code, title, credits, capacity, time_slot, prerequisites=None):
        self.code = code
        self.title = title
        self.credits = credits
        self.capacity = capacity
        self.time_slot = time_slot
        self.prerequisites = prerequisites or []
        self.enrolled_students = []  # For consistency, though not used in view

    def get_enrollment_count(self):
        return len(self.enrolled_students)

    def is_full(self):
        return self.get_enrollment_count() >= self.capacity

    def __str__(self):
        prereq_str = ", ".join(self.prerequisites) if self.prerequisites else "None"
        time_str = str(self.time_slot) if self.time_slot else "TBA"
        return (f"{self.code:<10} {self.title:<40} Credits: {self.credits}  "
                f"Capacity: {self.get_enrollment_count()}/{self.capacity}  "
                f"Time: {time_str:<18}  Prerequisites: {prereq_str}")

def view_course_catalog(courses):
    print("=" * 70)
    print("  COURSE CATALOG")
    print("=" * 70)
    if not courses:
        print("  No courses available.")
        return
    print(f"  {'Code':<10} {'Title':<40} {'Credits':<8} {'Seats':<12} {'Time':<18} {'Prerequisites'}")
    print("  " + "-" * 70)
    for course in courses:
        print(f"  {course}")

def main():
    # Sample courses equivalent to the Java seed data
    courses = [
        Course("CS101", "Intro to Programming", 3, 30, TimeSlot("MWF", "09:00", "10:00")),
        Course("CS201", "Data Structures", 3, 25, TimeSlot("MWF", "10:00", "11:00"), ["CS101"]),
        Course("CS301", "Algorithms", 3, 25, TimeSlot("TTh", "09:00", "10:30")),
        Course("CS401", "Operating Systems", 3, 20, TimeSlot("TTh", "10:30", "12:00")),
        Course("MATH101", "Calculus I", 4, 35, TimeSlot("MWF", "08:00", "09:00")),
        Course("MATH201", "Calculus II", 4, 30, TimeSlot("MWF", "11:00", "12:00")),
        Course("ENG101", "Technical Writing", 2, 40, TimeSlot("TTh", "13:00", "14:00")),
        Course("NET101", "Computer Networks", 3, 25, TimeSlot("MWF", "14:00", "15:00")),
        Course("DB101", "Database Systems", 3, 25, TimeSlot("TTh", "14:00", "15:30")),
        Course("SE101", "Software Engineering", 3, 30, TimeSlot("MWF", "15:00", "16:00")),
    ]

    view_course_catalog(courses)

if __name__ == "__main__":
    main()