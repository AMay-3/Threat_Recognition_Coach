# CHALLENGE 1 — Threat Recognition Coach: input validation
#
# 1. Print this fictional scenario:
#    An unexpected message says your account will be disabled
#    unless you sign in through its link.
#
# 2. Display these options:
#    1. Open the supplied link.
#    2. Contact IT through a known, trusted contact method.
#
# 3. Ask for a choice and store it in response.
# 4. While response is neither "1" nor "2":
#    - Print an invalid-choice message.
#    - Ask again and update response.
# 5. After the loop, print "Accepted choice:" and response.

# CHALLENGE 2 — Count invalid menu answers
# 1. Before the while loop, create invalid_attempts and set it to 0.
# 2. Inside the loop, increase invalid_attempts by 1 each time
#    an invalid answer is rejected, before asking again.
# 3. After the loop, print the count with this label:
#    "Invalid attempts:"

# The following code is a continuation of Python_Day_03.py 

authorized_users = ["aaron", "sam", "aaron"]
new_username = input("Enter another username to add: ")
authorized_users.append(new_username)
print(authorized_users)
unique_users = set(authorized_users)
print(unique_users)
print("Total entries:", len(authorized_users))
print("Unique usernames:", len(unique_users))
IT_Team = "TCR IT"
TCR_Employee_Email_List = ["sam.tcr@tcr.com", "aaron.tcr@tcr.com", "joseph.tcr@tcr.com"]
Official_TCR_Domain = "@tcr.com"
Official_TCR_Employees = ["sam", "aaron", "joseph"]
Phishing_Target_Email_List = ["tcg.official@tcg.com", "tcb.official@tcb.com", "tcr.official@tcr.com"]
User_Email = input("Enter your email address: ")
if User_Email in TCR_Employee_Email_List:                                                                                                    
    print("This is an official message from", IT_Team, " WARNING!! Your account credentials have expired!"                                  
          "Your account will be disabled if you do not sign in immediately though the following link: [INSERT_LINK_HERE]. "  
          "Please sign in immedieatly!! to avoid account suspension. Thank you for your prompt attention to this matter. -", IT_Team)
Trainee_Option_1 = "Open the message's link and sign in."
Trainee_Option_2 = "Contact IT through a known, trusted contact method."
User_Response = input("Choose an option:\n1. " + Trainee_Option_1 + "\n2. " + Trainee_Option_2 + "\nEnter 1 or 2: ")
Response = User_Response
invalid_attempts = 0
while Response != "1" and Response != "2":
    print("Invalid choice. Enter 1 or 2.")
    invalid_attempts = invalid_attempts + 1
    User_Response = input("Choose an option:\n1. " + Trainee_Option_1 + "\n2. " + Trainee_Option_2 + "\nEnter 1 or 2: ")
    Response = User_Response
if Response == "2":
    print("You chose to contact IT through a known, trusted contact method. This is the safer option because it allows you to independently verify the legitimacy of the message and avoid potential phishing attacks.")
elif Response == "1":
    print("You chose to open the message's link and sign in. This is risky because it could lead to a phishing site that steals your credentials.")
else:
    print("Invalid choice. Enter 1 or 2.")

#Current code below

print("Accepted choice:", Response)
print("Invalid attempts:", invalid_attempts)

 