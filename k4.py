# 1. Store multiple users in a list of dictionaries
users = [
    {
        "name": "Alice",
        "scores": [80, 90, 85],
        "roles": {"viewer", "editor"}
    },
    {
        "name": "Bob",
        "scores": [70, 75, 80],
        "roles": {"admin", "viewer"}
    }
]

def calculate_user_average(scores_list):
    if not scores_list:
        return 0
    return sum(scores_list) / len(scores_list)

def check_admin_access(roles_set):
    return "admin" in roles_set

def main():
    print("--- User Data Processing ---\n")
    for user in users:
        avg_score = calculate_user_average(user["scores"])
        has_admin = check_admin_access(user["roles"])
        
        print(f"User: {user['name']}")
        print(f"Average Score: {avg_score:.2f}")
        print(f"Admin Access: {'Yes' if has_admin else 'No'}")
        print("-" * 25)

if __name__ == "__main__":
    main()