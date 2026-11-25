from src.models import Assignment, Exam, Instance, Room
from src.validator import validate_timetable


def test_student_conflicts_are_reported_in_sorted_student_order():
    instance = Instance(
        exams={
            "AI": Exam("AI", frozenset({"z", "a"})),
            "Statistics": Exam("Statistics", frozenset({"z", "a"})),
        },
        rooms={
            "A": Room("A", 10),
            "B": Room("B", 10),
        },
        slots=["Mon-09:00"],
    )
    assignments = [
        Assignment("AI", "Mon-09:00", "A"),
        Assignment("Statistics", "Mon-09:00", "B"),
    ]

    errors = validate_timetable(instance, assignments)

    assert errors == [
        "Student conflict: a has exams AI and Statistics at Mon-09:00",
        "Student conflict: z has exams AI and Statistics at Mon-09:00",
    ]