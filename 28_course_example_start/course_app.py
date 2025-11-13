# Import the class data using the data module.
from data.course_data import (
    student_data,
    assignment_data,
    submission_data
)

from tools.course import Course
from tools.assignment import Assignment
from tools.student import Student

# let's move this functionality into the class.
def add_students(course):
    for student_info in student_data:
        course.add_student(
            Student(id=student_info['id'],
                    name=student_info['name'])
        )

def add_assignments(course):
    for assignment_info in assignment_data:

        course.add_assignment(
            Assignment(id=assignment_info['id'],
                       name=assignment_info['name'])
        )


def main():
    course = Course("Dan's Engagement seminar for sleep")
    course.bulk_add_students(
        student_data=student_data
    )
    course.bulk_add_assignments(
        assignment_data=assignment_data
    )
    course.bulk_add_submissions(
        submission_data=submission_data
    )

    breakpoint()
    # add_students(course)
    # add_assignments(course)


if __name__ == "__main__":
    main()