from utils import get_connection, clear
from config import connection_url
from models import Class

db = get_connection(connection_url)

# db["classes"].drop()

Class.db = db['classes']



def create_class():
    class_name = input('Class Name: ')
    instructor = input('Instructor Name: ')
    schedule = input('Schedule: Day of the week and time. Monday 10:30: ')
    clear()
    searched_class = Class.get_class(class_name,instructor,schedule)
    if searched_class:
        print(f'Class with {class_name}, {instructor} and {schedule} already exists.')
        return 

    object_class = Class(
        class_name,instructor,schedule
    )
    object_class.save()
    
    print('Saved')
    
def _get_list(promt_name):
    classes = get_all_classes()
    print()
    id = input(f'{promt_name}\n')

    try:
        class_object = classes[int(id)]
    except:
        print('Choosen id not presented in the class.')
        return None
    clear()
    return class_object

def update_class():
    class_object = _get_list('Choose id to modify.')
    print('Provide fields to update:')
    class_name = input('Class Name: (Press enter to skip): ')
    instructor = input('Instructor Name: (Press enter to skip): ')
    schedule = input('Schedule: Day of the week and time. Monday 10:30 (Press enter to skip): ')

    if class_name:
        class_object.class_name = class_name
    if instructor:
        class_object.instructor = instructor
    if schedule:
        class_object.schedule = schedule

    class_object.save()
    clear()
    print('Updated')

def get_all_classes():
    classes = Class.get_all()
    print(f"{'Classname':<15} {'Instructor':<20} {'Schedule':<15} {'Id':<15}")
    for id, _class in enumerate(classes):
        print(f"{_class.class_name:<15} {_class.instructor:<20} {_class.schedule:<15} {id}")

    return classes


def delete_class():
    class_object = _get_list('Choose id to delete.')
    class_object.delete()


def enroll_students():
    class_object = _get_list('Choose id to enroll.')
    student_name = input('Student_name : ')

commands_map = {
    '1' : create_class,
    '2' : get_all_classes,
    '3' : update_class,
    '4' : delete_class,
    # '5' : view_students,
    '6' : enroll_students
    # '5' : delete_students
}

promt = "1. make class\n2. list all classes\n3. update class\n4. delete class\n"
        
        
        

while True:
    command_name = input(promt)
    func = commands_map.get(command_name, None)
    clear()
    if not func:
        print("Select from the command list")
    func()
# create_class()
get_all_classes()