class huffmanNode:
    def __init__(self, x, y):
        self.ascii = x
        self.prob = y
        self.Lchild = None
        self.Rchild = None
        self.charCodeword = ""

class sortingArray:
    def sorting(inputLinkedList):
        for i in range(len(inputLinkedList) - 1):
            for j in range(i + 1, len(inputLinkedList)):
                if (inputLinkedList[i].prob > inputLinkedList[j].prob):
                    tempFre = inputLinkedList[j].prob
                    tempAscii = inputLinkedList[j].ascii
                    inputLinkedList[j].prob = inputLinkedList[i].prob
                    inputLinkedList[j].ascii = inputLinkedList[i].ascii
                    inputLinkedList[i].prob = tempFre
                    inputLinkedList[i].ascii = tempAscii
                else:
                    continue
        return inputLinkedList

class encoding:
    def encodingCodebook(huffmanSorting):
        huffmanTable = [""] * 128
        for i in range(len(huffmanSorting)):
            if huffmanSorting[i].ascii != -1:
                huffmanTable[huffmanSorting[i].ascii] = huffmanSorting[i].charCodeword
            else:
                continue
        return huffmanTable
    # Line 24~32 : Codebook

    def encodingString(huffmanTable, inputString):
        encodedString = ""
        for i in range(len(inputString)):
            encodedString = encodedString + huffmanTable[ord(inputString[i])]
        return encodedString
    # Line 35~39 : Codebook轉成編碼字串

    def encodingBinaryFile(huffmanSorting, encodedString):
        CodedSeqInAscii = []
        if len(encodedString) % 8 != 0:
            extraStr = huffmanSorting[0].charCodeword[0 : 8 - (encodedString % 8)]
            encodedString = encodedString + extraStr

        for i in range(0, len(encodedString) - 1, 8):
            tmp_str2hexnum = encodedString[i : i + 8]
            CodedSeqInAscii.append(int(tmp_str2hexnum, 2))
        return CodedSeqInAscii
    
    def exportBinaryFile(CodedSeqInAscii):
        outData = bytes(CodedSeqInAscii)
        file = open("HuffmanCode.txt", 'wb')
        file.write(outData)
        file.close()
    # Line 53~57 : output file

def main():
    opts = input("輸入指令: " + "\n" + "0 : 使用內建檔案編碼" + "\n" + "1 : 匯入txt檔案編碼 Ex:data.txt" + "\n")
    data = ""
    
    if opts == "0":  
        data = "In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression. The process of finding and/or using such a code proceeds by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper 'A Method for the Construction of Minimum-Redundancy Codes'.[1] The output from Huffman's algorithm can be viewed as a variable-length code table for encoding a source symbol (such as a character in a file). The algorithm derives this table from the estimated probability or frequency of occurrence (weight) for each possible value of the source symbol. As in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols. Huffman's method can be efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted.[2] However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among all compression methods."
    elif opts == "1":
         fileName = input("請匯入檔案名稱: ")
         file = open(fileName, "r")
         data = file.read()
    else:
        print("請輸入有效指令!")

    charMatrix = []
    for i in range(128):
        charMatrix.append(0)

    for i in range(len(data)):
        index = ord(data[i])
        charMatrix[index] = charMatrix[index] + 1

    for i in range(len(charMatrix)):
        charMatrix[i] = charMatrix[i] / len(data)
        
    Huffman = []

    for i in range(len(charMatrix)):
        newNode = huffmanNode(i, charMatrix[i])
        Huffman.append(newNode)

    huffmanSorting = sortingArray.sorting(Huffman) 

    treeIndicator = 0
    tempProb = 0
    while(tempProb != 1):
        tempProb = huffmanSorting[treeIndicator].prob + huffmanSorting[treeIndicator + 1].prob
        newNode = huffmanNode(-1, tempProb)
        newNode.Lchild = huffmanSorting[treeIndicator]
        newNode.Rchild = huffmanSorting[treeIndicator + 1]
        insertIndex = len(huffmanSorting)
        for i in range(len(huffmanSorting) - 1, -1, -1):
            # print(tempProb)
            if huffmanSorting[i].prob > tempProb:
                insertIndex = i
                continue
            else:
                break
        huffmanSorting.insert(insertIndex, newNode)
        treeIndicator = treeIndicator + 2
        # print(treeIndicator, len(huffmanSorting))

    for i in range(len(huffmanSorting) - 1, -1, -1):
        if huffmanSorting[i].ascii == -1:
            huffmanSorting[i].Lchild.charCodeword = huffmanSorting[i].charCodeword + '0'
            huffmanSorting[i].Rchild.charCodeword = huffmanSorting[i].charCodeword + '1'
        else:
            continue
    # Line 111~116 : Huffman Codeword

    huffmanTable = encoding.encodingCodebook(huffmanSorting)
    # Line 119 : Codebook
    encodingString = encoding.encodingString(huffmanTable, data)
    # Line 121 : 編碼字串
    CodedSeqInAscii = encoding.encodingBinaryFile(huffmanSorting, encodingString)
    # Line 123 : 轉成2進位
    print(CodedSeqInAscii)
    encoding.exportBinaryFile(CodedSeqInAscii)

if __name__ == '__main__':
    main()



