
employee_info = (101, "Aravind", "Engineering")
roles = {"editor", "viewer", "admin"}

print(f"ID: {employee_info[0]}")
print(f"Name: {employee_info[1]}")
print(f"Department: {employee_info[2]}")

if "admin" in roles:
    print("\nAdmin Access: Yes")
else:
    print("\nAdmin Access: No")