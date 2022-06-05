import tool


course = tool.get_course_info("cs233", "70586")

course2 = tool.get_course_info("cs225", "62137")

print(tool.is_valid_course(course))
print(tool.is_valid_course(course2))
