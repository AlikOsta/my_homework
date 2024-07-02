
def get_grades() :
    grades = []
    for i in range(10) :
        while True :
            try :
                grade = int(input(f"Введите оценку {i + 1} (от 1 до 12): "))
                if 1 <= grade <= 12 :
                    grades.append(grade)
                    break
                else :
                    print("Оценка должна быть в диапазоне от 1 до 12. Попробуйте еще раз.")
            except ValueError :
                print("Некорректный ввод. Пожалуйста, введите целое число.")
    return grades


def print_grades(grades, message="Оценки студента: ") :
    print(message)
    for i, grade in enumerate(grades, 1) :
        print(f"Оценка {i}: {grade}")


def retake_exam(grades) :
    while True :
        try :
            index = int(input("Введите номер оценки, которую хотите изменить (от 1 до 10): ")) - 1
            if 0 <= index < 10 :
                break
            else :
                print("Номер должен быть в диапазоне от 1 до 10. Попробуйте еще раз.")
        except ValueError :
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    while True :
        try :
            new_grade = int(input("Введите новую оценку (от 1 до 12): "))
            if 1 <= new_grade <= 12 :
                grades[index] = new_grade
                break
            else :
                print("Оценка должна быть в диапазоне от 1 до 12. Попробуйте еще раз.")
        except ValueError :
            print("Некорректный ввод. Пожалуйста, введите целое число.")


def check_scholarship(grades) :
    average_grade = sum(grades) / len(grades)
    print(f"Средний балл: {average_grade:.2f}")
    if average_grade >= 10.7 :
        print("Стипендия выходит.")
    else :
        print("Стипендия не выходит.")


def print_sorted_grades(grades) :
    sorted_grades = sorted(grades)
    print_grades(sorted_grades, "Сортировка оценок:")


def main() :
    grades = get_grades()
    print_grades(grades)
    retake_exam(grades)
    print_grades(grades)
    check_scholarship(grades)
    print_sorted_grades(grades)


main()


