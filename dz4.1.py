def total_salary(path):
    try:
        with open(path, "r", encoding='utf-8') as file:
            salaries = list()
            data = file.readlines()
            for i in data:
                i = i.strip().split(',')
                salaries.append(int(i[1]))

            total = 0
            for i in salaries:
                total += i

            average = int(total / len(salaries))

            return total, average
    except FileNotFoundError:
        print('Такого файлу не існує')
        return None, None


def main():
    total, average = total_salary('text.txt')
    if total is not None:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

r
if __name__ == '__main__':
    main()
