import sys


def display_first_10_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            for i in range(10):
                line = file.readline().rstrip()
                if not line:
                    break
                print(line)
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_name}' не існує.")
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python script.py <ім'я_файлу>")
    else:
        file_name = sys.argv[1]
        display_first_10_lines(file_name)
