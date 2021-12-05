class Cars:
    def __init__(self,brand, model, color, speed):
        self.brand=brand
        self.model=model
        self.color=color
        self.speed=speed


    def start(self):
        print("started")
        
    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating") 
        

BMW=Cars("BMW", "M5", "Black", 120)
       
print(BMW.model)
BMW.accelerate()