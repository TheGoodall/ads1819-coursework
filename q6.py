def hybridsort(data):
    def merge(data1, data2):
        output = []
        while data1 and data2:
            if data1[0] > data2[0]:
                output.append(data2.pop(0))
            else:
                output.append(data1.pop(0))
        while data1:
            output.append(data1.pop(0))
        while data2:
            output.append(data2.pop(0))
        return output

    def mergesort(data):
        data1 = data[:len(data)//2]
        data2 = data[len(data)//2:]

        data1 = hybridsort(data1)
        data2 = hybridsort(data2)

        return merge(data1, data2)
    def selectionsort(data):
        output = []
        while data:
            smallest = [data[0], 0]
            for i, item in enumerate(data):
                if item < smallest[0]:
                    smallest = [item, i]
            output.append(data.pop(smallest[1]))
        return output

    if len(data) > 4:
        return mergesort(data)
    else:
        return selectionsort(data)

print(hybridsort([4,6,2,7,5,34,2,2,3,5]))
