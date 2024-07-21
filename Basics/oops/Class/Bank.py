#create a class bank every bank should have some name and the bank should provide 
# the loan facility for the home loan . A bank should provide 12% of interest with theprincipal amount of 
# 1lakh . For the education loan bank provides 10% of interest with the principal amount of 
# 50k rupees 
# There are 2 banks from where we can avail the loan facility.
#provide the rate and time for rate and time for any specific type of loan 
#and do compare  which particular bank is better to avail the loan facility


# Solution

#SOLUTION
#create a class bank
#create a function that can calculate the interest on the basis of rate and time
#create a function of the loan types and calculate the actual amount on the basis of above mentioned interst
#ask the user to input the rate and time for a class object to check the final amount
#compare the final amount of both the banks and provide the decision for minimum amount





class Bank:
    def __init__(self, name):
        self.name = name
        self.home_loan_principal = 100000  # Principal amount for home loan
        self.education_loan_principal = 50000  # Principal amount for education loan
        self.home_loan_interest_rate = 12  # 12% interest for home loan
        self.education_loan_interest_rate = 10  # 10% interest for education loan
    
    def calculate_interest(self, principal, rate, time):
        # Simple interest formula: SI = P * R * T / 100
        return (principal * rate * time) / 100
    
    def calculate_loan_amount(self, loan_type, rate, time):
        if loan_type == "home":
            principal = self.home_loan_principal
            interest = self.calculate_interest(principal, rate, time)
        elif loan_type == "education":
            principal = self.education_loan_principal
            interest = self.calculate_interest(principal, rate, time)
        else:
            raise ValueError("Invalid loan type. Choose 'home' or 'education'.")
        total_amount = principal + interest
        return total_amount

# Create two bank objects
bank1 = Bank("Bank A")
bank2 = Bank("Bank B")

# Input rate and time for a specific type of loan
loan_type = input("Enter loan type ('home' or 'education'): ").lower()
rate = float(input("Enter interest rate (as a percentage): "))
time = float(input("Enter time period (in years): "))

# Calculate the total loan amount for both banks
bank1_total_amount = bank1.calculate_loan_amount(loan_type, rate, time)
bank2_total_amount = bank2.calculate_loan_amount(loan_type, rate, time)

# Print the results
print(f"\nTotal amount to be paid for {loan_type} loan in {bank1.name}: {bank1_total_amount}")
print(f"Total amount to be paid for {loan_type} loan in {bank2.name}: {bank2_total_amount}")

# Compare which bank is better for the specific type of loan
if bank1_total_amount < bank2_total_amount:
    print(f"\n{bank1.name} offers a better {loan_type} loan.")
else:
    print(f"\n{bank2.name} offers a better {loan_type} loan.")
