def study_schedule(permanence_period, target_time):
    if isinstance(target_time, int):
        only_student_count = 0
        for login, logout in permanence_period:
            if not isinstance(login, int) or not isinstance(logout, int):
                return None
            if target_time >= login and target_time <= logout:
                only_student_count += 1
        return only_student_count
    else:
        return None


# permanence_period = [(2, 3), (5, 7), (1, 2), (6, 7), (5, 7), (5, 7)]

# print(study_schedule(permanence_period, 6))
