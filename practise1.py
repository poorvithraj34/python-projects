def check_for_word():
    word="poorvith"
    data=True
    line_no=1
    with open("demo.txt") as f:
        while data:
            data=f.read()
            if(word in data):
                print(line_no)
                return
            line_no+=1

            return -1

check_for_word()        
    

    


 