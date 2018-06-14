# mylist = [1,2,3,4,5]
# for i in mylist:
#     if i>2:
#         print(i)
#
#
# myfile = open ("fruits.txt")
# content = myfile.read()
# myfile.close()
# content = content.splitlines()
# for i in content:
#     print(len(i))
#
#
# def FahrenhiteToCelcius(c):
#     if c < -273.15:
#         return "That temperature doesn't make sense!"
#     else:
#         f = c * 9 / 5 + 32
#         return f
#
# temperatures=[10,-20,-289,100]
#
# for i in temperatures:
#     print(FahrenhiteToCelcius(i))
#
#
# numbers = [1, 2, 3]
# myfile = open("numbers.txt","w")
# for i in numbers:
#     myfile.write(str(i) +"\n")
# myfile.close()
#
# myfile = open("numbers.txt", "r")
# content = myfile.read()
# print(content)
# myfile.close()
#
#
# 
# def FahrenhiteToCelciusWriteInFile(c):
#     if c < -273.15:
#         return "That temperature doesn't make sense!"
#     else:
#         f = c * 9 / 5 + 32
#         return f
#
# temperatures=[10,-20,-289,100]
# with open("result.txt", "w") as myfile:
#     for i in temperatures:
#         result = FahrenhiteToCelciusWriteInFile(i)
#         print(result)
#         if type(result) == int or type(result) == float:
#             myfile.write(str(result)+"\n")
#         # else :
#         #     myfile.write(str(result))


temperatures = [10,-20,-289,100]

def writer(temperatures):
    with open("result.txt", 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c* 9/5 + 32
                file.write(str(f) + "\n")

writer(temperatures)
