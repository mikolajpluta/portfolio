from PIL import Image, ImageDraw
import math

# def calculate_points_on_circle(n, l, r, image_size):

#     # Obliczanie środka obrazu
#     center_x = image_size[0] // 2
#     center_y = image_size[1] // 2

#     # Obliczanie kąta pomiędzy punktami
#     angle_delta = l / (n - 1) if n > 1 else 0  # Uwzględnienie liczby punktów

#     # Lista punktów
#     points = []

#     # Obliczanie współrzędnych dla każdego punktu
#     for i in range(n):
#         angle = i * angle_delta
#         x = center_x + int(r * math.cos(angle))
#         y = center_y + int(r * math.sin(angle))
#         points.append((x, y))

#     return points

def calculate_points(n, l, r):
    radians = math.radians(l)
    angle = radians/n
    emiters = []
    detectors = []
    for i in range(n):
        alpha = angle * i
        theta = math.radians(90) - alpha
        emiters.append((r*math.cos(alpha)+r, r*math.sin(alpha)+r))
        detectors.append((r*math.cos(alpha+math.pi) + r, r* math.sin(alpha + math.pi)+r))
    return emiters, detectors

def rotate_points(points, center, alpha):
    rotated_points = []
    alpha_rad = math.radians(alpha)  # Konwersja kąta na radiany

    # Przesunięcie i rotacja każdego punktu
    for point in points:
        dx = point[0] - center[0]
        dy = point[1] - center[1]
        new_x = dx * math.cos(alpha_rad) - dy * math.sin(alpha_rad) + center[0]
        new_y = dx * math.sin(alpha_rad) + dy * math.cos(alpha_rad) + center[1]
        rotated_points.append((new_x, new_y))

    return rotated_points


def draw_points_on_image(image, points, color='white', radius=10):
    draw = ImageDraw.Draw(image)
    for point in points:
        draw.ellipse((point[0] - radius, point[1] - radius, point[0] + radius, point[1] + radius), fill=color)


def calculate_opposite_points_on_image(points, image_center):
    opposite_points = []
    for point in points:
        opposite_point = (2 * image_center[0] - point[0], 2 * image_center[1] - point[1])
        opposite_points.append(opposite_point)
    return opposite_points


# Wczytanie obrazu
img = Image.open("przyklady_proj1/SADDLE_PE.jpg")

# Pobranie wymiarów obrazu
width, height = img.size
d = int(pow(width**2 + height**2, 0.5))

# Tworzenie nowego obrazu z odpowiednim paddingiem
new_image = Image.new('L', (d, d), color='black')

# Obliczenie współrzędnych lewego górnego rogu dla wklejenia obrazu
left = (d - width) // 2
top = (d - height) // 2

# Wklejenie obrazu w odpowiednie miejsce
new_image.paste(img, (left, top))

# Utworzenie obiektu do rysowania na nowym obrazie
draw = ImageDraw.Draw(new_image)

# Obliczenie środka obrazu
center = (d // 2, d // 2)

# Obliczenie promienia koła
radius = d // 2

# Narysowanie koła
draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), outline='white')

emiters, detectors = calculate_points(5, 20, radius)


# Wyświetlenie nowego obrazu
print(emiters + detectors)
draw_points_on_image(new_image, emiters + detectors)
new_image.show()

#obrot
rotated_points = rotate_points(emiters + detectors, center, 30)
draw_points_on_image(new_image, rotated_points)
new_image.show()
