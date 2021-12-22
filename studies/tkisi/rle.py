import cv2
import numpy as np
import math
import time
import os
#from zigzag import *

# Зигзагообразное сканирование матрицы
# Аргумент - это двумерная матрица любого размера, не строго квадратная.
# Функция возвращает массив размером 1 на (m * n), где m и n - размеры входной матрицы,
# состоящий из его элементов, сканированных зигзагообразным методом.


def zigzag(input):
    # Инициализация переменных
    h = 0
    v = 0
    vmin = 0
    hmin = 0
    vmax = input.shape[0]
    hmax = input.shape[1]
    i = 0
    output = np.zeros((vmax * hmax))
    while ((v < vmax) and (h < hmax)):
        if ((h + v) % 2) == 0:
            if (v == vmin):
                output[i] = input[v, h]  # если добрались до первой строки
                if (h == hmax):
                    v = v + 1
                else:
                    h = h + 1
                i = i + 1
            elif ((h == hmax - 1) and (v < vmax)):  # если добрались до последнего столбца
                output[i] = input[v, h]
                v = v + 1
                i = i + 1
            elif ((v > vmin) and (h < hmax - 1)):  # во всех других случаях
                output[i] = input[v, h]
                v = v - 1
                h = h + 1
                i = i + 1
        else:
            if ((v == vmax - 1) and (h <= hmax - 1)):  # если мы добрались до последней строки
                output[i] = input[v, h]
                h = h + 1
                i = i + 1
            elif (h == hmin):  # если добрались до первого столбца
                output[i] = input[v, h]
                if (v == vmax - 1):
                    h = h + 1
                else:
                    v = v + 1
                i = i + 1
            elif ((v < vmax - 1) and (h > hmin)):  # во вех других случаях
                # print(6)
                output[i] = input[v, h]
                v = v + 1
                h = h - 1
                i = i + 1
        if ((v == vmax - 1) and (h == hmax - 1)):  # проверка правого нижнего эл-та
            output[i] = input[v, h]
            break
    return output

# Обратное зигзагообразное сканирование матрицы
# Аргументы: массив размером 1 x m * n, где m & n - размеры выходной матрицы по вертикали и горизонтали.
# Функция возвращает двумерную матрицу определенных размеров,
# состоящий из элементов входного массива, собранных зигзагообразным методом.


def inverse_zigzag(input, vmax, hmax):
    # Инициализация переменных
    h = 0
    v = 0
    vmin = 0
    hmin = 0
    output = np.zeros((vmax, hmax))
    i = 0
    while ((v < vmax) and (h < hmax)):
        if ((h + v) % 2) == 0:
            if (v == vmin):
                output[v, h] = input[i]  # если добрались до первой линии
                if (h == hmax):
                    v = v + 1
                else:
                    h = h + 1
                i = i + 1
            elif ((h == hmax - 1) and (v < vmax)):  # если добрались до последного столбца
                output[v, h] = input[i]
                v = v + 1
                i = i + 1
            elif ((v > vmin) and (h < hmax - 1)):  # в остальных случаях
                output[v, h] = input[i]
                v = v - 1
                h = h + 1
                i = i + 1
        else:
            if ((v == vmax - 1) and (h <= hmax - 1)):  # если добрались до последней линии
                output[v, h] = input[i]
                h = h + 1
                i = i + 1
            elif (h == hmin):  # если добрались до первого столбца
                output[v, h] = input[i]
                if (v == vmax - 1):
                    h = h + 1
                else:
                    v = v + 1
                i = i + 1
            elif ((v < vmax - 1) and (h > hmin)):  # в остальных случаях
                output[v, h] = input[i]
                v = v + 1
                h = h - 1
                i = i + 1
        if ((v == vmax - 1) and (h == hmax - 1)):
            output[v, h] = input[i]
            break
    return output


def get_run_length_encoding(image):
    i = 0
    skip = 0
    stream = []
    bitstream = ""
    image = image.astype(int)
    while i < image.shape[0]:
        if image[i] != 0:
            stream.append((image[i], skip))
            bitstream = bitstream + str(image[i]) + " " + str(skip) + " "
            skip = 0
        else:
            skip = skip + 1
        i = i + 1
    return bitstream


def main():
    print("0 - Для архивирования, 1 - Для разархивирования")
    mode = input()
    if mode == "0":
        start_time = (int(round(time.time() * 1000)))
        block_size = 8

        # Матрица квантования
        QUANTIZATION_MAT = np.array(
            [[16, 11, 10, 16, 24, 40, 51, 61], [12, 12, 14, 19, 26, 58, 60, 55], [14, 13, 16, 24, 40, 57, 69, 56],
             [14, 17, 22, 29, 51, 87, 80, 62], [18, 22, 37, 56, 68,
                                                109, 103, 77], [24, 35, 55, 64, 81, 104, 113, 92],
             [49, 64, 78, 87, 103, 121, 120, 101], [72, 92, 95, 98, 112, 100, 103, 99]])

        img = cv2.imread('studies\\tkisi\\boat.512.tiff', cv2.IMREAD_GRAYSCALE)

        [h, w] = img.shape
        height = h
        width = w
        h = np.float32(h)
        w = np.float32(w)
        nbh = math.ceil(h / block_size)
        nbh = np.int32(nbh)
        nbw = math.ceil(w / block_size)
        nbw = np.int32(nbw)
        H = block_size * nbh
        W = block_size * nbw

        # Создаём нулевую матрицу размером H на W
        padded_img = np.zeros((H, W))
        padded_img[0:height, 0:width] = img[0:height, 0:width]

        for i in range(nbh):
            row_ind_1 = i * block_size
            row_ind_2 = row_ind_1 + block_size

            for j in range(nbw):
                col_ind_1 = j * block_size
                col_ind_2 = col_ind_1 + block_size
                block = padded_img[row_ind_1: row_ind_2, col_ind_1: col_ind_2]
                DCT = cv2.dct(block)  # Дискретное косинусное преобразование
                DCT_normalized = np.divide(DCT, QUANTIZATION_MAT).astype(int)
                reordered = zigzag(DCT_normalized)
                reshaped = np.reshape(reordered, (block_size, block_size))
                padded_img[row_ind_1: row_ind_2,
                           col_ind_1: col_ind_2] = reshaped

        cv2.imshow('compressed', np.uint8(padded_img))
        end_time = (int(round(time.time() * 1000)))
        print("Скорость сжатия: " + str((end_time - start_time)) + " мсек.")
        cv2.imwrite('compressed.tiff', np.uint8(padded_img))
        size_compress = os.stat('compressed.tiff').st_size
        width = np.size(padded_img, 1)
        height = np.size(padded_img, 0)
        quality = (101 - ((width * height) * 3) / size_compress)
        print("Качество сжатия: " + str(quality))
        arranged = padded_img.flatten()
        bitstream = get_run_length_encoding(arranged)
        bitstream = str(padded_img.shape[0]) + " " + \
            str(padded_img.shape[1]) + " " + bitstream + ";"
        file1 = open("image.txt", "w")
        file1.write(bitstream)
        file1.close()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif mode == "1":
        QUANTIZATION_MAT = np.array(
            [[16, 11, 10, 16, 24, 40, 51, 61], [12, 12, 14, 19, 26, 58, 60, 55], [14, 13, 16, 24, 40, 57, 69, 56],
             [14, 17, 22, 29, 51, 87, 80, 62], [18, 22, 37, 56, 68,
                                                109, 103, 77], [24, 35, 55, 64, 81, 104, 113, 92],
             [49, 64, 78, 87, 103, 121, 120, 101], [72, 92, 95, 98, 112, 100, 103, 99]])

        block_size = 8
        with open('image.txt', 'r') as myfile:
            image = myfile.read()
        details = image.split()

        h = int(''.join(filter(str.isdigit, details[0])))
        w = int(''.join(filter(str.isdigit, details[1])))

        array = np.zeros(h * w).astype(int)
        k = 0
        i = 2
        x = 0
        j = 0

        while k < array.shape[0]:
            if (details[i] == ';'):
                break
            if "-" not in details[i]:
                array[k] = int(''.join(filter(str.isdigit, details[i])))
            else:
                array[k] = -1 * int(''.join(filter(str.isdigit, details[i])))
            if (i + 3 < len(details)):
                j = int(''.join(filter(str.isdigit, details[i + 3])))
            if j == 0:
                k = k + 1
            else:
                k = k + j + 1
            i = i + 2
        array = np.reshape(array, (h, w))

        i = 0
        j = 0
        k = 0

        padded_img = np.zeros((h, w))

        while i < h:
            j = 0
            while j < w:
                temp_stream = array[i:i + 8, j:j + 8]
                block = inverse_zigzag(
                    temp_stream.flatten(), int(block_size), int(block_size))
                de_quantized = np.multiply(block, QUANTIZATION_MAT)
                padded_img[i:i + 8, j:j + 8] = cv2.idct(de_quantized)
                j = j + 8
            i = i + 8

        padded_img[padded_img > 255] = 255
        padded_img[padded_img < 0] = 0
        cv2.imwrite("decompressed.tiff", np.uint8(padded_img))


if __name__ == '__main__':
    main()
