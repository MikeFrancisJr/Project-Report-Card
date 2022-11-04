################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")
  print()

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

################ Main Program ################

# Define the student's overall letter grade
def letterGrades(name, dictionary):

  # Create a variable to count the number of grades added to the list
  countGrade = 0

  # Create a variable to collect the total sum of all grades for each student
  sum = 0

  # Create a for loop to loop through all the student grades in the dictionary
  for grade in dictionary[name]:

    # count the number of grades added for each student
    countGrade += 1

    # Collect the sum of each student's grades
    sum += grade

  # Calculate the average of each student's grades
  averageGrade = sum / countGrade

  # If the average grade is 90 or higher, student gets an 'A'
  if(averageGrade >= 90):
    letter = "A"

  # If 80 or higher, a 'B'
  elif(averageGrade >= 80):
    letter = "B"

  # If 70 or higher, a 'C'
  elif(averageGrade >= 70):
    letter = "C"

  # If 60 or higher, a 'D'
  elif(averageGrade >= 60):
    letter = "D"

  # If less than 60, a 'F'
  elif(averageGrade < 60):
    letter = "F"

  # Show the user the student's name and letter grade
  print(f"{name}'s letter grade is {letter}")
  print()
  
# Display title message and option choices
print("~ TEACHER GRADE TRACKER ~")
print()
print("Welcome to UMBC's grading system service.  Today you will analyze and manage")
print("your student's grades using the options below:")
print()

# Prompt the user to pick an option
choice = ""

# Create an empty dictionary to hold student's names and grades
studentDict = {}

# Loop through the option choices until the user picks option 6
while(choice != "6"):
  
  displayMenu()
  choice = input("Select an option: ")
  print()
  
  # If user picks option 1, add student's name to the dictionary
  if(choice == "1"):
    
    # Prompt user to enter a student's name and display the name
    name = input("Enter student's name: ")
    name = name.capitalize()

    # Create an empty list for the dictionary to hold the student's grades
    studentDict[name] = []
    
    # Display the name added
    print(f"{name} added!")
    print()

  # If user picks option 2, remove the student's name for the dictionary
  elif(choice == "2"):

    # Prompt the user to enter a name
    removeName = input("Enter student's name: ")
    removeName = removeName.capitalize()

    # If the name isn't in the dictionary, let the user know 
    if(removeName not in studentDict):
      print(f"Sorry, but {removeName} is not in dictionary!")
      print()

    # If it is, remove it
    else:
      studentDict.pop(removeName)
      print(f"{removeName} is removed!")
      print()

  # If the user picks option 3
  elif(choice == "3"):
    
    # Prompt the user to enter a name
    gradeName = input("Enter a student's name: ")
    gradeName = gradeName.capitalize()

    # If student's name is in the dictionary, add the number grade
    if(gradeName in studentDict):
      addGrade = getNumberGradeFromUser()
      studentDict[gradeName].append(addGrade)
      print(f"{addGrade} has been added to {gradeName}'s quizzes")
      print()

    # If it isn't, let the user know
    else:
      print(f"{gradeName} hasn't been added to the dictionary!")
      print()

  # If user picks options 4
  elif(choice == "4"):
    
    #Prompt the user to enter a name
    name4 = input("Enter a student's name: ")
    name4 = name4.capitalize()
    print()

    # If the name is in the dictionary
    if(name4 in studentDict):
      print(f"{name4}'s Quizz Grades:")

      # Loop through and display the student's number grades
      for grade in studentDict[name4]:

        print(grade)
        print()

    # If it isn't, let the user know
    else:
      print(f"Sorry, but {name4} is not in the dictionary!")
      print()

  # If user picks option 5
  elif(choice == "5"):

    # Prompt the user for a name
    name5 = input("Enter a student's name: ")
    name5 = name5.capitalize()

    # If name is in the dictionary, show the letter grade to the user
    if(name5 in studentDict):
      letterGrades(name5, studentDict)

    # If it isn't, let the user know
    else:
      print(f"Sorry, but {name5} is not in the dictionary!")
      print()
  

