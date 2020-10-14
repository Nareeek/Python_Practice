class PC:
    processor = "Xeon"
    def set_processor(self, new_processor):
        processor = new_processor
        
class Desktop(PC):
    os = "Mac OS High Sierra"
    ram = "32 GB"
    
class Laptop(PC):
    os = "Windows 10 Pro 64"
    ram = "16 GB"
    
desk = Desktop()
print(desk.processor, desk.os, desk.ram)

lap = Laptop()
print(lap.processor, lap.os, lap.ram)