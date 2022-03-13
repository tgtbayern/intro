from xml.etree.ElementTree import QName


isRunning=True
while(isRunning):
    message=input("Do you wanna quit?")
    if(message.lower()=='q'):
        isRunning=False
