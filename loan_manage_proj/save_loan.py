import csv

def save_loan_details(email,interest_rate,repayment_terms,loan_amount):
  fields = ['Email', 'Interest Rate', 'Repayment Terms', 'Loan Amount']
  rows = [email,interest_rate,repayment_terms,loan_amount]
  filename = "loan_records.csv"
  status = 0

  # writing to csv file
  with open(filename, 'w') as csvfile:
      # creating a csv writer object
      csvwriter = csv.writer(csvfile)

      # writing the fields
      csvwriter.writerow(fields)

      # writing the data rows
      csvwriter.writerows(rows)

      status+=1


  return status