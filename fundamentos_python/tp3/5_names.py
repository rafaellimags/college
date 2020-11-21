print('\nPara sair, digite "Sair"\n')


class Student:
    name = '',
    height = 0


def create_student():
    students = []
    cent = 100

    while True:
        student = Student()
        student.name = input('Nome: ')
        if student.name == 'sair':
            break
        student.height = int(input('Altura: ')) / cent
        print('')
        students.append(student)

    return students


def show_results(students):
    print('')
    for student in students:
        str_height = str(student.height)
        fromat_height = str_height.replace('.', ',')
        print(f'{student.name} - {fromat_height}m')


def calc_avg_height(students):
    sum_heights = 0
    amount_of_students = 0

    for student in students:
        sum_heights += student.height
        amount_of_students += 1

    avg_height = sum_heights / amount_of_students

    print(f'\nAltura média: {avg_height}')

    return avg_height


def check_hight_abv_avg(all_students, avg):
    for student in all_students:
        if student.height > avg:
            print(f'\nAcima da média: {student.name} {student.height}\n')


def init():
    all_students = create_student()

    show_results(all_students)

    avg = calc_avg_height(all_students)

    check_hight_abv_avg(all_students, avg)


init()
