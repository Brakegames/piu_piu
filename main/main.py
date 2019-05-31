from tkinter import *


class MainClass:

    def __init__(self):

        self.window = Tk()
        self.window.title("Piu Piu")

        self.window.resizable(width=False, height=False)
        self.window.geometry('640x100')

    def run(self):

        fio_label = Label(self.window, text="ФИО")
        fio_label.place(x=14, y=14)

        fio_input = Entry(self.window)
        fio_input.place(x=64, y=14, width=562)

        training_button = Button(self.window, text="Тренировка")
        training_button.place(x=14, y=50, width=100)
        training_button.config(state="disabled")

        series_1_button = Button(self.window, text="Серия 1")
        series_1_button.place(x=142, y=50, width=100)
        series_1_button.config(state="disabled")

        series_2_button = Button(self.window, text="Серия 2")
        series_2_button.place(x=270, y=50, width=100)
        series_2_button.config(state="disabled")

        series_3_button = Button(self.window, text="Серия 3")
        series_3_button.place(x=398, y=50, width=100)
        series_3_button.config(state="disabled")

        series_4_button = Button(self.window, text="Серия 4")
        series_4_button.place(x=526, y=50, width=100)
        series_4_button.config(state="disabled")

        self.window.mainloop()


if __name__ == "__main__":
    main_entity = MainClass()
    main_entity.run()