"""Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список."""

from datetime import datetime

card = 0  # начальная сумма
oper_num = 0  # считаем операции
percent_withdraw = 0.015
percent_add = 0.03
rich_tax = 0.1




def check_sum():
    """
    проверяем возможность ввода
    :param oper_sum: желаемая пользователем сумма операции
    :return:
    """
    oper_sum = None
    while oper_sum is None:
        try:
            oper_sum = int(input("Сумма операции, кратную 50 рублям"))
            if oper_sum % 50 == 0:
                return oper_sum
            else:
                raise ValueError
        except ValueError:
            oper_sum = None
            print(f"Введенная сумма не кратна 50 рублям. Повторите ввод")
            continue
        except TypeError:  # на случай, если у банкомата есть qwerty-клавиатура
            print(f"Допустимо вводить только числа. Повторите ввод")
            continue
    return oper_sum



def check_riches(money: float, marker=False):
    """
    Проверим сумму счета на налог на богатство
    :param money: сумма для проверки
    :param marker: отметка для вывода информации об удержании налога
    :return:
    """
    if money > 5_000_000:
        marker = True
        money *= (1-rich_tax)
    else:
        pass

    return money, marker

def end_session():
    print("Спасибо, что пользуетесь нашими услугами. Всего доброго!")
    exit()


class MyCard:
    """
    операции со счетом клиента в банке
    """

    def __init__(self, money: float):
        """
        Открываем счет
        :param money: начальная сумма при открытии счета
        :return:
        """
        self.operation_list = []
        self.oper_num = 0
        self.money = money

    def balance(self):
        print(f"На вашем счету {self.money}")

    def billing(self):
        print(f"Последние 5 операций:")
        if len(self.operation_list) >= 5:
            print(*(i for i in self.operation_list[:-5:-1]), sep='\n')
        else:
            print(*(i for i in self.operation_list[::-1]), sep='\n')

    def add(self) -> None:
        self.money, operation = check_riches(self.money)
        if operation:
            self.operation_list.append(f"{datetime.now()}, удержание налога на богатство {rich_tax * 100}%")
        add_money = check_sum()
        self.money += add_money
        self.operation_list.append(f"{datetime.now()}, пополнение счета на сумму {add_money}")
        self.oper_num += 1
        if self.oper_num % 3 == 0:
            self.money *= (1 + percent_add)
            self.operation_list.append(f"{datetime.now()}, начислено {percent_add * 100}% "
                                       f"на остаток за пользование счетом")
            print(f"Вам начислено 3% процента за количество операций - {self.oper_num} ")

    def withdraw(self) -> None:
        self.money, operation = check_riches(self.money)
        if operation:
            self.operation_list.append(f"{datetime.now()}, удержание налога на богатство {rich_tax * 100}%")
        w4w = None
        wd = None
        while wd is None or wd > self.money:
            wd = check_sum()
            if wd > self.money:
                print("Нельзя снять больше, чем есть на счете. Повторите ввод")
                self.operation_list.append(f"{datetime.now()}, попытка снятия - {wd}. "
                                           f"Отмена: остаток по счету меньше")
                continue
            if wd == 0:
                break
        if wd * percent_withdraw < 30:
            w4w = 30
            self.money -= w4w
            self.money -= wd
        elif wd * percent_withdraw > 600:
            w4w = 600
            self.money -= w4w
            self.money -= wd
        else:
            self.money -= wd * percent_withdraw
        self.operation_list.append(f"{datetime.now()}, снятие средств - {wd}")
        self.operation_list.append(f"{datetime.now()}, комиссия за снятие средств - {w4w}")
        self.oper_num += 1
        if self.oper_num % 3 == 0:
            self.money *= (1 + percent_add)
            self.operation_list.append(f"{datetime.now()}, начислено {percent_withdraw * 100}% "
                                       f"на остаток за пользование счетом")
            print(f"Вам начислено 3% процента за количество операций - {self.oper_num} ")


def menu(num_oper=0, action=None, card_input=None):
    while True:
        if card_input is None:
            print("Карта повреждена. Обратитесь в ближайшее отделение банка")
            end_session()
        if num_oper == 0:
            print("Добро пожаловать! Выберите действие")
        else:
            print("Продолжить? Выберите действие")
        while action is None:
            try:
                action = int(input("1 - пополнить счет\n"
                        "2 - снятие средств\n"
                        "3 - запрос баланса\n"
                        "4 - биллинг\n"
                        "5 - вернуть карту\n"))
            except TypeError:
                print("Ошибка ввода. Повторите")
                action = None
                continue
            num_oper += 1
            if 6 > action > 0:
                pass
            else:
                action = None
                print("Выбрана несуществующая операция. Повторите ввод")
                continue
        if action == 1:
            card_input.add()
        elif action == 2:
            card_input.withdraw()
        elif action == 3:
            card_input.balance()
        elif action == 4:
            card_input.billing()
        else:
            end_session()
        action = None


if __name__ == '__main__':
    userCard = MyCard(money=0)
    menu(card_input=userCard)
