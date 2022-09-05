# BMP I/O 以及 上下鏡射
import math

class BMP():
    def mainFunction():
        lst = []
        file = open("lena.bmp", "rb")
        line = file.read()
        for i in range(len(line)):
            lst.append(line[i])
        ImgType = BMP.getImgType(lst)
        ImgSize = BMP.getImgSize(lst)
        ImgOffBits = BMP.getImgOffBits(lst)
        ImgWidth = BMP.getImgWidth(lst)
        ImgHeight = BMP.getImgHeight(lst)
        ImgRawData = BMP.getImgRawData(lst)
        print("ImageType(binary):", ImgType)
        print("ImageSize(binary):", ImgSize, "  ImageSize(byte):", countHex.countFunction(ImgSize))
        print("ImageOffBits(binary):", ImgOffBits, "  ImageOffBits(byte):", countHex.countFunction(ImgOffBits))
        print("ImageWidth(binary):", ImgWidth, "  ImageWidth(byte):", countHex.countFunction(ImgWidth))
        print("ImageHeight(binary):", ImgHeight, "  ImageHeight(byte):", countHex.countFunction(ImgHeight))
        reflectionData = reflection.reflectionImg(ImgRawData, countHex.countFunction(ImgWidth))
        outputData = BMP.outputData(lst, reflectionData)
        BMP.outputFile(outputData)
    
    def getImgType(inputList):
        lst = []
        for i in range(0, 2):
            lst.append(inputList[i])
        return lst

    def getImgSize(inputList):
        lst = []
        for i in range(2, 6):
            lst.append(inputList[i])
        return lst

    def getImgOffBits(inputList):
        lst = []
        for i in range(10, 14):
            lst.append(inputList[i])
        return lst

    def getImgWidth(inputList):
        lst = []
        for i in range(18, 22):
            lst.append(inputList[i])
        return lst

    def getImgHeight(inputList):
        lst = []
        for i in range(22, 26):
            lst.append(inputList[i])
        return lst

    def getImgRawData(inputList):
        lst = []
        for i in range(1078, len(inputList)):
            lst.append(inputList[i])
        return lst

    def outputData(rawData, reflectionData):
        outputData = []
        stringData = ''
        for i in range(0, 1078):
            outputData.append(rawData[i])
        for j in range(len(reflectionData)):
            outputData.append(reflectionData[j])
        return outputData
    
    def outputFile(data):
        print(data)
        outData = bytes(data)
        file = open("lena_reflection.bmp", 'wb')
        file.write(outData)
        file.close()

class countHex():
    def countFunction(inputList):
        total = 0
        for i in range(len(inputList)):
            total = total + inputList[i] * (256 ** i)
        return total

class reflection():
    def reflectionImg(data, width):
        reflectionData = []
        tempData = []
        for i in range((len(data) - 1), -1, -1):
            if i % width != 0:
                tempData.append(data[i])
            else:
                reflection.reflectionDataAppend(reflectionData, tempData)
                if i != 0:
                    tempData = []
                    tempData.append(data[i])
                else:
                    tempData = []
                    tempData.append(data[i])
                    reflection.reflectionDataAppend(reflectionData, tempData)
        return reflectionData

    def reflectionDataAppend(reflectionData, tempData):
        for j in range((len(tempData) - 1), -1, -1):
            reflectionData.append(tempData[j])
        return reflectionData


BMP.mainFunction()
