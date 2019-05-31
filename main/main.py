from tkinter import *


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

        self.training_button = None
        self.series_1_button = None
        self.series_2_button = None
        self.series_3_button = None
        self.series_4_button = None

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

        self.series_1_button = Button(self.main_window, text="Серия 1")
        self.series_1_button.place(x=142, y=50, width=100)
        self.series_1_button.config(state="disabled")

        self.series_2_button = Button(self.main_window, text="Серия 2")
        self.series_2_button.place(x=270, y=50, width=100)
        self.series_2_button.config(state="disabled")

        self.series_3_button = Button(self.main_window, text="Серия 3")
        self.series_3_button.place(x=398, y=50, width=100)
        self.series_3_button.config(state="disabled")

        self.series_4_button = Button(self.main_window, text="Серия 4")
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

        self.start_label = Label(self.task_window, text="Нажмите пробел чтобы начать")
        self.start_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    def on_training_button(self):

        self.init_task_window()

        self.task_window.bind("<space>", self.start_training)

    def start_training(self, event=None):

        self.start_label.destroy()

        canvas = Canvas(self.task_window)
        canvas.create_rectangle(318, 220, 322, 260, fill="black")
        canvas.create_rectangle(300, 238, 340, 242, fill="black")

        canvas.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    main_entity = MainClass()
    main_entity.run()