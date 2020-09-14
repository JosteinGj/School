def make_board(filename):
    file=open(filename)
    board=file.readlines()
    output=[]
    for i in board:
        row=i.split(",")
        output.append(row)
    return output
print(make_board("test.txt"))