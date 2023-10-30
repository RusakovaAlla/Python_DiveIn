"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""
import sys


def check_date():
    days_30 = [4, 6, 9, 11]
    date_parameters = ".".join(sys.argv[1:]).split(".")
    if len(date_parameters) != 3:
        print("На дату совсем не похоже (формат DD.MM.YYYY)")
    else:
        if 0 < int(date_parameters[0]) < 32 and \
                0 < int(date_parameters[1]) < 13 and \
                0 < int(date_parameters[1]) < 10_000:
            if int(date_parameters[0]) > 29 and int(date_parameters[1]) == 2 and int(date_parameters[2]) % 4 != 0:
                print("False")
            elif int(date_parameters[0]) > 30 and int(date_parameters[1]) in days_30:
                print("False")
            else:
                print("True")
        else:
            print("False")


if __name__ == "__main__":
    check_date()
