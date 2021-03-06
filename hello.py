isLoading = False

c = input("Loading? : ")

if c == "Yes":
    isLoading = True
else:
    isLoading = False

if isLoading == True:
    print("Sedang Loading")
else:
    print("Tidak Loading")