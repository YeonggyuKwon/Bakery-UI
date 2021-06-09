import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        Label(window, text="샌드위치 (5000원)").grid(column=0,row=0)
        Label(window, text="케이크 (20000원)").grid(column=0,row=1)
        self.sandwich=Entry(window, width=10)
        self.sandwich.grid(column=1, row=0)
        self.cake=Entry(window, width=10)
        self.cake.grid(column=1,row=1)
        order=Button(window, text="주문하기",command=self.send_order).grid(column=0,row=2)

    def send_order(self):
        sandwich_num=str(self.sandwich.get())
        cake_num=str(self.cake.get())
        if(sandwich_num.isdigit() and cake_num.isdigit()):
            if(int(sandwich_num)>0 and int(cake_num)>0):
                order_text = '{}: 샌드위치 (5000원) {}개 케이크 (20000원) {}개'.format(self.name,sandwich_num,cake_num)
                self.bakeryView.add_order(order_text)
            elif (int(sandwich_num) <=0):
                order_text = '{}: 케이크 (20000원) {}개'.format(self.name, cake_num)
                self.bakeryView.add_order(order_text)
            elif (int(cake_num) <=0):
                order_text = '{}: 샌드위치 (5000원) {}개'.format(self.name, sandwich_num)
                self.bakeryView.add_order(order_text)
        elif(not sandwich_num.isdigit() and cake_num.isdigit()): #샌드위치가 문자고 케이크가 숫자
            if(int(cake_num)>0): #케이크가 양수일때만 출력
                order_text = '{}: 케이크 (20000원) {}개'.format(self.name, cake_num)
                self.bakeryView.add_order(order_text)
        elif(not cake_num.isdigit() and sandwich_num.isdigit()):
            if (int(sandwich_num) > 0):
                order_text = '{}: 샌드위치 (5000원) {}개'.format(self.name, sandwich_num)
                self.bakeryView.add_order(order_text)

if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
