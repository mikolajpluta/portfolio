from PIL import Image, ImageDraw
import math
from sensor import *
import numpy as np

class Tomograph:
    def __init__(self, alpha, l, n, image):
        self.alpha = alpha
        self.l = l
        self.n = n
        self.width, self.height = image.size
        self.d = int(pow(self.width**2 + self.height**2, 0.5))
        self.r = self.d // 2
        self.final_img = Image.new('L', (self.d, self.d), color='black')
        self.final_base_img = self.final_img.copy()
        left = (self.d - self.width) // 2
        top = (self.d - self.height) // 2
        self.final_img.paste(image, (left, top))
        self.center = (self.r, self.r)
        self.emiters = []
        self.detectors = []
        self.sinogram = [[0.0 for _ in range(self.n)] for _ in range(360 // alpha)]
        self.pixels = self.final_img.load()
        self.step = 0
        self.final_pixels = [[[0, 0] for _ in range(self.d)] for _ in range(self.d)]
        self.img_state = Image.new('RGB', (self.d, self.d), 'white')
        self.sinogram_step_image = Image.new('RGB', (len(self.sinogram[0]), len(self.sinogram)), 'white')
        self.max_val = 0

    def calculate_points(self):

        radians = math.radians(self.l)
        angle_between_detectors = radians/self.n
        offset = math.radians(self.step * self.alpha)
        emiters = []
        detectors = []
        for i in range(self.n):
            alpha = (angle_between_detectors * i) + offset
            emiters.append((int(self.r*math.cos(alpha)+self.r), int(self.r*math.sin(alpha)+self.r)))
            detectors.append((int(self.r*math.cos(alpha+math.pi) + self.r), int(self.r * math.sin(alpha + math.pi)+self.r)))
        self.emiters = emiters
        self.detectors = detectors

    def sinogram_step(self):
        for i in range(self.n):
            sensor = Sensor(self.emiters[i], self.detectors[self.n - i - 1], self.pixels, self.height, self.width)
            self.sinogram[self.step][i] = sensor.calculate_sum()

    def get_sinogram_image(self):

        width = len(self.sinogram[0])
        height = len(self.sinogram)

        # Tworzenie nowego obrazu
        img = Image.new('RGB', (width, height), 'white')

        # Iteracja przez wartości tablicy i ustawianie odpowiednich pikseli
        for x in range(width):
            for y in range(height):
                # Normalizacja wartości z zakresu 0-1 do 0-255
                normalized_value = int(self.sinogram[y][x] * 255)

                # Dla wartości 0 ustawiamy kolor czarny, dla wartości 1 - biały
                color = (normalized_value, normalized_value, normalized_value)
                img.putpixel((x, y), color)
        return img


    def make_sinogram_step_image(self):

            width = len(self.sinogram[0])
            height = len(self.sinogram)

            # Iteracja przez wartości tablicy i ustawianie odpowiednich pikseli
            for y in range(height):
                for x in range(width):
                    # Normalizacja wartości z zakresu 0-1 do 0-255
                    normalized_value = int(self.sinogram[y][x] * 255)
                    # Dla wartości 0 ustawiamy kolor czarny, dla wartości 1 - biały
                    color = (normalized_value, normalized_value, normalized_value)
                    self.sinogram_step_image.putpixel((x, y), color)


    def sum_brightness(self, point1, point2, color): 
        dx = abs(point2[0] - point1[0])
        dy = abs(point2[1] - point1[1])
        
        if dx >= dy:
            steps = dx
        else:
            steps = dy
        
        dx = (point2[0] - point1[0]) / steps
        dy = (point2[1] - point1[1]) / steps

        x = point1[0]
        y = point1[1]

        for i in range(int(steps) + 1):
            # Sprawdź czy piksel jest w granicach obrazu
            if 0 <= int(x) < self.d and 0 <= int(y) < self.d:
                self.final_pixels[int(x)][int(y)][0] += int(color * 255)
                self.final_pixels[int(x)][int(y)][1] += 1

            x += dx
            y += dy

    def draw_points_on_image(self, color='white', radius=10):
        draw = ImageDraw.Draw(self.final_base_img)
        for point in self.emiters + self.detectors:
            draw.ellipse((point[0] - radius, point[1] - radius, point[0] + radius, point[1] + radius), fill=color)

    def draw_final_image(self):
        self.max_val = np.amax(self.final_pixels)
        img = Image.new('RGB', (self.d, self.d), 'white')

        for x in range(self.d):
            for y in range(self.d):
                normalized_pixel_val = (self.final_pixels[x][y][0] / self.max_val) * 255
                clr = int(normalized_pixel_val)
                color = (clr, clr, clr)
                img.putpixel((x, y), color)

        print("zwracam obraz wyjsciowy")

        img_width, img_height = img.size
        left = (img_width - self.width) / 2
        top = (img_height - self.height) / 2
        right = (img_width + self.width) / 2
        bottom = (img_height + self.height) / 2
        img = img.crop((left, top, right, bottom))

        return img
    
    def draw_step(self):
        for x in range(self.d):
            for y in range(self.d):
                if self.max_val <= 0.0:
                    self.max_val = 1.0
                normalized_pixel_val = (self.final_pixels[x][y][0] / self.max_val) * 255
                clr = int(normalized_pixel_val)
                color = (clr, clr, clr)
                self.img_state.putpixel((x, y), color)

