# data.py

from pymongo import MongoClient

# === Mock Data ===

degree_plans = {
    "Computer Science": {
        "required_courses": [
            "CS101", "CS102", "CS201", "CS202", "CS301",
            "CS302", "MATH101", "MATH201", "ENG101", "HIST101"
        ],
        "credits_to_graduate": 120
    },
    "Data Science": {
        "required_courses": [
            "DS101", "DS102", "CS101", "CS102", "MATH101",
            "MATH201", "STATS101", "STATS201", "ENG101", "HIST101"
        ],
        "credits_to_graduate": 120
    }
}

student_profiles = [
    {
        "id": 1,
        "name": "Alice Smith",
        "major": "Computer Science",
        "completed_courses": ["CS101", "MATH101", "ENG101"],
        "gpa": 3.4,
        "completed_credits": 30,
        "grade_level": "Sophomore",
        "is_ncaa_athlete": True,
        "social_security_number": "123-45-67890" 
    },
    {
        "id": 2,
        "name": "Bob Johnson",
        "major": "Data Science",
        "completed_courses": ["DS101", "CS101", "ENG101"],
        "gpa": 2.1,
        "completed_credits": 30,
        "grade_level": "Sophomore",
        "is_ncaa_athlete": True,
        "social_security_number": "123-45-67891"
    },
    {
        "id": 3,
        "name": "Carla Thomas",
        "major": "Data Science",
        "completed_courses": ["DS101", "DS102", "MATH101", "STATS101", "ENG101", "CS101"],
        "gpa": 3.7,
        "completed_credits": 60,
        "grade_level": "Junior",
        "is_ncaa_athlete": False,
        "social_security_number": "123-45-67892"
    },
    {
        "id": 4,
        "name": "Daniel Lee",
        "major": "Computer Science",
        "completed_courses": ["CS101", "CS102", "CS201", "CS202", "MATH101", "MATH201", "ENG101", "HIST101"],
        "gpa": 3.2,
        "completed_credits": 90,
        "grade_level": "Senior",
        "is_ncaa_athlete": False,
        "social_security_number": "123-45-67893"
    },
    {
        "id": 5,
        "name": "Kenneth Johnson",
        "major": "Computer Science",
        "completed_courses": ["CS301", "CS101", "CS102", "CS201", "HIST101", "ENG101"],
        "gpa": 2.96,
        "completed_credits": 69,
        "grade_level": "Senior",
        "is_ncaa_athlete": True,
        "social_security_number": "397-39-2035"
    },
    {
        "id": 6,
        "name": "Alexandra Bailey",
        "major": "Computer Science",
        "completed_courses": ["CS101", "CS201", "MATH101"],
        "gpa": 2.87,
        "completed_credits": 45,
        "grade_level": "Freshman",
        "is_ncaa_athlete": False,
        "social_security_number": "643-01-8664"
    },
    {
        "id": 7,
        "name": "Samuel Jenkins",
        "major": "Data Science",
        "completed_courses": ["CS101", "MATH201", "HIST101", "STATS101"],
        "gpa": 3.53,
        "completed_credits": 41,
        "grade_level": "Sophomore",
        "is_ncaa_athlete": False,
        "social_security_number": "259-71-3131"
    },
    {
        "id": 8,
        "name": "Melissa Thompson",
        "major": "Computer Science",
        "completed_courses": ["CS101", "CS202", "CS301", "CS201"],
        "gpa": 3.92,
        "completed_credits": 70,
        "grade_level": "Senior",
        "is_ncaa_athlete": True,
        "social_security_number": "141-61-9422"
    },
    {
        "id": 9,
        "name": "Joshua Young",
        "major": "Data Science",
        "completed_courses": ["CS102", "ENG101", "DS102"],
        "gpa": 3.03,
        "completed_credits": 28,
        "grade_level": "Freshman",
        "is_ncaa_athlete": False,
        "social_security_number": "808-34-2968"
    },
    {
        "id": 10,
        "name": "Ashley Murphy",
        "major": "Computer Science",
        "completed_courses": ["CS301", "CS202", "CS101", "ENG101", "HIST101", "MATH101"],
        "gpa": 2.94,
        "completed_credits": 65,
        "grade_level": "Junior",
        "is_ncaa_athlete": False,
        "social_security_number": "857-10-6670"
    },
    {
        "id": 11,
        "name": "Kevin Simmons",
        "major": "Computer Science",
        "completed_courses": ["CS102", "CS302", "MATH101", "ENG101", "HIST101"],
        "gpa": 3.82,
        "completed_credits": 55,
        "grade_level": "Junior",
        "is_ncaa_athlete": True,
        "social_security_number": "209-20-6796"
    },
    {
        "id": 12,
        "name": "Megan Robinson",
        "major": "Data Science",
        "completed_courses": ["STATS101", "CS101", "DS101", "DS102", "ENG101"],
        "gpa": 3.34,
        "completed_credits": 48,
        "grade_level": "Sophomore",
        "is_ncaa_athlete": True,
        "social_security_number": "410-79-5213"
    },
    {
        "id": 13,
        "name": "Brian Scott",
        "major": "Data Science",
        "completed_courses": ["DS101", "DS102", "CS101", "STATS101"],
        "gpa": 2.76,
        "completed_credits": 37,
        "grade_level": "Sophomore",
        "is_ncaa_athlete": False,
        "social_security_number": "131-97-1297"
    },
    {
        "id": 14,
        "name": "Caitlyn Morgan",
        "major": "Computer Science",
        "completed_courses": ["CS301", "CS101", "CS102"],
        "gpa": 3.69,
        "completed_credits": 52,
        "grade_level": "Junior",
        "is_ncaa_athlete": True,
        "social_security_number": "137-24-1501"
    },
    {
        "id": 15,
        "name": "Tyler Adams",
        "major": "Data Science",
        "completed_courses": ["DS101", "MATH201", "ENG101"],
        "gpa": 3.45,
        "completed_credits": 42,
        "grade_level": "Junior",
        "is_ncaa_athlete": False,
        "social_security_number": "652-31-4461"
    },
    {
        "id": 16,
        "name": "Danielle Griffin",
        "major": "Computer Science",
        "completed_courses": ["CS101", "CS102", "MATH201"],
        "gpa": 2.35,
        "completed_credits": 30,
        "grade_level": "Sophomore",
        "is_ncaa_athlete": True,
        "social_security_number": "578-83-3921"
    },
    {
        "id": 17,
        "name": "Nathan Ross",
        "major": "Computer Science",
        "completed_courses": ["CS301", "MATH101", "HIST101"],
        "gpa": 3.11,
        "completed_credits": 35,
        "grade_level": "Sophomore",
        "is_ncaa_athlete": False,
        "social_security_number": "373-19-2204"
    },
    {
        "id": 18,
        "name": "Jessica Foster",
        "major": "Data Science",
        "completed_courses": ["DS102", "STATS101", "STATS201"],
        "gpa": 3.27,
        "completed_credits": 58,
        "grade_level": "Junior",
        "is_ncaa_athlete": True,
        "social_security_number": "805-64-9629"
    },
    {
        "id": 19,
        "name": "Eric Diaz",
        "major": "Computer Science",
        "completed_courses": ["CS101", "CS102", "MATH101"],
        "gpa": 2.98,
        "completed_credits": 39,
        "grade_level": "Sophomore",
        "is_ncaa_athlete": False,
        "social_security_number": "112-03-9820"
    },
    {
        "id": 20,
        "name": "Lauren Hughes",
        "major": "Data Science",
        "completed_courses": ["DS102", "STATS201", "CS101", "ENG101", "HIST101"],
        "gpa": 3.6,
        "completed_credits": 61,
        "grade_level": "Junior",
        "is_ncaa_athlete": True,
        "social_security_number": "357-61-8414"
    },
    {
        "id": 21,
        "name": "Zachary Reed",
        "major": "Computer Science",
        "completed_courses": ["CS202", "MATH201", "ENG101"],
        "gpa": 3.01,
        "completed_credits": 33,
        "grade_level": "Sophomore",
        "is_ncaa_athlete": False,
        "social_security_number": "155-32-4062"
    },
    {
        "id": 22,
        "name": "Amber Long",
        "major": "Computer Science",
        "completed_courses": ["CS301", "MATH101", "HIST101", "ENG101"],
        "gpa": 3.8,
        "completed_credits": 75,
        "grade_level": "Senior",
        "is_ncaa_athlete": True,
        "social_security_number": "654-28-1994"
    },
    {
        "id": 23,
        "name": "Justin Howard",
        "major": "Data Science",
        "completed_courses": ["DS101", "DS102", "CS102", "STATS101"],
        "gpa": 3.2,
        "completed_credits": 50,
        "grade_level": "Junior",
        "is_ncaa_athlete": False,
        "social_security_number": "460-99-3148"
    },
    {
        "id": 24,
        "name": "Rachel Bennett",
        "major": "Computer Science",
        "completed_courses": ["CS101", "CS102", "CS201"],
        "gpa": 2.88,
        "completed_credits": 40,
        "grade_level": "Sophomore",
        "is_ncaa_athlete": True,
        "social_security_number": "193-30-9317"
    },
    {
        "id": 25,
        "name": "Jordan Patterson",
        "major": "Data Science",
        "completed_courses": ["STATS201", "MATH101", "DS101", "ENG101"],
        "gpa": 3.72,
        "completed_credits": 68,
        "grade_level": "Senior",
        "is_ncaa_athlete": False,
        "social_security_number": "198-49-1056"
    }
]

current_course_offerings = {
    "Fall2025": {
        "CS102": {"credits": 3, "days": ["Mon", "Wed"], "time": "10AM"},
        "CS201": {"credits": 3, "days": ["Tue", "Thu"], "time": "1PM"},
        "MATH201": {"credits": 3, "days": ["Mon", "Wed"], "time": "2PM"},
        "HIST101": {"credits": 3, "days": ["Fri"], "time": "9AM"},
        "CS301": {"credits": 3, "days": ["Tue", "Thu"], "time": "3PM"},
        "DS102": {"credits": 3, "days": ["Mon", "Wed"], "time": "12PM"},
        "STATS101": {"credits": 3, "days": ["Tue", "Thu"], "time": "9AM"},
        "STATS201": {"credits": 3, "days": ["Fri"], "time": "1PM"},
        "CS302": {"credits": 3, "days": ["Mon", "Wed"], "time": "3PM"},
        "CS202": {"credits": 3, "days": ["Tue", "Thu"], "time": "11AM"}
    },
    "Spring2026": {
        "CS102": {"credits": 3, "days": ["Mon", "Wed"], "time": "9AM"},
        "CS201": {"credits": 3, "days": ["Tue", "Thu"], "time": "2PM"},
        "MATH201": {"credits": 3, "days": ["Tue", "Thu"], "time": "10AM"},
        "ENG101": {"credits": 3, "days": ["Mon", "Wed"], "time": "1PM"},
        "STATS101": {"credits": 3, "days": ["Tue", "Thu"], "time": "3PM"},
        "STATS201": {"credits": 3, "days": ["Mon"], "time": "4PM"},
        "DS102": {"credits": 3, "days": ["Wed"], "time": "2PM"},
        "HIST101": {"credits": 3, "days": ["Fri"], "time": "10AM"},
        "CS301": {"credits": 3, "days": ["Mon", "Wed"], "time": "11AM"},
        "CS302": {"credits": 3, "days": ["Tue", "Thu"], "time": "4PM"}
    },
    "Summer2026": {
        "CS202": {"credits": 3, "days": ["Mon", "Wed"], "time": "9AM"},
        "CS301": {"credits": 3, "days": ["Tue", "Thu"], "time": "11AM"},
        "MATH201": {"credits": 3, "days": ["Mon", "Wed"], "time": "12PM"},
        "HIST101": {"credits": 3, "days": ["Fri"], "time": "9AM"},
        "DS102": {"credits": 3, "days": ["Tue", "Thu"], "time": "10AM"},
        "STATS101": {"credits": 3, "days": ["Mon", "Wed"], "time": "1PM"},
        "STATS201": {"credits": 3, "days": ["Tue", "Thu"], "time": "2PM"},
        "CS302": {"credits": 3, "days": ["Mon", "Wed"], "time": "3PM"},
        "ENG101": {"credits": 3, "days": ["Tue", "Thu"], "time": "1PM"},
        "CS102": {"credits": 3, "days": ["Mon", "Wed"], "time": "10AM"}
    }
}

student_financial_info = {
    1: {"balance": 1000, "financial_aid": True},
    2: {"balance": 0, "financial_aid": False},
    3: {"balance": 250, "financial_aid": True},
    4: {"balance": 0, "financial_aid": True},
    5: {"balance": 0, "financial_aid": True},
    6: {"balance": 500, "financial_aid": False},
    7: {"balance": 1000, "financial_aid": False},
    8: {"balance": 0, "financial_aid": True},
    9: {"balance": 1500, "financial_aid": False},
    10: {"balance": 0, "financial_aid": True},
    11: {"balance": 0, "financial_aid": True},
    12: {"balance": 500, "financial_aid": False},
    13: {"balance": 0, "financial_aid": True},
    14: {"balance": 250, "financial_aid": False},
    15: {"balance": 0, "financial_aid": True},
    16: {"balance": 1000, "financial_aid": False},
    17: {"balance": 0, "financial_aid": True},
    18: {"balance": 0, "financial_aid": True},
    19: {"balance": 500, "financial_aid": False},
    20: {"balance": 0, "financial_aid": True},
    21: {"balance": 1500, "financial_aid": False},
    22: {"balance": 0, "financial_aid": True},
    23: {"balance": 250, "financial_aid": False},
    24: {"balance": 0, "financial_aid": True},
    25: {"balance": 0, "financial_aid": True}
}

student_academic_standing = {
    1: "Good Standing",
    2: "Probation",
    3: "Good Standing",
    4: "Good Standing",
    5: "Good Standing",
    6: "Probation",
    7: "Good Standing",
    8: "Good Standing",
    9: "Probation",
    10: "Good Standing",
    11: "Good Standing",
    12: "Probation",
    13: "Good Standing",
    14: "Good Standing",
    15: "Good Standing",
    16: "Probation",
    17: "Good Standing",
    18: "Good Standing",
    19: "Probation",
    20: "Good Standing",
    21: "Probation",
    22: "Good Standing",
    23: "Probation",
    24: "Good Standing",
    25: "Good Standing"
}

ncaa_eligibility_rules = {
    "min_gpa": 2.3,
    "min_credits_per_semester": 12,
    "progress_by_year": {
        "Freshman": 0.0,
        "Sophomore": 0.40,
        "Junior": 0.60,
        "Senior": 0.80
    }
}

# === MongoDB Connection and Upload ===

client = MongoClient("mongodb+srv://sonu:Lk$pk8s1@cluster0.tfvplte.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["college_registration"]

# Drop existing collections to avoid duplicates
db.degree_plans.drop()
db.student_profiles.drop()
db.current_course_offerings.drop()
db.student_financial_info.drop()
db.student_academic_standing.drop()
db.ncaa_eligibility_rules.drop()

# Insert documents
db.degree_plans.insert_one({"data": degree_plans})
db.student_profiles.insert_many(student_profiles)
db.current_course_offerings.insert_one({"data": current_course_offerings})

# Convert integer keys to strings for BSON
student_financial_info_str_keys = {str(k): v for k, v in student_financial_info.items()}
student_academic_standing_str_keys = {str(k): v for k, v in student_academic_standing.items()}

db.student_financial_info.insert_one({"data": student_financial_info_str_keys})
db.student_academic_standing.insert_one({"data": student_academic_standing_str_keys})
db.ncaa_eligibility_rules.insert_one(ncaa_eligibility_rules)

print("✅ Mock data stored in MongoDB exactly as in your original code.")
