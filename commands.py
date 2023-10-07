from models import Class

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
    
def _get_list(promt_name, show_students = False):
    classes = get_all_classes(show_students = show_students)
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

def get_all_classes(show_students = True):
    classes = Class.get_all()
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
    print(f"{'id':<15} {'Student':<20}")
    for id,student in enumerate(class_object.students):
        print(f"{id:<15} {student:<20}")
    student_name = input('Student_name : ')
    class_object.add_student(student_name)
    class_object.save()
    clear()
    print('Saved')
    return 


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
    print('Deleted')

commands_map = {
    '1' : create_class,
    '2' : get_all_classes,
    '3' : update_class,
    '4' : delete_class,
    '5' : enroll_students,
    '6' : delete_students
}
promt = "1. Make class.\n2. List all classes\n3. Update class\n4. Delete class\n5. Enroll student\n6. Delete student\nType 'stop' to exit.\n"