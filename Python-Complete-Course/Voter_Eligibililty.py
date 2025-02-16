# Voter Eligibility – Check if a person is eligible to vote (must be 18 or older).


print("Voter Eligible or no")
try:
    VoterAge = int(input("Enter your age: "))
    if VoterAge >=18:
        print("You are eligible for voting.")
    else:
        print("You are under age")
except ValueError:
    print("Please Valid Input!!!")