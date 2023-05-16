import numpy
arr = numpy.array([10,20,30,40,50])
print(arr)

#the array object in NumPy is called ndarray,  it provides so many supporting functions to interact with the array

#to get NumPy version
print(numpy.__version__)

#array function is used to create obejct of ndArray
arr1 = numpy.array([2,6,8,10,4])
print(arr1)
print(type(arr1))

#0 dimension array using NumPy
zerodimarr = numpy.array(107)
print(zerodimarr)
print(zerodimarr.ndim)

onedimarr  = numpy.array(['Dettol','Cinthiol','Hamam'])
print(onedimarr)
print(onedimarr.ndim)

#to determine shape of an array
shp = onedimarr.shape
print(shp)
totalElements = onedimarr.shape[0]
print(totalElements)

#To iterate all the elements of an array
for data in arr:
    print(data)

#Two dimension array
matrix1 = numpy.array([[1,2,3],[4,5,6]])
print(matrix1)
print(matrix1[0][0],matrix1[0][1],matrix1[0][2])
print(matrix1[1][0],matrix1[1][1],matrix1[1][2])

#To iterate two dimension array
print("Traverse/Iterate all the elements of two dimension array")
for row in matrix1:
    for cell in row:
        print(cell)

#To understand difference between Copy and View
#Copy is a new array, view is just a view of the original array

questions = numpy.array([101,302,301,501,401])
questionsCopy = questions.copy()
questionsCopy[0]=10
print(questions)
print(questionsCopy)
print(questions.base)   #returns None if the array owns the data
print(questionsCopy.base)

questionsView = questions.view()
questionsView[0]=1000
print(questions)
print(questionsView)
print(questions.base)   #returns None if the array owns the data
print(questionsView.base) #returns original array object

#To filter array of elements
arrMarks = numpy.array([45,65,90,30,89,30])
qualifieldMarks = arrMarks>40
print(arrMarks)
print(qualifieldMarks)
evenMarks = arrMarks%2==0
print(evenMarks)