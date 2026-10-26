#Enrollment no. : 92600584055
#Name: Aditi Arun Mane

print("===================================================")
print("          CAREER GUIDANCE SYSTEM")
print("===================================================")

print("Answer the following questions with yes or no.")

coding = input("Do you like coding? ").lower()
maths = input("Do you like mathematics? ").lower()
biology = input("Do you like biology? ").lower()
drawing = input("Do you like drawing? ").lower()

print("\n====== Career Suggestion ======")

if coding == "yes" and maths == "yes":
    print("Suggested Career: Software Engineer / Computer Scientist")
elif biology == "yes":
    print("Suggested Career: Doctor / Medical Scientist")
elif drawing == "yes":
    print("Suggested Career: Graphic Designer / Architect")
elif maths == "yes":
    print("Suggested Career: Engineer / Mathematician")
else:
    print("Suggested Career: Explore different career options")

print("\nThank you for using the Career Guidance Expert System!")
