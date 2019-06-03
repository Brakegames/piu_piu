import random
from tkinter import *
import time


class MainClass:

    def __init__(self):

        self.main_window = Tk()
        self.main_window.title("Piu Piu")

        self.main_window.resizable(width=False, height=False)
        self.main_window.geometry('640x100')

        position_right = int(self.main_window.winfo_screenwidth() / 2 - 320)
        position_down = int(self.main_window.winfo_screenheight() / 2 - 50)
        self.main_window.geometry("+{}+{}".format(position_right, position_down))

        self.task_window = None
        self.start_label = None

        self.current_task = 0
        self.repeat_counter = 0

        self.is_answered = True
        self.is_right_answer = False
        self.is_left_answer = False
        self.start_time = None
        self.is_fixed_time = False
        self.is_task_end = False

        self.current_series = None

        self.result_file = None

        self.fio = ""

        self.training_button = None
        self.series_1_button = None
        self.series_2_button = None
        self.series_3_button = None
        self.series_4_button = None

        self.instruction_1 = "Вам необходимо реагировать на звуки, которые вы услышите. Нажатием кнопки влево, если звук низкий и кнопки вправо, если высокий. При этом, вам необходимо читать текст, который вы будете видеть на мониторе."
        self.instruction_2 = "Вам необходимо реагировать на звуки, которые вы услышите. Нажатием кнопки влево, если звук низкий и кнопки вправо, если высокий. При этом, вам необходимо читать текст, который вы будете видеть на мониторе."
        self.instruction_3 = "Вам необходимо реагировать на звуки, которые вы услышите. Нажатием кнопки влево, если звук низкий и кнопки вправо, если высокий. При этом, вам необходимо решить задачу, которую вы увидите на экране. Задание продлится до тех пор, пока вы не найдете верное решение задачи. Свои догадки и комментарии вы можете озвучивать экспериментатору."

        self.task_1 = "Девушка имеет четыре части цепи. Каждая часть состоит из трех звеньев. Необходимо сомкнуть звенья в замкнутую цепь (как ожерелье). Открыть звено стоит 2 цента, замкнуть - 3 цента. Она имеет только 15 центов. Как это сделать?"
        self.task_2 = "Необходимо организовать 6 одинаковых карандашей, таким образом, чтобы получилось 4 одинаковых треугольника, стороны которого равны."
        self.task_3 = "Эвкалипты нравятся Салли Лу больше, чем сосны. Она любит электрическое освещение и не любит сидеть при свечах. Люди эксцентричные вызывают у нее больше симпатий, чем уравновешенные. Как вы думаете, кто Салли Лу по профессии - экономист или бухгалтер?"
        self.task_4 = "Кирилл провел три дня в больнице. Он не был болен и не получил травму, но во время выписки его пришлось нести. Почему?"

    def run(self):

        fio_label = Label(self.main_window, text="ФИО")
        fio_label.place(x=14, y=14)

        fio_var = StringVar()
        fio_var.trace("w", lambda name, index, mode, sv=fio_var: self.on_fio_entry(sv))

        fio_input = Entry(self.main_window, textvariable=fio_var)
        fio_input.place(x=64, y=14, width=562)

        self.training_button = Button(self.main_window, text="Тренировка", command=self.on_training_button)
        self.training_button.place(x=14, y=50, width=100)
        self.training_button.config(state="disabled")

        self.series_1_button = Button(self.main_window, text="Серия 1", command=self.on_series_1_button)
        self.series_1_button.place(x=142, y=50, width=100)
        self.series_1_button.config(state="disabled")

        self.series_2_button = Button(self.main_window, text="Серия 2", command=self.on_series_1_button)
        self.series_2_button.place(x=270, y=50, width=100)
        self.series_2_button.config(state="disabled")

        self.series_3_button = Button(self.main_window, text="Серия 3", command=self.on_series_1_button)
        self.series_3_button.place(x=398, y=50, width=100)
        self.series_3_button.config(state="disabled")

        self.series_4_button = Button(self.main_window, text="Серия 4", command=self.on_series_1_button)
        self.series_4_button.place(x=526, y=50, width=100)
        self.series_4_button.config(state="disabled")

        self.main_window.mainloop()

    def on_fio_entry(self, sv):

        if len(sv.get()) == 0:
            self.training_button.config(state="disabled")
            self.series_1_button.config(state="disabled")
            self.series_2_button.config(state="disabled")
            self.series_3_button.config(state="disabled")
            self.series_4_button.config(state="disabled")
        else:
            self.fio = sv.get()
            self.training_button.config(state="normal")
            self.series_1_button.config(state="normal")
            self.series_2_button.config(state="normal")
            self.series_3_button.config(state="normal")
            self.series_4_button.config(state="normal")

    def init_task_window(self):

        self.task_window = Tk()
        self.task_window.title("Task")

        self.task_window.resizable(width=False, height=False)
        self.task_window.geometry('640x480')

        position_right = int(self.task_window.winfo_screenwidth() / 2 - 320)
        position_down = int(self.task_window.winfo_screenheight() / 2 - 240)
        self.task_window.geometry("+{}+{}".format(position_right, position_down))

        self.task_window.bind("<Right>", self.on_right_button)
        self.task_window.bind("<Left>", self.on_left_button)

        self.start_label = Label(self.task_window, text="Нажмите пробел чтобы начать")
        self.start_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    def on_training_button(self):

        self.init_task_window()

        self.result_file = open("{}_training.txt".format(self.fio), "w+")

        self.current_series = self.start_training
        self.task_window.bind("<space>", self.start_training)

    def start_training(self, event=None):

        _list = self.task_window.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        for item in _list:
            item.pack_forget()

        self.task_window.unbind("<space>")
        if self.current_task == 0:
            instruction = Message(self.task_window, text=self.instruction_1)
            instruction.place(x=20, y=20, width=600, height=440)
            self.task_window.bind("<space>", self.start_training)
            self.current_task += 1
        elif self.current_task == 1:
            self.is_fixed_time = False

            canvas = Canvas(self.task_window)
            canvas.create_rectangle(318, 220, 322, 260, fill="black")
            canvas.create_rectangle(300, 238, 340, 242, fill="black")

            canvas.pack(fill=BOTH, expand=1)

            self.repeat_counter = 40
            self.task_window.after(random.randint(1000, 2000), self.random_two_keys)

        elif self.current_task == 2:
            self.result_file.write("--------------------------\r\n")
            instruction = Message(self.task_window, text=self.instruction_2)
            instruction.place(x=20, y=20, width=600, height=440)
            self.task_window.bind("<space>", self.start_training)
            self.current_task += 1
        elif self.current_task == 3:
            self.is_fixed_time = True

            canvas = Canvas(self.task_window)
            canvas.create_rectangle(318, 220, 322, 260, fill="black")
            canvas.create_rectangle(300, 238, 340, 242, fill="black")

            canvas.pack(fill=BOTH, expand=1)

            self.repeat_counter = 40
            self.task_window.after(1000, self.fixed_two_keys)
        else:
            self.current_task = 0
            self.result_file.close()
            self.task_window.destroy()

    def on_series_1_button(self):

        self.init_task_window()

        self.result_file = open("{}_series_1.txt".format(self.fio), "w+")

        self.current_series = self.start_series_1
        self.task_window.bind("<space>", self.start_series_1)

    def start_series_1(self, event=None):

        _list = self.task_window.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        for item in _list:
            item.pack_forget()

        self.task_window.unbind("<space>")
        self.task_window.unbind("<Return>")

        if self.current_task == 0:
            instruction = Message(self.task_window, text=self.instruction_3)
            instruction.place(x=20, y=20, width=600, height=440)
            self.task_window.bind("<space>", self.start_series_1)
            self.current_task += 1
        elif self.current_task == 1:
            self.is_fixed_time = False
            task = Message(self.task_window, text=self.task_1)
            task.place(x=20, y=20, width=600, height=440)

            self.repeat_counter = -1
            self.task_window.after(random.randint(1000, 2000), self.random_two_keys)

            self.task_window.bind("<Return>", self.on_enter_button)
        elif self.current_task == 2:
            instruction = Message(self.task_window, text=self.instruction_3)
            instruction.place(x=20, y=20, width=600, height=440)
            self.task_window.bind("<space>", self.start_series_1)
            self.current_task += 1
        elif self.current_task == 3:
            self.is_fixed_time = False
            task = Message(self.task_window, text=self.task_2)
            task.place(x=20, y=20, width=600, height=440)

            self.repeat_counter = -1
            self.task_window.after(random.randint(1000, 2000), self.random_two_keys)

            self.task_window.bind("<Return>", self.on_enter_button)
        elif self.current_task == 4:
            instruction = Message(self.task_window, text=self.instruction_3)
            instruction.place(x=20, y=20, width=600, height=440)
            self.task_window.bind("<space>", self.start_series_1)
            self.current_task += 1
        elif self.current_task == 5:
            self.is_fixed_time = True
            task = Message(self.task_window, text=self.task_3)
            task.place(x=20, y=20, width=600, height=440)

            self.repeat_counter = -1
            self.task_window.after(1000, self.fixed_two_keys)

            self.task_window.bind("<Return>", self.on_enter_button)
        elif self.current_task == 6:
            instruction = Message(self.task_window, text=self.instruction_3)
            instruction.place(x=20, y=20, width=600, height=440)
            self.task_window.bind("<space>", self.start_series_1)
            self.current_task += 1
        elif self.current_task == 7:
            self.is_fixed_time = True
            task = Message(self.task_window, text=self.task_4)
            task.place(x=20, y=20, width=600, height=440)

            self.repeat_counter = -1
            self.task_window.after(1000, self.fixed_two_keys)

            self.task_window.bind("<Return>", self.on_enter_button)
        else:
            self.current_task = 0
            self.result_file.close()
            self.task_window.destroy()

    def random_two_keys(self):

        if self.is_task_end:
            self.is_task_end = False
            self.current_task += 1
            self.current_series()
            return

        if not self.is_answered:
            self.result_file.write("false;0;\r\n")
        if self.repeat_counter != 0:
            self.is_answered = False
            if bool(random.getrandbits(1)):
                print("Hight beep")
                self.start_time = int(round(time.time() * 1000))
                self.is_right_answer = True
                self.is_left_answer = False
            else:
                print("Low beep")
                self.start_time = int(round(time.time() * 1000))
                self.is_right_answer = False
                self.is_left_answer = True
            self.task_window.after(random.randint(1000, 2000), self.random_two_keys)
            self.repeat_counter -= 1
        else:
            self.current_task += 1
            self.current_series()

    def fixed_two_keys(self):

        if self.is_task_end:
            self.is_task_end = False
            self.current_task += 1
            self.current_series()
            return

        if self.repeat_counter != 0:
            self.is_answered = False
            if bool(random.getrandbits(1)):
                print("Hight beep")
                self.start_time = int(round(time.time() * 1000))
                self.is_right_answer = True
                self.is_left_answer = False
            else:
                print("Low beep")
                self.start_time = int(round(time.time() * 1000))
                self.is_right_answer = False
                self.is_left_answer = True
            self.repeat_counter -= 1
        else:
            self.current_task += 1
            self.current_series()

    def on_right_button(self, event=None):

        if not self.is_answered:
            self.is_answered = True
            answer_time = int(round(time.time() * 1000)) - self.start_time
            if self.is_right_answer:
                self.result_file.write("true;{};\r\n".format(answer_time))
            else:
                self.result_file.write("false;{};\r\n".format(answer_time))

        if self.is_fixed_time:
            self.task_window.after(1000, self.fixed_two_keys)

    def on_left_button(self, event=None):

        if not self.is_answered:
            self.is_answered = True
            answer_time = int(round(time.time() * 1000)) - self.start_time
            if self.is_left_answer:
                self.result_file.write("true;{};\r\n".format(answer_time))
            else:
                self.result_file.write("false;{};\r\n".format(answer_time))

        if self.is_fixed_time:
            self.task_window.after(1000, self.fixed_two_keys)

    def on_enter_button(self, event=None):
        self.result_file.write("--------------------------\r\n")
        self.is_task_end = True

        if self.is_fixed_time:
            self.is_task_end = False
            self.current_task += 1
            self.current_series()
            return


if __name__ == "__main__":
    main_entity = MainClass()
    main_entity.run()