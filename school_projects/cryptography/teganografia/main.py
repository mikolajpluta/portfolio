from PIL import Image

def hide_message_in_image(image_path, message):
    # Otwieramy obraz
    img = Image.open(image_path)
    img = img.convert("RGB")
    width, height = img.size
    pixels = img.load()

    # Konwertujemy wiadomość na binarną reprezentację
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Lista do przechowywania zmienionych pikseli
    changed_pixels = []

    # Zmieniamy najmniej znaczący bit RGB dla każdego piksela
    bit_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])
            original_pixel = pixel.copy()  # Zapamiętujemy oryginalną wartość piksela
            for i in range(3):
                if bit_index < len(binary_message):
                    # Modyfikujemy najmniej znaczący bit
                    pixel[i] &= 0xFE  # Ustawiamy na 0
                    pixel[i] |= int(binary_message[bit_index])  # Ustawiamy na 1, jeśli to konieczne
                    bit_index += 1
            pixels[x, y] = tuple(pixel)
            if pixel != original_pixel:  # Sprawdzamy, czy piksel został zmieniony
                changed_pixels.append((x, y, original_pixel, pixel))

    # Zapisujemy zmodyfikowany obraz
    img.save("encrypted_image.png")
    img.close()

    print("Wiadomość została ukryta w obrazie.")

    # Wyświetlamy binarną reprezentację tekstu do zaszyfrowania
    print("Tekst do zaszyfrowania (binarnie):", ''.join(format(ord(char), '08b') for char in message))

    # Wyświetlamy tylko zmienione piksele
    print("\nZmienione piksele:")
    for pixel_info in changed_pixels:
        x, y, original_pixel, new_pixel = pixel_info
        print(f"Piksel ({x}, {y}): {original_pixel} => {new_pixel}")
        print(f"Binarna reprezentacja piksela: {[format(value, '08b') for value in original_pixel]} => {[format(value, '08b') for value in new_pixel]}")

# Przykładowe użycie
text_to_hide = "kocham Olke bardzo mocno"
hide_message_in_image("wolf.png", text_to_hide)
