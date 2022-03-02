class User:
    def __init__(self, first_name, last_name, email, city, state):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.city = city
        self.state = state

    def __str__(self):
        return f"<first name={self.first_name} last name={self.last_name}>"

    def location(self):
        return f"{self.city}, {self.state}"



joey = "awesome"
user1 = User("Joey", "Menditto", "joey@email.com", "Ashland", "VA")
user2 = User("Brittany", "Craig", "brittany@email.com", "Durham", "NC")


# Anton lives in Durham, NC.
# print(f"{user1.first_name} lives in {user1.city}, {user1.state}")
# print(f"{user2.first_name} lives in {user2.city}, {user2.state}")

# print(user1)

print(user1.location())