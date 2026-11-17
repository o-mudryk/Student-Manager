print('''===== МЕНЕДЖЕР СТУДЕНТІВ =====

1. Додати студента
2. Додати оцінку студенту
3. Видалити студента
4. Показати всіх студентів
5. Показати середній балл студента
6. Знайти кращого студента
7. Сортувати студентів за середнім баллом
0. Вихіж
''')
students = {}
def average_mar(student):
                    average = students[student]
                    if not average:
                        print("У студента поки немає оцінок!")
                        return None
                    average_mark = sum(average)/len(average)
                    average_mark = round(average_mark, 2)
                    return average_mark
def option_var(option):
    if option == 1:
        while True:
            try:
                new_student = input(("Введіть ім'я та прізвище студента: "))
                if new_student.strip().capitalize() == "":
                    raise ValueError
                student_marks = []
                new_student = new_student.strip().capitalize()
                while new_student in students:
                    new_student = input("Цей студент вже є в базі данних, введіть нового: ")
                    new_student = new_student.capitalize()
                while True:
                        try:
                            numb = int(input("Скільки у нього оцінок? "))
                        except ValueError:
                            print("введіть кількість оцінок! ")
                        while True:
                            for i in range (1, numb + 1):
                                while True:
                                    try:
                                        new_mark = int(input("введіть його оцінку(1-100): "))
                                        if new_mark < 1 or new_mark > 100:
                                            new_mark = int(input("Оцінка лише від 1 до 100!! "))
                                            continue
                                        student_marks.append(new_mark)
                                        break
                                    except:
                                        print("Введіть число! ")               
                            break
                        students[new_student] = student_marks
                        break
            except ValueError:
                print("Введіть ім'я та прізвище!")
                        
            break
        return students





    elif option == 2:
        while True:
            try:
                student_name = input("Введіть студента, як він записаний в базі данних: ")
                student_name = student_name.strip().capitalize()
                if student_name.strip() == "":
                    raise ValueError
                while student_name not in students:
                    student_name = input(("Такого студента не існує! Введіть як він записанний в базі данних. "))
                    student_name = student_name.strip().capitalize()
                while True:
                    try:
                        new_markk = int(input("Введіть нову оцінку(1-100): "))
                        if new_markk < 1 or new_markk > 100:
                            new_markk = int(input("Введіть оцінку(1-100): "))
                            continue
                        students[student_name].append(new_markk)
                        break
                    except ValueError:
                        print("Введіть оцінку в межах від 1 до 100 включно! ")
                    
                return students
            except ValueError:
                print("Введіть Студента!")
    elif option == 3:
        while True:
            try:
                student = input("введіть студента, якого треба прибрати: ")
                student = student.strip().capitalize()
                if student == "":
                    raise ValueError
                while student not in students:
                    student = input(("Такого студента не існує! Введіть як він записанний в базі данних. "))
                    student = student.strip().capitalize()
                print("Студента успішно видалено!")
                students.pop(student)
                break
            except ValueError:
                print("введіть студента як він записан в базі данних: ")
            return students
    elif option == 4:
        while True:
            if not students:
                print("В базі данних немає студентів, спочатку додайте їх!")
                break
            else:
                mainup = "СТУДЕНТИ"
                print(mainup.rjust(17, "=") + "=" * 9)
                for name, marks in students.items():
                    print(f"{name}: {', '.join(map(str, marks))}")
                print("=" * 27) 
                break       
    elif option == 5:

        while True:
            try:
                student = input("Введіть студента, для визначення його середнього баллу: ")
                student = student.strip().capitalize()
                if student == "":
                    raise ValueError
                while student not in students:
                    student = input(("Такого студента не існує! Введіть як він записанний в базі данних. "))
                    student = student.strip().capitalize()
                average_mar(student)
                average_mark = average_mar(student)

                if average_mark is None:
                    print("У цього студента поки що немає оцінок.")
                else:
                    print(f"Середній бал: {average_mark}")
                break
            except ValueError:
                print("Введіть Студента!")
        
    elif option == 6:
        all_averages = {}
        for student, mark in students.items():
            i = average_mar(student)
            if i is not None:
                all_averages[student] = i
        if not all_averages:
            print("Немає студентів з оцінками! ")
        else:
            max_mark = max(all_averages.items(), key = lambda item: item[1])
            name, mark = max_mark
            print(f'Найкращий студент: {name} \nСередній балл: {mark}')
    elif option == 7:
        all_averages = {}

        for student, mark in students.items():
            average = average_mar(student)

            if average is not None:
                all_averages[student] = average

        if not all_averages:
            print("Немає студентів з оцінками!")
        else:
            sorted_students = sorted(
                all_averages.items(),
                key=lambda item: item[1],
                reverse=True
            )

            print("Студенти за середнім балом:")

            for student, average in sorted_students:
                print(f"{student}: {average:.2f}")
    
    

while True:
    try:
        option = int(input("Введіть ваш вибір: "))     
        if option == 0:
            print("Завершення програми. ")
            break
        option_var(option)

    except:
        print("Введіть число!")

