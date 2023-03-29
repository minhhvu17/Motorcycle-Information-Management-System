import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

url = "E:\\Second_year\\Advanced Programming with Python\\Final\\"

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
        
        userInformationFrame = tk.Frame(self.window, width=1280, height=60, bg="black")
        userInformationFrame.place(x=0, y=0)
        
        navigationFrame = tk.Frame(self.window, width=270, height=660, bg="#cc0000")
        navigationFrame.place(x=0, y=60)
        
        self.contentFrame = tk.Frame(self.window, width=1010, height=660, bg='#fff')
        self.contentFrame.place(x=270, y=60)
        
        
        self.logoImg = Image.open(f"{url}image\\motorbike.png")
        self.logoResizeImg = self.logoImg.resize((120, 120))
        self.logoResizeImg = ImageTk.PhotoImage(self.logoResizeImg)
        self.logo = tk.Label(navigationFrame, image=self.logoResizeImg, bg='#cc0000')
        self.logo.place(x=60, y=30)
        

        dashboardBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Dashboard", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayDashboard(self.contentFrame), cursor = 'hand2')
        dashboardBtn.place(x=0, y=200)
        
        # Button to activate the function
        brandBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Brand", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayBrand(self.contentFrame))
        brandBtn.place(x=0, y=235)
        
        categoryBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Category", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayCategory(self.contentFrame))
        categoryBtn.place(x=0, y=270)
        
        addProductBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Add Product", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayAddProduct(self.contentFrame))
        addProductBtn.place(x=0, y=305)
        
        manageProductsBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Manage Products", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayManageProducts(self.contentFrame))
        manageProductsBtn.place(x=0, y=340)
        
        newOrderBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="New order", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayNewOrder(self.contentFrame))
        newOrderBtn.place(x=0, y=375)
        
        manageOrdersBtn = HoverButton(navigationFrame, width=26, fg="#fff", bg="#cc0000", text="Orders history", font=('Helvetica', 13, 'bold'), bd=None, activebackground='#b20000', activeforeground = 'white', relief='flat', command=lambda: self.displayManageOrders(self.contentFrame))
        manageOrdersBtn.place(x=0, y=410)
        
        self.displayDashboard(self.contentFrame)
    
    
    # Function to clear all widgets in frame
    def clearFrame(self, contentFrame):
        for widget in contentFrame.winfo_children():
            widget.destroy()
            
            
    
    # Dashboard content
    def displayDashboard(self, contentFrame):
        self.clearFrame(contentFrame)    
        tk.Label(contentFrame, text="Dashboard",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        
        contentFrameOne = tk.Frame(contentFrame, width=220, height=220, bg='#cccccc')
        contentFrameOne.place(x=180, y=140)
        
        self.totalProductImg = Image.open(f"{url}image\\Total_products.png")
        self.totalProductResizeImg = self.totalProductImg.resize((220, 220))
        self.totalProductResizeImg = ImageTk.PhotoImage(self.totalProductResizeImg)
        self.totalProduct = tk.Label(contentFrameOne, image=self.totalProductResizeImg, bg='#ffffff')
        self.totalProduct.place(x=0, y=0)
        
        
        contentFrameTwo = tk.Frame(contentFrame, width=220, height=220, bg='#cccccc')
        contentFrameTwo.place(x=580, y=140)
        self.revenueImg = Image.open(f"{url}image\\Revenue.png")
        self.revenueResizeImg = self.revenueImg.resize((220, 220))
        self.revenueResizeImg = ImageTk.PhotoImage(self.revenueResizeImg)
        self.revenue = tk.Label(contentFrameTwo, image=self.revenueResizeImg, bg='#ffffff')
        self.revenue.place(x=0, y=0)
        
        contentFrameThree = tk.Frame(contentFrame, width=220, height=220, bg='#cccccc')
        contentFrameThree.place(x=180, y=390)
        self.brandsImg = Image.open(f"{url}image\\Brands.png")
        self.brandsResizeImg = self.brandsImg.resize((220, 220))
        self.brandsResizeImg = ImageTk.PhotoImage(self.brandsResizeImg)
        self.brands = tk.Label(contentFrameThree, image=self.brandsResizeImg, bg='#ffffff')
        self.brands.place(x=0, y=0)
        
        contentFrameFour = tk.Frame(contentFrame, width=220, height=220, bg='#cccccc')
        contentFrameFour.place(x=580, y=390)
        self.soldProductsImg = Image.open(f"{url}image\\Sold_products.png")
        self.soldProductsResizeImg = self.soldProductsImg.resize((220, 220))
        self.soldProductsResizeImg = ImageTk.PhotoImage(self.soldProductsResizeImg)
        self.soldProducts = tk.Label(contentFrameFour, image=self.soldProductsResizeImg, bg='#ffffff')
        self.soldProducts.place(x=0, y=0)
        
        
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
        def directToManual(e):
            pass
        self.manualImg = Image.open(f"{url}image\\manual.png")
        self.manualResizeImg = self.manualImg.resize((200, 200))
        self.manualResizeImg = ImageTk.PhotoImage(self.manualResizeImg)
        self.manual = tk.Label(contentFrame, image=self.manualResizeImg, bg='#ffffff', cursor='hand2')
        self.manual.place(x=180, y=140)
        self.manual.bind('<Button-1>', directToManual)
        
        
        # Scooter Box
        def directToScooter(e):
            pass
        self.scooterImg = Image.open(f"{url}image\\scooter.png")
        self.scooterImg = self.scooterImg.resize((200, 200))
        self.scooterImg = ImageTk.PhotoImage(self.scooterImg)
        self.scooter = tk.Label(contentFrame, image=self.scooterImg, bg='#ffffff', cursor='hand2')
        self.scooter.place(x=580, y=140)
        self.scooter.bind('<Button-1>', directToScooter)
        
        # Sport Box
        def directToSport(e):
            pass
        self.sportImg = Image.open(f"{url}image\\sport.png")
        self.sportImg = self.sportImg.resize((200, 200))
        self.sportImg = ImageTk.PhotoImage(self.sportImg)
        self.sport = tk.Label(contentFrame, image=self.sportImg, bg='#ffffff', cursor='hand2')
        self.sport.place(x=380, y=390)
        self.sport.bind('<Button-1>', directToSport)
        
          
        
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
        
        tk.Label(inputFrame, text="Quantity:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=30, y=380)
        quantityInput = ttk.Entry(inputFrame, width=7, font=('Helvetica', 14))
        quantityInput.place(x=230,y=380)
        
        # Get entry box content
        def getContent():
            model = modelInput.get()
            brand = brandOption.get()
            category = categoryOption.get()
            length = lengthInput.get()
            width = widthInput.get()
            height = heightInput.get()
            mass = massInput.get()
            fuelCapacity = fuelCapacityInput.get()
            fuelConsumption = fuelConsumptionInput.get()
            engineType = engineTypeInput.get()
            maximalEfficiency = maximalEfficiencyInput.get()
            color = colorInput.get()
            sellingPrice = sellingPriceInput.get()
            quantity = quantityInput.get()
            atrribute = [model, brand, category, length, width, height, mass, fuelCapacity, fuelConsumption, engineType, maximalEfficiency, color, sellingPrice, quantity]
            for i in atrribute:
                if i == '':
                    messagebox.showwarning("warning", "Some boxes are not filled!")
                    return
        
        # Add button
        addBtn = HoverButton(inputFrame,text='Add',bg='#238636', fg='#fff', font=('Helvetica', 10, 'bold'), width=10, activebackground='#238636', activeforeground='#fff', relief='flat', command=getContent)
        addBtn.place(x=660,y=420)
        
        # Clear entry box content
        def clearContent():
            modelInput.delete(0, tk.END)
            brandOption.set('')
            categoryOption.set('')
            lengthInput.delete(0, tk.END)
            widthInput.delete(0, tk.END)
            heightInput.delete(0, tk.END)
            massInput.delete(0, tk.END)
            fuelCapacityInput.delete(0, tk.END)
            fuelConsumptionInput.delete(0, tk.END)
            engineTypeInput.delete(0, tk.END)
            maximalEfficiencyInput.delete(0, tk.END)
            colorInput.delete(0, tk.END)
            sellingPriceInput.delete(0, tk.END)
            quantityInput.delete(0, tk.END)
        
        # Clear button
        clearBtn = HoverButton(inputFrame,text='Clear',bg='#cc0000', fg='#fff', font=('Helvetica', 10, 'bold'), width=10, activebackground='#cc0000', activeforeground='#fff', relief='flat', command=clearContent)
        clearBtn.place(x=770,y=420)
        
        
        
    def displayManageProducts(self, contentFrame):
        self.clearFrame(contentFrame)   
        tk.Label(contentFrame, text="Manage products",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        
    def displayNewOrder(self, contentFrame):   
        self.clearFrame(contentFrame)
        tk.Label(contentFrame, text="New order",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
        
        customerInformationFrame = tk.Frame(contentFrame, height=180, width=890, bg='#cccccc')
        customerInformationFrame.place(x=60, y=120)
        tk.Label(customerInformationFrame, text="Customer Information:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=10, y=10)
        
        tk.Label(customerInformationFrame, text="Name:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=40, y=60)
        customerNameInput = ttk.Entry(customerInformationFrame, width=22, font=('Helvetica', 14))
        customerNameInput.place(x=150,y=60)
        
        tk.Label(customerInformationFrame, text="Phone:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=40, y=120)
        phoneInput = ttk.Entry(customerInformationFrame, width=22, font=('Helvetica', 14))
        phoneInput.place(x=150,y=120)
        
        modelInformationFrame = tk.Frame(contentFrame, height=290, width=890, bg='#cccccc')
        modelInformationFrame.place(x=60, y=330)
        tk.Label(modelInformationFrame, text="Product bought:",font=('Helvetica', 14, 'bold'), bg='#cccccc').place(x=10, y=10)
        
    def displayManageOrders(self, contentFrame):
        self.clearFrame(contentFrame)
        tk.Label(contentFrame, text="Orders history",font=('Helvetica', 25, 'bold'), bg='#fff').place(x=60, y=60)
    

            
        
def main():
    root = tk.Tk()
    program = Main(root)
    root.mainloop()

if __name__ == "__main__":
    main()