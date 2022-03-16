def converts(celcius):
    result=celcius*9/5+32
    return result
if __name__ == "__main__":
    while(True):
        message=input("Input the celcius or q for quit")
        if(message.lower()=='q'):
            print("quit")
            break
        message1=int(message)
        print("The result is",converts(message1))
