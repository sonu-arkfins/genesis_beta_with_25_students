import streamlit as st
from pymongo import MongoClient
import datetime
from typing import List, Dict
from encryption_utils import encrypt_ssn, decrypt_ssn, mask_ssn

# === MongoDB Connection and Data Load ===
client = MongoClient("mongodb+srv://sonu:Lk$pk8s1@cluster0.tfvplte.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["college_registration"]

degree_plans = db.degree_plans.find_one()["data"]
student_profiles = list(db.student_profiles.find({}))
current_course_offerings = db.current_course_offerings.find_one()["data"]
student_financial_info = db.student_financial_info.find_one()["data"]
student_academic_standing = db.student_academic_standing.find_one()["data"]
ncaa_eligibility_rules = db.ncaa_eligibility_rules.find_one()
social_security_number = db.social_security_number.find_one()

# === Core Functions ===
def get_remaining_courses(student, plan):
    required = set(plan["required_courses"])
    completed = set(student["completed_courses"])
    return list(required - completed)

def generate_schedule_options(remaining_courses: List[str], offerings: Dict, max_credits=12):
    options = []
    course_list = list(offerings.items())

    def backtrack(schedule=[], total_credits=0, index=0):
        if total_credits >= max_credits or index >= len(course_list):
            if schedule:
                options.append(schedule.copy())
            return

        for i in range(index, len(course_list)):
            course, meta = course_list[i]
            if course in remaining_courses and course not in [c[0] for c in schedule]:
                if total_credits + meta["credits"] <= max_credits:
                    schedule.append((course, meta))
                    backtrack(schedule, total_credits + meta["credits"], i + 1)
                    schedule.pop()

    backtrack()
    return options[:4]

def forecast_graduation(student, credits_per_semester=15):
    plan = degree_plans[student["major"]]
    remaining = plan["credits_to_graduate"] - student["completed_credits"]
    semesters_needed = (remaining + credits_per_semester - 1) // credits_per_semester
    current_year = datetime.datetime.now().year
    current_sem = "Fall" if datetime.datetime.now().month < 6 else "Spring"
    grad_sem = "Spring" if (current_sem == "Fall" and semesters_needed % 2 == 1) else "Fall"
    grad_year = current_year + (semesters_needed // 2) + (1 if grad_sem == "Spring" else 0)
    return f"{grad_sem} {grad_year}"

def full_graduation_path(student, all_offerings, max_credits_per_term=15):
    completed = set(student["completed_courses"])
    major = student["major"]
    required_courses = set(degree_plans[major]["required_courses"])
    credits_needed = degree_plans[major]["credits_to_graduate"] - student["completed_credits"]
    path = []
    credits_so_far = student["completed_credits"]

    upcoming_terms = sorted(all_offerings.keys())
    future_courses = list(required_courses - completed)

    while credits_so_far < degree_plans[major]["credits_to_graduate"]:
        term_added = False
        for term in upcoming_terms:
            term_schedule = []
            total_credits = 0
            for course in all_offerings[term]:
                if course in future_courses and total_credits < max_credits_per_term:
                    meta = all_offerings[term][course]
                    if course not in completed:
                        term_schedule.append((course, meta))
                        total_credits += meta["credits"]
                        completed.add(course)
                        future_courses.remove(course)
                if total_credits >= max_credits_per_term:
                    break
            if term_schedule:
                path.append((term, term_schedule, total_credits))
                credits_so_far += total_credits
                term_added = True
        if not term_added:
            break
    return path

def check_ncaa_eligibility(student, selected_schedule):
    if not student.get("is_ncaa_athlete"):
        return True, "Not an NCAA athlete — eligibility not required."
    min_gpa = ncaa_eligibility_rules["min_gpa"]
    min_credits = ncaa_eligibility_rules["min_credits_per_semester"]
    progress_required = ncaa_eligibility_rules["progress_by_year"][student["grade_level"]]
    actual_progress = student["completed_credits"] / degree_plans[student["major"]]["credits_to_graduate"]
    schedule_credits = sum(meta["credits"] for _, meta in selected_schedule)
    if student["gpa"] < min_gpa:
        return False, f"GPA too low ({student['gpa']:.2f}) — must be ≥ {min_gpa}"
    if schedule_credits < min_credits:
        return False, f"Schedule does not meet full-time requirement (only {schedule_credits} credits)"
    if actual_progress < progress_required:
        return False, f"Insufficient progress toward degree ({actual_progress:.0%}) — required: {progress_required:.0%}"
    return True, "Meets all NCAA requirements ✅"

def register_for_classes(student_id: int, selected_schedule: List[str]):
    st.success(f"✅ Student {student_id} successfully registered for:")
    for course, meta in selected_schedule:
        st.write(f"  - {course} on {meta['days']} at {meta['time']} ({meta['credits']} credits)")

# === Streamlit App ===
def main():
    st.title("📘 College Registration System")

    # Student selection
    student_ids = [s["id"] for s in student_profiles]
    student_id = st.selectbox("Select your Student ID", student_ids)
    student = next((s for s in student_profiles if s["id"] == student_id), None)

    if not student:
        st.error("❌ Invalid student ID.")
        return

    major = student["major"]
    plan = degree_plans[major]

    # Display student information
    st.subheader(f"Welcome {student['name']}!")
    st.write(f"*Major*: {major}")
    st.write(f"*Academic Standing*: {student_academic_standing[str(student_id)]}")
    st.write(f"*Financial Balance*: ${student_financial_info[str(student_id)]['balance']}")
    st.write(f"*GPA*: {student['gpa']:.2f}")
    st.write(f"*NCAA Athlete*: {'Yes' if student['is_ncaa_athlete'] else 'No'}")
    ssn_plain = student.get('social_security_number', 'Hidden')
    if ssn_plain != 'Hidden':
        encrypted_ssn = encrypt_ssn(ssn_plain)
        decrypted_ssn = decrypt_ssn(encrypted_ssn)
        masked_ssn = mask_ssn(decrypted_ssn)
    else:
        encrypted_ssn = 'Hidden'
        decrypted_ssn = 'Hidden'
        masked_ssn = 'Hidden'
    st.write(f"*SSN (Plain)*: {decrypted_ssn}")
    st.write(f"*SSN (Encrypted)*: {encrypted_ssn}")
    st.write(f"*SSN (Masked)*: {masked_ssn}")

    # Display remaining courses
    remaining = get_remaining_courses(student, plan)
    st.subheader("Remaining Courses to Graduate")
    st.write(", ".join(remaining) if remaining else "None")

    # Semester selection
    st.subheader("📅 Available Semesters")
    semester_names = list(current_course_offerings.keys())
    semester_choice = st.selectbox("Choose a semester to register for", semester_names)
    offerings = current_course_offerings[semester_choice]

    # Generate and display schedule options
    options = generate_schedule_options(remaining, offerings)
    st.subheader(f"📚 Schedule Options for {semester_choice}")
    if not options:
        st.warning("⚠ No available schedule options for this semester.")
        return

    option_strings = []
    for i, option in enumerate(options):
        total_credits = sum(meta["credits"] for _, meta in option)
        option_text = f"Option {i + 1}: ({total_credits} credits)\n"
        for course, meta in option:
            option_text += f"  {course}: {meta['days']} @ {meta['time']} ({meta['credits']} credits)\n"
        option_strings.append(option_text)

    selected_option = st.selectbox("Select a schedule option", option_strings, format_func=lambda x: x.split("\n")[0])
    selected_index = option_strings.index(selected_option)
    selected_schedule = options[selected_index]

    # Display graduation forecast
    forecast = forecast_graduation(student)
    st.subheader("🎓 Basic Forecasted Graduation")
    st.write(forecast)

    # Display full graduation path
    st.subheader("📈 Full Forecasted Graduation Plan (by semester)")
    grad_path = full_graduation_path(student, current_course_offerings)
    for term, courses, total_credits in grad_path:
        st.write(f"{term}** ({total_credits} credits):")
        for course, meta in courses:
            st.write(f"  {course}: {meta['days']} @ {meta['time']} ({meta['credits']} credits)")
    final_term = grad_path[-1][0] if grad_path else "Unknown"
    st.write(f"*Estimated Final Graduation Term*: {final_term}")

    # NCAA eligibility check and registration
    if st.button("Register for Selected Schedule"):
        eligible, reason = check_ncaa_eligibility(student, selected_schedule)
        st.subheader("📋 NCAA Eligibility Check")
        st.write(reason)
        if eligible:
            register_for_classes(student_id, selected_schedule)
        else:
            st.error("⛔ Registration blocked due to NCAA ineligibility.")

# ...existing code...
if __name__ == "__main__":
    main()
# ...existing code...