# File = open("My_file.txt")
# contents = File.read()
# print(contents)
# File.close()


######################  OR #################
# with open("My_file.txt") as File:
#     contents = File.read()
#     print(contents)

#################### This will delete the former text and save the new one inside #########
# with open("My_file.txt", mode="w") as File:
#     File.write("New text life")

####################### this will only add the new file to old file ##########
# with open("My_file.txt", mode="a") as File:
#     File.write("\nNew text life.")

######################### this will open new file and save the text inside but this only work when you are in the write(w) mode. like this mode="w" ################
with open("new_file.txt", mode="w") as File:
    File.write("Yorube ma ni, Oro ose sor ni fitiler, afe ti ino ba ku.\n"
               "physical contact make more emotion than spiritual interaction, life can be suprizing!!\n"
               "some word are better left on side,")

