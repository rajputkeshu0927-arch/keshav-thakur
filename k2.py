contacts={"keshav":"9876543210",
"rahul":"1234567890", 
"john":"5556667777"}
print(contacts)
search_name = input("Enter the name to search: ")
if search_name in contacts:
    phone_number = contacts[search_name]
    print(f"Phone number of {search_name} is {phone_number}")
else:
    print(f"{search_name} not found in contacts.")