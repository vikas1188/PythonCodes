with open("example.txt", "w") as myfile:
    myfile.write("Something")
# benefit of the code above written over the file related code is
# that this is :
# 1. less code
# 2. if for some reason the code breaks between opening the file and closing the find_in_file
# the file method doesn't close the file descriptor, but `with` code does that work for us
