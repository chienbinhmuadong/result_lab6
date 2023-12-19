class Optical_disc:
    
    def __init__(self, capacity, rotation_speed, thickness_laze=1.2*10**6):
        self.capacity = capacity # считать в МБ (мегабайт)
        self.rotate = rotation_speed #количество оборот в течение 1 минуты (rpm: round per minute)
        self.thickness_laze = thickness_laze # считать в нанометр

    def count_byte(self, time, speed_transfer_data):
        # time = 20secs
        #speed_transfer_data зависит от параметров каждого диска
        return time*speed_transfer_data
   
    def time_read_disc(self, data_density):
        self.speed_read_disc = data_density * self.rotate
        
        ...
    
class CD(Optical_disc):

    def count_average_speed_1_rotate(self):
        self.average_time_1_rotation = 1/self.rotate
    ...
    
class DVD(Optical_disc):

    def count_average_speed_1_rotate(self):
        self.average_time_1_rotation = 1/self.rotate
    ...
    
cd = CD(700, 200, 1200)
dvd_5_ROM = DVD(4700, 1200, 900)

cd.time_read_disc(44.1)
dvd_5_ROM.time_read_disc(300)

print(cd.speed_read_disc)
print(dvd_5_ROM.speed_read_disc)

cd.count_average_speed_1_rotate()
dvd_5_ROM.count_average_speed_1_rotate()

print(cd.average_time_1_rotation)
print(dvd_5_ROM.average_time_1_rotation)

