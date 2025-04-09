print("---Quiz Question Creator---")
 
# Choose between entering a question or exiting the program
while True:
    print("\nMenu:")
    print("1. Enter a question (or another question/s)")
    print("2. Exit the program")

    choice = input("\nEnter your choice (1 or 2): ")
    
    if choice == "2":
        print("\nExiting the program... The entered data saved.")
        break 

    # Ask the user what category the question belongs to
    if choice == "1":
        print("\nChoose a category for the quiz (Math, English, Science, Filipino)")
        category = input("Enter the category: ").lower() # To lower every entered category

        if category not in ["math", "english", "science", "filipino"]: 
            print("\nInvalid category. Choose from Math, English, Science, or Filipino.")
            continue

        file_name = f"{category}.txt"
        
        # Ask the user how many question/s do they want to enter)
        num = int(input("\nHow many question/s do you want to enter? "))
        
        # Ask the user for the question/s, choices and its correct answer/s
        for i in range(num):
            print(f"\nQuestion {i + 1} of {num}")
            question = input("Enter the question: ")
            choice_a = input("Enter the choice a: ")
            choice_b = input("Enter the choice b: ")
            choice_c = input("Enter the choice c: ")
            choice_d = input("Enter the choice d: ")
            correct_answer = input("What is the correct answer (a, b, c, d)? ")
    
            # Storing the entered data by the user
            saving_file = open(file_name, "a")
            saving_file.write(f"Question: {question}\n")
            saving_file.write(f"a) {choice_a}\n")
            saving_file.write(f"b) {choice_b}\n")
            saving_file.write(f"c) {choice_c}\n")
            saving_file.write(f"d) {choice_d}\n")
            saving_file.write(f"Correct answer: {correct_answer}\n")
            saving_file.write("-----\n")
            saving_file.close()

            print(f"\nThe entered question/s saved to {file_name}!")

    else:
        print("\nInvalid input. Choose between 1 or 2.")

print("Thank you!")