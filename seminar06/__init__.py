import time


class Stopwatch:
    def __init__(self):  # конструктор класса
        self.start_point = None  # Время начала работы секундомера
        self.isPause = False  # Переменная, указывающая, находится ли секундомер в режиме паузы
        self.pause_point = None  # What time is paused?
        self.go_point = None  # What time is started again?
        self.stop_point = None  # What time is stopped again?
        self.isGo = False  # Is timer running?
        self.total_paused = 0  # Общее время пауз
        self.total_time = 0  # How many seconds has timer running?
        self.result = 0 # end of work of timer

    def start(self):  # запускает секундомер
        if not self.isGo and not self.isPause:  # Если секундомер еще не запущен
            self.start_point = time.time()  # Запускаем секундомер
            print(f"Timer has started at {self.start_point}")
            self.isGo = True
        else:
            return

    def pause(self):  # приостанавливает работу секундомера
        if self.isGo:  # Если секундомер запущен и не находится в режиме паузы
            self.isPause = True  # Входим в режим паузы
            self.isGo = False
            self.pause_point = time.time()  # Запоминаем время начала паузы
            if not self.go_point:
                self.total_time = self.pause_point - self.start_point
            else:
                self.total_time += self.pause_point - self.go_point

            print(f"Timer has paused at {self.pause_point}")
            print(f"Timer has run {int(self.total_time)} sec")
        else:
            return

    def go(self):  # возобновляет работу секундомера после паузы
        if self.isPause:  # Если секундомер находится в режиме паузы
            self.isPause = False  # Выходим из режима паузы
            self.isGo = True
            self.go_point = time.time()  # Fix time of the start again
            print(f"Timer has ran again at {self.go_point}")
        else:
            return

    def stopping(self) -> float:
        if not self.pause_point:
            self.total_time = self.stop_point - self.start_point
            return self.total_time
        if not self.go_point:
            self.total_time = self.pause_point - self.start_point
            return self.total_time
        else:
            self.total_time += self.stop_point - self.go_point
            return self.total_time

    def stop(self):  # останавливает секундомер и сбрасывает все переменные

        if self.isGo:
            self.stop_point = time.time()
            self.total_time = self.stopping()
            print(f"Timer has stopped at {self.stop_point}")
            print(f"Timer has run {int(self.total_time)} sec")

            self.result = self.total_time

        # Сбрасываем все переменные секундомера
        self.start_point = None  # Время начала работы секундомера
        self.isPause = False  # Переменная, указывающая, находится ли секундомер в режиме паузы
        self.pause_point = None  # What time is paused?
        self.go_point = None  # What time is started again?
        self.isGo = False  # Is timer running?
        self.total_paused = 0  # Общее время пауз
        self.total_time = 0  # How many seconds has timer running?

    def get_time(self) -> float:  # возвращает время работы секундомера в секундах
        if self.isGo or self.isPause:
            return self.total_time
        else:
            return 0

    def get_time_format(self) -> str:  # возвращает время работы секундомера в формате "минуты:секунды"
        delta_time = int(self.result)
        minutes = delta_time // 60
        sec = delta_time % 60
        return f"{minutes:02}: {sec:02}"


if __name__ == "__main__":  #
    timer = Stopwatch()

    # выводятся доступные опции управления, и пользователь выбирает одну из них.
    while True:
        print("1 - start")
        print("2 - pause")
        print("3 - continue")
        print("4 - stop")
        print("5 - exit")

        choice = input("Choose number: ")
        if choice == "1":
            timer.start()
        elif choice == "2":
            timer.pause()
        elif choice == "3":
            timer.go()
        elif choice == "4":
            timer.stop()
        elif choice == "5":
            print("Exit")
            break
    # После выхода из цикла выводится общее время работы секундомера

    print("Timer has been on for ", timer.get_time_format())
