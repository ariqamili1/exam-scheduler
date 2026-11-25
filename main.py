from src.models import load_instance, load_timetable
from src.validator import validate_timetable


# Load the instance
instance = load_instance("data/sample_instance.json")

# Load the valid timetable
timetable = load_timetable("data/sample_valid_timetable.json")

# Validate the timetable
errors = validate_timetable(instance, timetable)

print("\n--- VALID TIMETABLE TEST ---")

if errors:
    print("Invalid timetable:")
    for error in errors:
        print("-", error)
else:
    print("Valid timetable!")


# Test the invalid instance
print("\n--- INVALID INSTANCE TEST ---")

invalid_instance = load_instance("data/sample_invalid_timetable.json")

print("Number of exams loaded:", len(invalid_instance.exams))
print("Loaded exam IDs:", list(invalid_instance.exams.keys()))