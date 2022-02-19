# Starting with users that need to be verified,
# and an empty list to hold confirmed_users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verifying each user until there are no more unconfirmed users.
# Then moving each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)


print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(f"\t{confirmed_user.title()}")