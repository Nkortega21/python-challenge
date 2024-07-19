#Module 3 Bank_main.py

import OS
import CSV

Total_Months = 0
Net_Total = 0
Profit_Losses = []
Monthly_Change = []
months = []
Bank_main = os.path.join("UCI DA Class Folder","python-challenge","PyBank","Resources","budget_data.csv")
with open(Bank_main) as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=",")
	csv_header = next(csv_file)
	print(f"Header: {csv_header}")
	for row in csv_reader:
			print(row)
			Total_Months += 1
			Net_Total += int(row[1])
			Profit_Losses.append(int(row[1]))
			months.append(row[0])
			

for i in range(1,len(Profit_Losses)):
	Monthly_Change.append(Profit_Losses[i]- Profit_Losses[i-1])

Avg_change = sum(Monthly_Change) / len(Monthly_Change)
Rounded_avg_change = round(Avg_change,2)

Gincprof = max(Monthly_Change)
Gdecprof = min(Monthly_Change)

Gincmonth = months[Monthly_Change.index(Gincprof)+1]
Gdecmonth = months[Monthly_Change.index(Gdecprof)+1]

print(f'Financial Analysis\n -----------------------------\n Total Months:  {Total_Months}\n Total: ${Net_Total}\n Average Change {Rounded_avg_change}\n Greatest Increase in Profits: {Gincmonth} ${Gincprof}\n Greatest Decrease in Profits: {Gdecmonth} ${Gdecprof}')