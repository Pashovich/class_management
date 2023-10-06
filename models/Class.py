class Class:

    db = None
    def __init__(self, class_name, instructor, schedule):
        self.class_name = class_name
        self.instructor = instructor
        self.schedule = schedule
        self.students = []

    def get_class_info(self):
        return {
            "Class Name": self.class_name,
            "Instructor": self.instructor,
            "Schedule": self.schedule,
            "Enrolled Students": self.students
        }

    def create_class(self):
        Class.db["classes"].insert_one(self.get_class_info())

    def read_all_classes():
        classes = db["classes"].find()
        return [c for c in classes]