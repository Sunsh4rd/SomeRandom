from PIL import Image
import os
import numpy as np
import time
import matplotlib.image as mpimg

class LZW:
    def __init__(self, path):
        self.path = path
        self.compressionDictionary, self.compressionIndex = self.createCompressionDict()
        self.decompressionDictionary, self.decompressionIndex = self.createDecompressionDict()

    def compress(self):
        start_time = int(round(time.time() * 1000))
        self.initCompress()
        colorcompress = []
        colorcompress.append(self.compressColor(self.red))
        colorcompress.append(self.compressColor(self.green))
        colorcompress.append(self.compressColor(self.blue))
        print("Сжатие выполнено.")
        Split_file = str(os.path.basename(self.path)).split('.')
        Name_file = Split_file[0] + '_compressed.lzw'
        with open(Name_file, 'w') as file:
            for color in colorcompress:
                for row in color:
                    file.write(row)
                    file.write("\n")
        end_time = int(round(time.time() * 1000))
        size_origin = os.stat('test.tif').st_size
        print("Скорость сжатия: " + str(size_origin / (end_time - start_time)) + " кб/сек.")

    def compressColor(self, colorList):
        colorcompress = []
        i = 0
        for currentRow in colorList:
            currentString = currentRow[0]
            compressedRow = ""
            i += 1
            for charIndex in range(1, len(currentRow)):
                currentChar = currentRow[charIndex]
                if currentString + currentChar in self.compressionDictionary:
                    currentString = currentString + currentChar
                else:
                    compressedRow = compressedRow + str(self.compressionDictionary[currentString]) + ","
                    self.compressionDictionary[currentString + currentChar] = self.compressionIndex
                    self.compressionIndex += 1
                    currentString = currentChar
                currentChar = ""
            compressedRow = compressedRow + str(self.compressionDictionary[currentString])
            colorcompress.append(compressedRow)
        return colorcompress

    def decompress(self):
        image = []
        with open(self.path, "r") as file:
            for line in file:
                decoded_row = self.decompressRow(line)
                image.append(np.array(decoded_row))
        image = np.array(image)
        shape_tup = image.shape
        image = image.reshape((3, shape_tup[0] // 3, shape_tup[1]))
        self.saveImage(image)
        print("Расжатие выполнено.")

    def decompressRow(self, line):
        cur_row = line.split(",")
        cur_row[-1] = cur_row[-1][:-1]
        decoded_row = ""
        word, entry = "", ""
        decoded_row = decoded_row + self.decompressionDictionary[int(cur_row[0])]
        word = self.decompressionDictionary[int(cur_row[0])]
        for i in range(1, len(cur_row)):
            new = int(cur_row[i])
            if new in self.decompressionDictionary:
                entry = self.decompressionDictionary[new]
                decoded_row += entry
                add = word + entry[0]
                word = entry
            else:
                entry = word + word[0]
                decoded_row += entry
                add = entry
                word = entry
            self.decompressionDictionary[self.decompressionIndex] = add
            self.decompressionIndex += 1
        new_row = decoded_row.split(',')
        decodedRow = [int(x) for x in new_row]
        return decodedRow

    def initCompress(self):
        self.image = Image.open(self.path)
        self.height, self.width = self.image.size
        self.red, self.green, self.blue = self.processImage()

    def processImage(self):
        image = self.image.convert('RGB')
        red, green, blue = [], [], []
        pixel_values = list(image.getdata())
        iterator = 0
        for height_index in range(self.height):
            R, G, B = "", "", ""
            for width_index in range(self.width):
                RGB = pixel_values[iterator]
                R = R + str(RGB[0]) + ","
                G = G + str(RGB[1]) + ","
                B = B + str(RGB[2]) + ","
                iterator += 1
            red.append(R[:-1])
            green.append(G[:-1])
            blue.append(B[:-1])
        return red, green, blue

    def saveImage(self, image):
        Split_file = str(os.path.basename(self.path)).split('.')
        Name_file = Split_file[0] + "_decompressed.tif"
        imagelist, imagesize = self.makeImageData(image[0], image[1], image[2])
        imagenew = Image.new('RGB', imagesize)
        imagenew.putdata(imagelist)
        imagenew.save(Name_file)

    def makeImageData(self, r, g, b):
        imagelist = []
        for i in range(len(r)):
            for j in range(len(r[0])):
                imagelist.append((r[i][j], g[i][j], b[i][j]))
        return imagelist, (len(r), len(r[0]))

    def createCompressionDict(self):
        dictionary = {}
        for i in range(10):
            dictionary[str(i)] = i
        dictionary[','] = 10
        return dictionary, 11

    def createDecompressionDict(self):
        dictionary = {}
        for i in range(10):
            dictionary[i] = str(i)
        dictionary[10] = ','
        return dictionary, 11