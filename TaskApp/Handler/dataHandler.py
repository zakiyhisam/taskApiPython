def mapData(data, cls):
    dataList = []
    for d in data:
        mappedPost = cls.create_from_j(d)
        dataList.append(mappedPost)
    return dataList
def filterData(dataList, field, value):
    returnData = []
    valueType = type(value)
    isValid = checkInput(value, valueType)
    if isValid:
        for data in dataList:
            dataValue = getattr(data, field)
            if valueType == int:
                if dataValue == value:
                    returnData.append(data)
            elif valueType == str:
                if value in dataValue:
                    returnData.append(data)
    else:
        returnData = dataList
    return returnData

def checkInput(value, valueType):
    if valueType == int:
        if value == 0:
            return False
    if valueType == str:
        if value == "" or value.isspace():
            return False
    if value == None:
        return False
    return True
	