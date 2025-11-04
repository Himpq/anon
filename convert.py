from PIL import Image

def image_to_dot_matrix(path, width=128, height=64, grayscale=False):
    img = Image.open(path).convert('L')
    img = img.resize((width, height), Image.NEAREST)

    if grayscale:
        img = img.convert('1')
    else:
        threshold = 110
        ref = 0    #阴码/阳码
        img = img.point(lambda x: ref if x > threshold else (0 if ref else 1), '1')
    img.show()

    pixels = img.load()
    bytes_per_row = width // 8
    matrix = []

    for y in range(height):
        row = []
        for bx in range(bytes_per_row):
            byte = 0
            for bit in range(8):
                x = bx * 8 + bit
                val = pixels[x, y] & 1
                byte |= val << bit
            byte &= 0xFF  # 确保uint8_t范围
            row.append(byte)
        matrix.append(row)

    # 输出uint8_t数组
    print(f"uint8_t img_data[] = {{")
    for row in matrix:
        print("    " + ", ".join(f"0x{b:02X}" for b in row) + ",")
    print("};")

    return matrix



if __name__ == "__main__":
    image_to_dot_matrix(input("Image path:"), grayscale=True)
