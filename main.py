# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import  random

codes = ("~","`","!","1","@","2","3","#","4","$","5","%","6","^","7","&","8","*","9","(","0",")")
encryptedText = []
some_text = input("Please enter some text : ")
def encryptText(text):
    encodedText = ""
    for index,ch in enumerate(some_text):
        ind = random.randint(0, len(codes) - 1)
        encryptedText.append({codes[ind] : {index : ch}})
        encodedText = encodedText + codes[ind]
    return encodedText

def decryptText(encodedText):
    decodedText = ""
    for ind, ch in enumerate(encodedText):
      decodedText = decodedText + encryptedText[ind][ch][ind]
    return decodedText

encodedText = encryptText(some_text)
print(encodedText)
print(decryptText(encodedText))