# pydirecte/__init__.py

"""
pydirecte - A Python API wrapper for EcoleDirecte
"""

from .index import (
    Session,
    SessionTokenRequired,
    BadCredentials,
    DoubleAuthRequired,
    BadDoubleAuth,
    init_login,
    doubleauth_login,
    student_grades,
    student_homework,
    student_lesson,
    student_timetable,
    student_documents,
    student_vie_scolaire,
    student_cloud,
    student_message_list,
    student_message_get,
    student_message_set_read,
    student_canteen,
    Grade,
    Period,
    Subject,
    Lesson,
    Homework,
    Document,
    Attendance,
    Punishment,
    Cloud,
    Message,
)

__all__ = [
    "Session",
    "SessionTokenRequired",
    "BadCredentials",
    "DoubleAuthRequired",
    "BadDoubleAuth",
    "init_login",
    "doubleauth_login",
    "student_grades",
    "student_homework",
    "student_lesson",
    "student_timetable",
    "student_documents",
    "student_vie_scolaire",
    "student_cloud",
    "student_message_list",
    "student_message_get",
    "student_message_set_read",
    "student_canteen",
    "Grade",
    "Period",
    "Subject",
    "Lesson",
    "Homework",
    "Document",
    "Attendance",
    "Punishment",
    "Cloud",
    "Message",
]

__version__ = "1.0.0"
