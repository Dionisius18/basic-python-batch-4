text = input("input text: ")

while True :
    if text =="stop" or text == "end":
        print("prgram has stopped.")
        break
    print("text : {}".format(text))
    text = input("input text lain: ")