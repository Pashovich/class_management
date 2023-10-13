class BaseManager:
    db_manager = None

class Class:


    collection = 'classes'
    def __init__(self, class_name, instructor, schedule, _id = None,enrolled_students = []):
        '''
        Args:
            class_name (str): The name of the class.
            instructor (str): The name of the instructor.
            schedule (str): The schedule or time slot of the class.
            _id (ObjectId or None): An optional unique identifier for the class.
            enrolled_students (list): A list of students enrolled in the class. Can be empty.

        '''
        if BaseManager.db_manager == None:
            raise Exception('Database object class is not provided. BaseModel.db_manager = db_manager') 
        self.class_name = class_name
        self.instructor = instructor
        self.schedule = schedule
        self.students = enrolled_students
        self._id = _id
        self._to_update = False
        if self._id:
            self._to_update = True

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, id):
        self.students.pop(id)

    def get_info(self):
        '''
        Returns:
            dict: A dictionary with class info.
        '''
        return {
            "class_name": self.class_name,
            "instructor": self.instructor,
            "schedule": self.schedule,
            "enrolled_students": self.students
        }

    @staticmethod
    def get_class(class_name = None, instructor = None, schedule = None):
        '''
        Static method that retrieves a class by its name from the database and returns it as a Class
            object. Returns None if the class does not exist.
        Returns:
            object : Class
        '''

        search_pattern = {
            'class_name' : class_name,
            'instructor' : instructor,
            'schedule' : schedule
        }
        search_pattern = {key:value for key,value in search_pattern.items() if value}
        the_class = BaseManager.db_manager[Class.collection].find_one(search_pattern)
        if the_class:
            return Class(**the_class)
        else:
            return None


    def save(self):
        '''
        Saves the class information to the database. If the class already exists (has an _id),
        it updates the existing record; otherwise, it inserts a new record.
        '''
        if self._to_update:
            BaseManager.db_manager[Class.collection].update_one(
                {'_id' : self._id},
                {
                    '$set' : self.get_info()
                }
            )
        else:
            BaseManager.db_manager[Class.collection].insert_one(self.get_info())

    def delete(self):
        '''

        Deletes the class from the database if it has an _id. Raises an exception if the class
        object does not have an _id.
        '''
        if self._id:
            BaseManager.db_manager[Class.collection].delete_one({"_id": self._id})
        else:
            raise Exception('Class object does not exists.')

    @staticmethod
    def get_all():
        '''
        Static method that retrieves all class records from the database and returns them as a list
        of Class objects.
        Returns:
            list: list of Class objects.
        '''
        classes = BaseManager.db_manager[Class.collection].find()
        return [Class(**c) for c in classes]