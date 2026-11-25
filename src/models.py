import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Exam:
    id: str
    students: frozenset[str]


@dataclass(frozen=True)
class Room:
    id: str
    capacity: int


@dataclass
class Instance:
    exams: dict[str, Exam]   # exam id -> Exam
    rooms: dict[str, Room]   # room id -> Room
    slots: list[str]         # slot ids, in order


@dataclass(frozen=True)
class Assignment:
    exam: str
    slot: str
    room: str


def load_instance(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    exams = {e["id"]: Exam(e["id"], frozenset(e["students"])) for e in data["exams"]}
    rooms = {r["id"]: Room(r["id"], r["capacity"]) for r in data["rooms"]}
    return Instance(exams, rooms, data["slots"])


def load_timetable(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return [Assignment(a["exam"], a["slot"], a["room"]) for a in data]