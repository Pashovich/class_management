from models import Class
from utils import clear
import re

def validate_schedule(input_string):
    pattern = r'^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) (0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$'

    match = re.match(pattern, input_string)

    if match:
        day, hours, minutes = match.groups()
        if 0 <= int(hours) <= 23 and 0 <= int(minutes) <= 59:
            return True

    return False

def create_class():
    class_name = input('Class Name: ')
    instructor = input('Instructor Name: ')
    while True:
        schedule = input('Schedule: Day of the week and time. Monday 10:30: ')
        if validate_schedule(schedule):
            break
        print("Wrong Format")
    clear()
    searched_class = Class.get_class(class_name,instructor,schedule)
    if searched_class:
        print(f'Class with {class_name}, {instructor} and {schedule} already exists.')
        return 

    object_class = Class(
        class_name,instructor,schedule
    )
    object_class.save()
    
    return "Class Saved"
    
def _get_list(promt_name, show_students = False):
    error_message = ''
    while True:
        clear()
        classes = get_all_classes(show_students = show_students)
        print()
        id = input(f'{promt_name + error_message}\n')

        try:
            class_object = classes[int(id)]
            break
        except:
            error_message = f' Choosen id : {id} not presented in the class.'
    
    return class_object

def update_class():
    class_object = _get_list('Choose id to modify.')
    print('Provide fields to update:')
    class_name = input('Class Name: (Press enter to skip): ')
    instructor = input('Instructor Name: (Press enter to skip): ')
    while True:
        schedule = input('Schedule: Day of the week and time. Monday 10:30 (Press enter to skip): ')
        if not schedule:
            break
        if validate_schedule(schedule):
            break
        print("Wrong Format")

    if class_name:
        class_object.class_name = class_name
    if instructor:
        class_object.instructor = instructor
    if schedule:
        class_object.schedule = schedule

    class_object.save()
    clear()
    return 'Class Updated'

def get_all_classes(show_students = True):
    classes = Class.get_all()
    print('Classes')
    print(f"{'Classname':<15} {'Instructor':<20} {'Schedule':<15} {'Id':<15}")
    for id, _class in enumerate(classes):
        print(f"{_class.class_name:<15} {_class.instructor:<20} {_class.schedule:<15} {id}")

    if show_students:
        while True:
            class_id = input('To show students in class type class id. Press enter to skip.')
            if class_id == '':
                return classes
            
            try:
                class_id = int(class_id)
            except:
                print('Invalid ID. Wrong type.')
                continue
            
            try:
                if class_id < 0 or class_id > len(classes):
                    print('Invalid ID. Wrong id.')
                    continue
                _class = classes[class_id]
            except:
                print('Invalid ID. Wrong id.')
                continue

            print('Students')
            print(f"{'id':<15} {'Student':<20}")
            for id,student in enumerate(_class.students):
                print(f"{id:<15} {student:<20}")
            
            break
            
    return classes


def delete_class():
    class_object = _get_list('Choose id to delete.', show_students = False)
    class_object.delete()


def enroll_students():
    class_object = _get_list('Choose class id to enroll.', show_students = False)
    print('Students')
    print(f"{'id':<15} {'Student':<20}")
    for id,student in enumerate(class_object.students):
        print(f"{id:<15} {student:<20}")
    student_name = input('Student_name : ')
    class_object.add_student(student_name)
    class_object.save()
    clear()
    return 'Student Saved'


def delete_students():
    class_object = _get_list('Choose class ID to delete.', show_students = False)
    print(f"{'id':<15} {'Student':<20}")
    for id,student in enumerate(class_object.students):
        print(f"{id:<15} {student:<20}")

    student_id = input('Student id : ')
    while True:
        try:
            student_id = int(student_id)
        except:
            print('Invalid ID. Wrong type.')
            continue
        
        try:
            if student_id < 0 or student_id > len(class_object.students):
                print('Invalid ID. Wrong id.')
                continue
            _ = class_object.students[student_id]
        except:
            print('Invalid ID. Wrong id.')
            continue

        break
    class_object.delete_student(student_id)
    class_object.save()
    clear()
    # print('Deleted')
    return 'Student Deleted'

def show_classes():
    get_all_classes()
    input('Press to continue.')

commands_map = {
    '1' : create_class,
    '2' : show_classes,
    '3' : update_class,
    '4' : delete_class,
    '5' : enroll_students,
    '6' : delete_students
}
promt = "1. Make class.\n2. List all classes\n3. Update class\n4. Delete class\n5. Enroll student\n6. Delete student\nType 'stop' to exit.\n"