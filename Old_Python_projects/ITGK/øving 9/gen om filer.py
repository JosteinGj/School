def write_to_file(data):
    file= open("my_file.txt","w")
    file.write(data)
    file.close()
def read_from_file(filename):
    f= open(filename,"r")
    innhold=(f.read())
    f.close()
    print(innhold)
write_to_file("test")
read_from_file("my_file.txt")

def main():
    entry=None
    while entry != "done":
        entry=input("do you want to read or write")
        if entry=="read":
            read_from_file("my_file.txt")
        elif entry=="write":
            write_to_file(input("what do you wanna write"))
main()