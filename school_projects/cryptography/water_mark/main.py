import numpy as np
from PIL import Image
import random



def embed_watermark(img_path, secret_key, n, d):

    #preprocessing
    img = Image.open(img_path)
    img = img.convert("L")
    pixels = np.array(img)
    for y in range(img.width):
        for x in range(img.height):
            pixels[x, y] = max(min(pixels[x, y], 245), 10)
    
    sum = 0

    random.seed(secret_key)
    for _ in range(n):
        x1, y1 = random.randint(0, img.width - 1), random.randint(0, img.height - 1)
        x2, y2 = random.randint(0, img.width - 1), random.randint(0, img.height - 1)
        
        # Zwiększamy jasność punktów w obszarze A o wartość d
        pixels[y1, x1] += d
        
        # Zmniejszamy jasność punktów w obszarze B o wartość d
        pixels[y2, x2] -= d

        #suma
        sum += pixels[y1, x1] - pixels[y2, x2]

    # Zapisujemy zmodyfikowany obraz
    embedded_img = Image.fromarray(pixels)
    embedded_img.save("embedded_image.png")

    # Zwracamy wynik osadzenia
    return sum

def detect_watermark(embedded_image_path, secret_key, n, d):
    # Otwieramy zmodyfikowany obraz
    embedded_img = Image.open(embedded_image_path)
    embedded_img = embedded_img.convert("L")
    pixels = np.array(embedded_img)
    sum = 0

    # Wybieramy n par obszarów (pikseli) za pomocą generatora pseudolosowego
    random.seed(secret_key)
    for _ in range(n):
        x1, y1 = random.randint(0, embedded_img.width - 1), random.randint(0, embedded_img.height - 1)
        x2, y2 = random.randint(0, embedded_img.width - 1), random.randint(0, embedded_img.height - 1)
        
        sum += pixels[y1, x1] - pixels[y2, x2]
        # Zmniejszamy jasność punktów w obszarze A o wartość d
        pixels[y1, x1] -= d
        
        # Zwiększamy jasność punktów w obszarze B o wartość d
        pixels[y2, x2] += d

        #suma
        

    return sum

# Przykładowe użycie
sum1 = embed_watermark("preprocessed_img.png", secret_key=42, n=10, d=10)
sum2 = detect_watermark("embedded_image.png", secret_key=42, n=10, d=10)

print(sum1, sum2)

