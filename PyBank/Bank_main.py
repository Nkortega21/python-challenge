#Module 3 Bank_main.py
import OS
import CSV

month_total = 0 #setup counters to 0
net_total = 0
profit_loss = [] #established list for code
mon_change = []
months = []
export_list = [] #established list for export

Bank_main = os.path.join("UCI DA Class Folder","Homework","python-challenge","PyBank","Resources","budget_data.csv") #define import filepath
with open(Bank_main) as csv_file: #open csv file
	csv_reader = csv.reader(csv_file,delimiter=",") #read csv file
	csv_header = next(csv_file) #skip header row
	for row in csv_reader:
			month_total += 1 #add total number of months
			net_total += int(row[1]) #add profit and losses to get net total
			profit_loss.append(int(row[1]))
			months.append(row[0])
			

for i in range(1,len(profit_loss)):
	mon_change.append(profit_loss[i]- profit_loss[i-1]) #calculate monthly change and add it to the list

Avg_change = sum(mon_change) / len(mon_change) #calculate the average change
Rounded_avg_change = round(Avg_change,2) #round change to 2 decimals

Gincprof = max(mon_change) #find greatest increase in profit
Gdecprof = min(mon_change) #find decrease increase in profit

Gincmonth = months[mon_change.index(Gincprof)+1] #find the corresponding months for the increase and decrease in profit
Gdecmonth = months[mon_change.index(Gdecprof)+1]

export_list.append('Financial Analysis') #results for financial analysis
export_list.append('-----------------------------')
export_list.append(f'Total Months:  {month_total}')
export_list.append(f'Total: ${net_total}')
export_list.append(f'Average Change {Rounded_avg_change}')
export_list.append(f'Greatest Increase in Profits: {Gincmonth} ${Gincprof}')
export_list.append(f'Greatest Decrease in Profits: {Gdecmonth} ${Gdecprof}')

output_file = os.path.join("UCI DA Class Folder","Homework","python-challenge","PyBank","Analysis","Financial_Analysis.txt") #define export file path
with open(output_file, 'w') as file:
    for line in export_list:
        file.write(line + "\n") #write a new line for each item in the export list