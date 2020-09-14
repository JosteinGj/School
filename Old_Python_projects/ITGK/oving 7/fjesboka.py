def add_data(user):
    data=user.split()
    data[2]=int(data[2])
    return data
print(add_data("Jostein Gjesdal 20 Mann Singel"))
def get_person(given_name,facebook):
    for n in facebook:
        if n[0]==given_name:
            print(n)
def main():
    facebook=[]
    entry=None
    while True:
        entry=input("add a new user: ")
        if entry=="done":
            break
        new_user=add_data(entry)
        print(new_user)
        facebook.append(new_user)
    print(facebook)
    entry=None
    while entry != "done":
        entry=input("let etter brukere i databasen")
        get_person(entry,facebook)
main()


