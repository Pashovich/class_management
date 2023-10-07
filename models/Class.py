


class BaseModel:

    def __init__(self, collection,_to_update):
        self._to_update = _to_update
        self.collection = collection
    '''

    Attributes:
        db: A database object.
    '''
    db = None
    def get_info():
        raise NotImplementedError()
    def save(self):
        '''
        Saves the class information to the database. If the class already exists (has an _id),
        it updates the existing record; otherwise, it inserts a new record.
        '''
        if self._to_update:
            BaseModel.db[self.collection].update_one(
                {'_id' : self._id},
                {
                    '$set' : self.get_info()
                }
            )
        else:
            BaseModel.db[self.collection].insert_one(self.get_info())

    def delete(self):
        '''

        Deletes the class from the database if it has an _id. Raises an exception if the class
        object does not have an _id.
        '''
        if self._id:
            BaseModel.db.delete_one({"_id": self._id})
        else:
            raise Exception('Class object does not exists.')



class Student(BaseModel):
    collection = 'students'
    def __init__(self, name, _id = None):
        
        if BaseModel.db == None:
            raise Exception('Database object class is not provided. BaseModel.db = db_') 
        self.name = name
        self._id = _id
        to_update = False
        if self._id:
            to_update = True

        super().__init__(Student.collection,to_update)

    def get_info(self):
        return {
            'name' : self.name
        }

    @staticmethod
    def get_all():
        '''
        Static method that retrieves all class records from the database and returns them as a list
        of Class objects.
        Returns:
            list: list of Class objects.
        '''
        classes = BaseModel.db.find()
        return [Class(**c) for c in classes]

class Class(BaseModel):
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
        if BaseModel.db == None:
            raise Exception('Database object class is not provided. BaseModel.db = db_') 
        self.class_name = class_name
        self.instructor = instructor
        self.schedule = schedule
        self.students = enrolled_students
        self._id = _id
        if self._id:
            to_update = True

        super().__init__(Class.collection,to_update)

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
        the_class = BaseModel.db[Class.collection].find_one(search_pattern)
        if the_class:
            return Class(**the_class)
        else:
            return None

    @staticmethod
    def get_all():
        '''
        Static method that retrieves all class records from the database and returns them as a list
        of Class objects.
        Returns:
            list: list of Class objects.
        '''
        classes = BaseModel.db[Class.collection].find()
        return [Class(**c) for c in classes]