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
        Img256Data = Img512To256.arrayReduceFunction(ImgRawData)
        lst = Img512To256.headerWidthAndHeightChange(lst, len(Img256Data))
        outputData = BMP.outputData(lst, Img256Data)
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

    def outputData(rawData, Img512Data):
        outputData = []
        stringData = ''
        for i in range(0, 1078):
            outputData.append(rawData[i])
        for j in range(len(Img512Data)):
            outputData.append(Img512Data[j])
        return outputData
    
    def outputFile(data):
        outData = bytes(data)
        file = open("lena_256.bmp", 'wb')
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
    
class Img512To256():
    def arrayReduceFunction(ImgRawData):

        reducedData = []
        count = 0

        for i in range(256):
            for j  in range(512):
                if j % 2 == 0:
                    reducedData.append(ImgRawData[j + count])
            count = count + 1024 
        return reducedData
    
    def headerWidthAndHeightChange(inputlist, lenOfRawData):
        width = math.floor(lenOfRawData ** 0.5)
        lst = [0,0,0,0]
        for i in range(3, -1, -1):
            tempValue = width
            if width // (256 ** i) != 0:
                tempValue = width - (256 * (width // (256 ** i)))
                lst[i] = width // (256 ** i)
                width = tempValue
            else:
                continue
        for i in range(18, 22):
            inputlist[i] = lst[i - 18]
        for j in range(22, 26):
            inputlist[j] = lst[j - 22]
        return inputlist

    

BMP.mainFunction()
