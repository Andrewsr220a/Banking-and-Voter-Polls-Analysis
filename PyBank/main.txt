import os
import csv
import math

budget_data = os.path.join('Resources', 'budget_data.csv')

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(type(budget_data))
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    months = []
    month_count = 0
    average_list = []
    average_change = 0
    pre_value = 0
    value_count = 0

    for i in csvreader:
        months, value = i
        value = float(value)

        monthly_change = value - pre_value
        average_list.append(monthly_change)
        average_change += monthly_change
        month_count += 1
        value_count += value
        pre_value = value

        # greatest_increase = max(average_list))
        # greatest_decrease = min(average_list)

print(month_count)
print(value_count)
print(monthly_change / month_count)
print(max(average_list))
print(min(average_list))
# print(months, value, monthly_change)
# print(average_list)
