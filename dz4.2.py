def get_cats_info(path):
    try:
        with open(path, "r", encoding='utf-8') as file:
            cats = list()
            data = file.readlines()
            for i in data:
                cat_data = i.strip().split(',')
                cat = {
                    'id': cat_data[0],
                    'name': cat_data[1],
                    'age': cat_data[2]
                }
                cats.append(cat)
            return cats

    except FileNotFoundError:
        print('Такого файлу не існує')
        return None


def main():
    cats_info = get_cats_info("cats.txt")
    if cats_info is not None:
        print(cats_info)
    else:
        print('Котів немає вдома')


if __name__ == '__main__':
    main()