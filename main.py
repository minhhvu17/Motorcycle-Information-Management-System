from datetime import datetime
import pytz

class MotorcycleManagement:
    def __init__(self):
        self.__brandList = []
        self.__categoryList = []
        
    def addBrandList(self, Brand):
        self.__brandList.append(Brand)
    def addCategoryList(self, Category):
        self.__categoryList.append(Category)
    
        
class Brand(MotorcycleManagement):
    def __init__(self, brandName):
        MotorcycleManagement.addBrandList(Brand)
        self.__brandName = brandName
        self.__motorcyclesListByBrand = []
    def getBrandName(self):
        return self.__brandName
    def setBrandName(self, brandName):
        self.__brandName = brandName
    def addToBrand(self, Motorcycle):
        self.__motorcyclesListByBrand.append(Motorcycle)
        
class Category(MotorcycleManagement):
    def __init__(self, categoryName):
        MotorcycleManagement.addCategoryList(Category)
        self.__categoryName = categoryName
        self.__motorcyclesListByCategory = []
    def getCategoryName(self):
        return self.__categoryName
    def setCategoryName(self, categoryName):
        self.__categoryName = categoryName
    def addToCategory(self, Motorcycle):
        self.__motorcyclesListByCategory.append(Motorcycle)
        
class Motorcycle(Brand, Category):
    def __init__(self, model, price, length, width, height, weight, fuelCapacity, maximalEfficiency, fuelConsumption, engineType, engineDisplacement):
        Brand.addToBrand(Motorcycle)
        self.__model = model
        Category.addToCategory(Motorcycle)
        self.__price = price
        self.__length = length
        self.__width = width
        self.__height = height
        self.__weight = weight
        self.__fuelCapacity = fuelCapacity
        self.__maximalEfficiency = maximalEfficiency
        self.__fuelConsumption = fuelConsumption
        self.__engineType = engineType
        self.__engineDisplacement = engineDisplacement
        
    def getModel(self):
        return self.__model
    def setModel(self, model):
        self.__model = model
        
    def getPrice(self):
        return self.__price
    def setPrice(self, price):
        self.__price = price
        
    def getLength(self):
        return self.__length
    def setLength(self, length):
        self.__length = length
        
    def getWidth(self):
        return self.__width
    def setWidth(self, width):
        self.__width = width
        
    def getHeight(self):
        return self.__height
    def setHeight(self, height):
        self.__height = height
    
    def getWeight(self):
        return self.__weight
    def setWeight(self, weight):
        self.__weight = weight
    
    def getFuelCapacity(self):
        return self.__fuelCapacity
    def setFuelCapacity(self, fuelCapacity):
        self.__fuelCapacity = fuelCapacity
    
    def getMaximalEfficiency(self):
        return self.__maximalEfficiency
    def setMaximalEfficiency(self, maximalEfficiency):
        self.__maximalEfficiency = maximalEfficiency
    
    def getFuelConsumption(self):
        return self.__fuelConsumption
    def setFuelConsumption(self, fuelConsumption):
        self.__fuelConsumption = fuelConsumption
    
    def getEngineType(self):
        return self.__engineType
    def setEngineType(self, engineType):
        self.__engineType = engineType
        
    def getEngineDisplacement(self):
        return self.__engineDisplacement
    def setEngineDisplacement(self, engineDisplacement):
        self.__engineDisplacement = engineDisplacement
    
class Order(Motorcycle):
    def __init__(self, buyerName):
        self.__buyerName = buyerName
        self.__timeOfPurchase = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
    
    def getOrderInformation(self):
        print("Customer: {}".format(self.__buyerName))
        print("Purchase at: {}".format(self.__timeOfPurchase))
        print("Product: {}".format(Order.getModel()))
        print("Price: {}".format(Order.getPrice()))
        


def main():
    managementSystem = MotorcycleManagement()
    

if __name__ == "__main__":
    main()
        
    