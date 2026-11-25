print("Welcome to Sam's Phone Fixing - Nkurenkuru")

phones = ["iPhone", "Samsung", "Tecno", "Huawei"]

print("We fix these phones:")
for phone in phones:
    print("- " + phone)

customer = input("What phone do you have? ")

if customer == "iPhone":
    print("Price is N$500")
elif customer == "Samsung":
    print("Price is N$400")
else:
    print("Price is N$300")

print("Thank you! Come again.")
