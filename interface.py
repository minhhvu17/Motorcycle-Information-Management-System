import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.background = self['bg']
        self.bind("<Enter>", self.hover)
        self.bind("<Leave>", self.leave)
        
    def hover(self, e):
        self['bg'] = self['activebackground']
    def leave(self, e):
        self['bg'] = self.background
        
# class OptionButton(tk.Button):
#     def __init__(self, master, text1, text2, bigFrame, **kw):
#         self.window = bigFrame
#         self.text1 = text1
#         self.text2 = text2
#         tk.Button.__init__(self, master=master, **kw)
#         self.background = self['bg']
#         self.bind("<Button-1>", self.click)
#         self.bind("<Enter>", self.hover)
#         self.bind("<Leave>", self.leave)
#         self.display = False
#         self.btn1 = None
#         self.btn2 = None
#     def click(self, e):
#         if self.display == False:
#             self.btn1 = HoverButton(self.window, width=26, fg="#fff", bg="#b20000", text=self.text1, font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat')
#             self.btn1.place(x=self.winfo_x()+270, y=self.winfo_y()+60)    
#             self.btn2 = HoverButton(self.window, width=26, fg="#fff", bg="#b20000", text=self.text2, font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat')
#             self.btn2.place(x=self.winfo_x()+270, y=self.winfo_y()+60+32)
#             self.display = True
#         else:
#             self.btn1.place_forget()
#             self.btn2.place_forget()
#             self.display = False   
#     def hover(self, e):
#         self['bg'] = self['activebackground']
#     def leave(self, e):
#         self['bg'] = self.background
    
        

class Main:
    def __init__(self, root):
        self.window = root
        self.window.geometry("1280x720+100+50")
        self.window.resizable(False, False)
        self.window.title("Motorcycle Store Information Management System")
        
        userInformationFrame = tk.Frame(self.window, width=1280, height=60, bg="#cccccc")
        userInformationFrame.place(x=0, y=0)
        
        navigationFrame = tk.Frame(self.window, width=270, height=660, bg="#cc0000")
        navigationFrame.place(x=0, y=60)
        
        self.contentFrame = tk.Frame(self.window, width=1010, height=660, bg='#fff')
        self.contentFrame.place(x=270, y=60)
            
        dashboardBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Dashboard", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayDashboard(self.contentFrame))
        dashboardBtn.place(x=0, y=40)
        
        # Button to activate the function
        brandBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Brand", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayBrand(self.contentFrame))
        brandBtn.place(x=0, y=75)
        
        categoryBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Category", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayCategory(self.contentFrame))
        categoryBtn.place(x=0, y=110)
        
        addProductBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Add Product", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayAddProduct(self.contentFrame))
        addProductBtn.place(x=0, y=145)
        
        manageProductsBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Manage Products", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayManageProducts(self.contentFrame))
        manageProductsBtn.place(x=0, y=180)
        
        newOrderBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="New order", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayNewOrder(self.contentFrame))
        newOrderBtn.place(x=0, y=215)
        
        manageOrdersBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Orders history", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayManageOrders(self.contentFrame))
        manageOrdersBtn.place(x=0, y=250)
        
        self.displayDashboard(self.contentFrame)
    
    
    # Function to clear all widgets in frame
    def clearFrame(self, contentFrame):
        for widget in contentFrame.winfo_children():
            widget.destroy()
            
            
    
    # Dashboard content
    def displayDashboard(self, contentFrame):
        self.clearFrame(contentFrame)    
        tk.Label(contentFrame, text="Dashboard",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        
        contentFrameOne = tk.Frame(contentFrame, width=220, height=200, bg='#cccccc')
        contentFrameOne.place(x=180, y=140)
        
        contentFrameTwo = tk.Frame(contentFrame, width=220, height=200, bg='#cccccc')
        contentFrameTwo.place(x=580, y=140)
        
        contentFrameThree = tk.Frame(contentFrame, width=220, height=200, bg='#cccccc')
        contentFrameThree.place(x=180, y=390)
        
        contentFrameFour = tk.Frame(contentFrame, width=220, height=200, bg='#cccccc')
        contentFrameFour.place(x=580, y=390)
        
        
    # Brand content
    def displayBrand(self, contentFrame):
        self.clearFrame(contentFrame)
        # Label "Brand"
        tk.Label(contentFrame, text="Brand",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        # Add new brand
        tk.Label(contentFrame, text="Add brand",font=('Helvetica', 18, 'bold'), bg='#fff').place(x=120, y=120)
        brandAddEntryBox = ttk.Entry(contentFrame, width=30, font=('Helvetica', 14))
        brandAddEntryBox.place(x=180, y=160)
        saveChangeBtn = HoverButton(contentFrame,text='Add brand',bg='#238636', fg='#fff', font=('Helvetica', 10, 'bold'), width=10, activebackground='#238636', activeforeground='#fff', relief='flat')
        saveChangeBtn.place(x=520,y=160)
        
        tk.Label(contentFrame, text="Brand list",font=('Helvetica', 18, 'bold'), bg='#fff').place(x=120, y=250)
        tableFrame = tk.Frame(contentFrame, height=300, width=890, bg='#cccccc')
        tableFrame.place(x=60, y=290)
        
    def displayCategory(self, contentFrame):
        self.clearFrame(contentFrame)   
        tk.Label(contentFrame, text="Category",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        
        # Manual Motorcycle Box
        self.manualImg = Image.open(r"E:/Second_year/Advanced Programming with Python/Final/image/manual.png")
        self.manualResizeImg = self.manualImg.resize((200, 200))
        self.manualResizeImg = ImageTk.PhotoImage(self.manualResizeImg)
        self.manual = tk.Label(contentFrame, image=self.manualResizeImg, bg='#ffffff')
        self.manual.place(x=180, y=140)
        
        # Scooter Box
        self.scooterImg = Image.open("E:\\Second_year\\Advanced Programming with Python\\Final\\image\\scooter.png")
        self.scooterImg = self.scooterImg.resize((200, 200))
        self.scooterImg = ImageTk.PhotoImage(self.scooterImg)
        self.scooter = tk.Label(contentFrame, image=self.scooterImg, bg='#ffffff')
        self.scooter.place(x=580, y=140)
        
        # Sport Box
        self.sportImg = Image.open("E:\\Second_year\\Advanced Programming with Python\\Final\\image\\sport.png")
        self.sportImg = self.sportImg.resize((200, 200))
        self.sportImg = ImageTk.PhotoImage(self.sportImg)
        self.sport = tk.Label(contentFrame, image=self.sportImg, bg='#ffffff')
        self.sport.place(x=380, y=390)
          
        
    def displayAddProduct(self, contentFrame):
        self.clearFrame(contentFrame)
        
        tk.Label(contentFrame, text="Add product",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        inputFrame = tk.Frame(contentFrame, width=890, height=470, bg='#cccccc')
        inputFrame.place(x=60, y=120)
        
        # Input for model name
        tk.Label(inputFrame, text="Model:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=30)
        modelInput = ttk.Entry(inputFrame, width=25, font=('Helvetica', 14))
        modelInput.place(x=120,y=30)
        
        # Options for brand
        tk.Label(inputFrame, text="Brand:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=80)
        brandOption = ttk.Combobox(inputFrame, width=25, font=('Helvetica', 14), values=['Yamaha', 'Honda'], state='r')
        brandOption.place(x=120, y=80)
        
        # Options for category
        tk.Label(inputFrame, text="Category:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=450, y=80)
        categoryOption = ttk.Combobox(inputFrame, width=25, font=('Helvetica', 14), values=['Manual', 'Scooter', 'Sport'], state='r')
        categoryOption.place(x=570, y=80)
        
        # Input for length
        tk.Label(inputFrame, text="Length:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=130)
        lengthInput = ttk.Entry(inputFrame, width=6, font=('Helvetica', 14))
        lengthInput.place(x=120,y=130)
        
        # Input for width
        tk.Label(inputFrame, text="Width:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=250, y=130)
        widthInput = ttk.Entry(inputFrame, width=6, font=('Helvetica', 14))
        widthInput.place(x=330,y=130)
        
        # Input for height
        tk.Label(inputFrame, text="Height:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=450, y=130)
        heightInput = ttk.Entry(inputFrame, width=6, font=('Helvetica', 14))
        heightInput.place(x=535,y=130)
        
        # Input mass
        tk.Label(inputFrame, text="Mass:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=700, y=130)
        massInput = ttk.Entry(inputFrame, width=6, font=('Helvetica', 14))
        massInput.place(x=780,y=130)
        
        # Input fuel capacity
        tk.Label(inputFrame, text="Fuel Capacity:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=180)
        fuelCapacityInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        fuelCapacityInput.place(x=230,y=180)
        
        # Input fuel consumption
        tk.Label(inputFrame, text="Fuel Consumption:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=450, y=180)
        fuelConsumptionInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        fuelConsumptionInput.place(x=680,y=180)
        
        # Input engine type
        tk.Label(inputFrame, text="Engine type:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=230)
        engineTypeInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        engineTypeInput.place(x=230,y=230)
        
        # Input maximal efficiency
        tk.Label(inputFrame, text="Maximal Efficiency:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=450, y=230)
        maximalEfficiencyInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        maximalEfficiencyInput.place(x=680,y=230)
        
        # Input selling price
        tk.Label(inputFrame, text="Color:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=280)
        colorInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        colorInput.place(x=230,y=280)
        
        # Input maximal efficiency
        tk.Label(inputFrame, text="Selling price:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=330)
        sellingPriceInput = ttk.Entry(inputFrame, width=15, font=('Helvetica', 14))
        sellingPriceInput.place(x=230,y=330)
        
        # Add button
        addBtn = HoverButton(inputFrame,text='Add',bg='#238636', fg='#fff', font=('Helvetica', 10, 'bold'), width=10, activebackground='#238636', activeforeground='#fff', relief='flat')
        addBtn.place(x=660,y=420)
        
        # Clear button
        clearBtn = HoverButton(inputFrame,text='Clear',bg='#cc0000', fg='#fff', font=('Helvetica', 10, 'bold'), width=10, activebackground='#cc0000', activeforeground='#fff', relief='flat')
        clearBtn.place(x=770,y=420)
        
        
    def displayManageProducts(self, contentFrame):
        self.clearFrame(contentFrame)   
        tk.Label(contentFrame, text="Manage products",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        
    def displayNewOrder(self, contentFrame):   
        self.clearFrame(contentFrame)
        tk.Label(contentFrame, text="New order",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        
    def displayManageOrders(self, contentFrame):
        self.clearFrame(contentFrame)
        tk.Label(contentFrame, text="Orders history",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
    
        
        
def main():
    root = tk.Tk()
    program = Main(root)
    root.mainloop()

if __name__ == "__main__":
    main()