print("---Quiz Question Creator---")
 
# Choose between entering a question or exiting the program
while True:
    print("\nMenu:")
    print("1. Enter a question")
    print("2. Exit the program")

    choice = input("\nEnter your choice (1 or 2): ")
    
    if choice == "1":
        print("\nChoose a category for the quiz (Math, English, Science, Filipino)")
        category = input("Enter the category: ").lower() # To lower every entered category

        if category not in ["math", "english", "science", "filipino"]: 
            print("\nInvalid category. Choose from Math, English, Science, or Filipino.")
            continue

        file_name = f"{category}.txt"
        
        num = int(input("\nHow many question/s do you want to enter?"))

        for i in range(num):
            print(f"\nQuestion {i + 1} of {num}")
            question = input("Enter the question: ")

    if choice == "2":
        print("\nExiting the program... The entered data saved.")
        break 

    else:
        print("\nInvalid input. Choose between 1 or 2.")