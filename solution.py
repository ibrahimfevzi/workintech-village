import math as Math


class Silo:
    
    def __init__(self, radius, height, material, max_capacity, current_capacity):
        self.radius = radius
        self.height = height
        self.material = material
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity

# getter & setter metodları

    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        self.radius = radius

    def get_height(self):
        return self.height
    
    def set_height(self, height):
        self.height = height

    def get_material(self):
        return self.material
    
    def set_material(self, material):
        self.material = material

    def get_max_capacity(self):
        return self.max_capacity
    
    def set_max_capacity(self, max_capacity):
        self.max_capacity = max_capacity

    def get_current_capacity(self):
        return self.current_capacity
    
    def set_current_capacity(self, current_capacity):
        self.current_capacity = current_capacity

# diğer metotlar

    def getArea(self):
        return (self.radius**2) * Math.pi
    
    def getVolume(self):
        return self.getArea() * self.height
    

    # silonun tüm özelliklerinin ve alan ve hacim bilgisinin görüldüğü bir __str__ metodu 
    
    def __str__(self):
        return f"""
        Silo
        ----
        radius: {self.radius}
        height: {self.height}
        material: {self.material}
        max_capacity: {self.max_capacity}
        current_capacity: {self.current_capacity}
        area: {self.getArea()}
        volume: {self.getVolume()}
        """
    
    # siloya malzeme ekleme işlemini yapan bir addMaterial metodu

    def addMaterial(self, material):
        if self.current_capacity + material <= self.max_capacity:
            self.current_capacity += material
            return True
        else:
            return False
        
    # silodan malzeme çıkarma işlemini yapan bir removeMaterial metodu

    def removeMaterial(self, material):

        if self.current_capacity - material >= 0:
            self.current_capacity -= material
            return True
        else:
            return False
        
    # silonun doluluk oranını hesaplayan bir getFillRate metodu

    def getFillRate(self):
        return self.current_capacity / self.max_capacity
    
    # silonun doluluk oranına göre dolu mu boş mu olduğunu döndüren bir isFull metodu

    def isFull(self):
        return self.getFillRate() == 1
    

# test kodu
def main():
    silo = Silo(3.75, 2, "metal", 1000, 500)
    print(silo)
    print(silo.addMaterial(100))
    print(silo)
    print(silo.removeMaterial(100))
    print(silo)
    print(silo.getFillRate())
    print(silo.isFull())

#getArea ve getVolume metotlarını test etmek için
    print(silo.getArea())
    print(silo.getVolume())


    main()


    

    