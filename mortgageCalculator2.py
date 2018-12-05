# Name the program source code file mortgageCalculator2.py and submit the required file here in Canvas.
# This assignment is worth 80 points, to be awarded after all labs are successfully completed.
# Submit your assignment as mortgageCalculator2.py making sure you put the ".py" file extension at the end of
# the file name. Submit mortgageCalculator2.py using the "Submit Assignment" button, and use the "File Upload" tab to
# select mortgageCalculator2.py from your computer to send it to the instructor


p = int(input("What is the purchase amount?")) #user inputs amount converted to int

interest = (input("What is annual interest rate? Ex. 5.1% = 5.1, 10% = 10, etc.")) #user inputs rate
interest_f = float(interest) # takes input value of interest and floats it
r = (interest_f/100)/12 # takes annual interest converts to monthly interest rate by dividing by 100, then by 12


years = int(input("What is the length of the loan in years?")) # user inputs years converted to from str to int
n = years * 12 # multiply years by 12 to get total months, assigned to n

c = (p * (1 + r)**n) * r / ((1 + r)**n - 1) # c assigned formula to calculate monthly mortgage

dollars_borrowed = ('%0.0f' % p) # purchase amount formatted 0 decimal points
years_f = ('%0.0f' % years) # years formatted 0 decimal points
dollars_per_month = ('%0.2f' % c) # monthly mortgage formatted to show two following decimal places


p_str = str(dollars_borrowed) # convert dollars_borrowed to str so it can be written to file
interest_str = str(interest) # convert pre-formatted interest to str so it can be written to file
years_str = str(years_f) # convert years formatted to str so it can be written to file
monthly_payment = str(dollars_per_month) # convert dollars_per_month to str so it can be written to file


with open("mortgage_info.txt", "w") as m_info: # open file mortgage_info.txt for writing as variable m_info
    m_info.write("Amount borrowed: " + "$" + p_str + "\n") # writes to file the amount borrowed
    m_info.write("Annual interest rate: " + interest_str + "%" + "\n") # writes to file interest rate
    m_info.write("Payback period: " + years_str + " years" + "\n") # writes years of mortgage to file
    m_info.write("Monthly payment: " + "$" + monthly_payment + "\n") # writes monthly mortgage to file

m_info.close() # close file

