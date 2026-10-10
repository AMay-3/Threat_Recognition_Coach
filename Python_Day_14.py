IT_Team = "TCR IT"
TCR_Employee_Email_List = ["sam.tcr@tcr.com", "aaron.tcr@tcr.com", "joseph.tcr@tcr.com"]
Official_TCR_Domain = "@tcr.com"
Official_TCR_Employees = ["sam", "aaron", "joseph"]
Phishing_Target_Email_List = ["tcg.official@tcg.com", "tcb.official@tcb.com", "tcr.official@tcr.com"]
def get_outcome(selected_choice):
    if selected_choice == "2":
        return("Safe Response")
    elif selected_choice == "1":
        return("Risky Response")
def show_summary(record):
    print("Training session summary:")
    print("Email:", record["Email"], "\nChoice:", record["choice"], "\nOutcome:", record["Outcome"], "\nInvalid attempts:", record["invalid_attempts"], "\nScenario ID:", record["scenario_id"], "\nCompletion Status:", record["completion_status"]) 
def main():
    Training_Records = []
    User_Email = input("Enter your email address: ")
    scenario_id = "account_expiration_001"
    while User_Email not in TCR_Employee_Email_List:
        print("Email is not associated with training roster")
        User_Email = input("Enter valid email address:")
    if User_Email in TCR_Employee_Email_List:                                                                                                    
        print("This is an official message from", IT_Team, " WARNING!! Your account credentials have expired! "                                  
          "Your account will be disabled if you do not sign in immediately through the following link: [INSERT_LINK_HERE]. "  
          "Please sign in immediately!! to avoid account suspension. Thank you for your prompt attention to this matter. -", IT_Team)
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
    Outcome = get_outcome(Response)
    if Outcome == "Safe Response":
        print("You chose to contact IT through a known, trusted contact method. This is the safer option because it allows you to independently verify the legitimacy of the message and avoid potential phishing attacks.")
    elif Outcome == "Risky Response":
        print("You chose to open the message's link and sign in. This is risky because it could lead to a phishing site that steals your credentials.")
    print("Accepted choice:", Response)
    print("Invalid attempts:", invalid_attempts)
    completion_status = "Complete"
    Training_Summary = {"Email": User_Email, "choice": Response, "Outcome": Outcome, "invalid_attempts": invalid_attempts, "scenario_id": scenario_id, "completion_status": completion_status}
    Training_Records.append(Training_Summary)
    show_summary(Training_Records[0])
    return(Training_Records)
if __name__ == "__main__":
    completed_records = main()
    print("Completed Records:" ,len(completed_records))