from collections import defaultdict


def validate_timetable(instance, assignments):
    errors = []

    assigned_exams = set()
    student_schedule = defaultdict(list)
    room_schedule = {}

    for assignment in assignments:
        exam_id = assignment.exam
        slot_id = assignment.slot
        room_id = assignment.room

        # 1. Check whether the exam exists
        if exam_id not in instance.exams:
            errors.append(f"Unknown exam: {exam_id}")
            continue

        # 2. Check for duplicate exam assignments
        if exam_id in assigned_exams:
            errors.append(f"Duplicate assignment for exam: {exam_id}")
            continue

        assigned_exams.add(exam_id)
        exam = instance.exams[exam_id]

        # 3. Check whether the time slot exists
        if slot_id not in instance.slots:
            errors.append(
                f"Invalid time slot '{slot_id}' for exam {exam_id}"
            )
            continue

        # 4. Check whether the room exists
        if room_id not in instance.rooms:
            errors.append(
                f"Unknown room '{room_id}' for exam {exam_id}"
            )
            continue

        room = instance.rooms[room_id]

        # 5. Check room capacity
        if room.capacity < len(exam.students):
            errors.append(
                f"Insufficient capacity in room {room_id} "
                f"for exam {exam_id}: "
                f"{len(exam.students)} students, "
                f"capacity {room.capacity}"
            )

        # 6. Check room conflicts
        room_key = (slot_id, room_id)

        if room_key in room_schedule:
            errors.append(
                f"Room conflict: room {room_id} in {slot_id} "
                f"is used by {room_schedule[room_key]} and {exam_id}"
            )
        else:
            room_schedule[room_key] = exam_id

        # 7. Check student conflicts
        for student in sorted(exam.students):
            for previous_exam in student_schedule[(student, slot_id)]:
                errors.append(
                    f"Student conflict: {student} has exams "
                    f"{previous_exam} and {exam_id} "
                    f"at {slot_id}"
                )

            student_schedule[(student, slot_id)].append(exam_id)

    # 8. Check for missing exams
    missing_exams = set(instance.exams.keys()) - assigned_exams

    for exam_id in sorted(missing_exams):
        errors.append(f"Missing exam: {exam_id}")

    return errors