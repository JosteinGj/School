def read_form_file(filename):
    file=open(filename)
    innhold=file.read()
    return innhold
def remove_symbols(text):
    text=list(text)
    output=[]
    for i in text:
        if i.isalpha() or i==" ":
            output.append(i)
    output="".join(output)
    return output
print(remove_symbols("123cx XDF¤d ¤&d f & b      .b ,bbbbb,\nbv.a,"))
def count_word(filename):
    text=remove_symbols(read_form_file(filename))
    wordlist=text.split()
    wordcounter={}
    for i in wordlist:
        wordcounter[i]=wordlist.count(i)
    return wordcounter
bible_dict=count_word("bible.txt")
for word,count in bible_dict.items():
    print(word,count)



