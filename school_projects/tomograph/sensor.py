from PIL import Image
import math

class Sensor:
    def __init__(self, emitter_position, detector_position, pixels, img_height, img_width):
        self.emitter_position = emitter_position
        self.detector_position = detector_position
        self.pixels = pixels
        self.img_height = img_height
        self.img_width = img_width
        
    def calculate_sum(self):
        # Pobierz współrzędne emitera i detektora
        x1, y1 = self.emitter_position
        x2, y2 = self.detector_position
        
        # Algorytm Bresenhama do liniowego przejścia przez piksele
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if x1 < x2:
            sx = 1
        else:
            sx = -1
        if y1 < y2:
            sy = 1
        else:
            sy = -1
        err = dx - dy
        
        # Oblicz długość linii między emiterem i detektorem
        line_length = int(max(dx, dy))
        
        # Iteruj po pikselach na linii między emiterem i detektorem
        total_sum = 0.0
        num_pixels = 0.0
        x = x1
        y = y1
        for i in range(line_length):
            # Sprawdzenie, czy piksel znajduje się w granicach obrazu
            if x >= 0 and x < self.img_width and y >= 0 and y < self.img_height:
                pixel_value = self.pixels[x, y]  # Pobierz tylko pierwszy element z krotki (wartość piksela)
                total_sum += pixel_value
                num_pixels += 1

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

        if (num_pixels == 0):
            return 0

        return math.log((num_pixels * 255) / ((num_pixels * 255) - total_sum), math.e)

