TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print('Electricity Bill Estimator')
tariff_choice = int(input('Which Tariff? 11 or 31?'))
daily_use_kWh = float(input("Enter Daily Use in kWh:"))
number_billing_days = float(input('Enter Numebr of Billing Days:'))
bill = 0

if tariff_choice == 11:
    cents_per_kWh = TARIFF_11
    bill = cents_per_kWh * daily_use_kWh * number_billing_days

elif tariff_choice == 31:
    cents_per_kWh = TARIFF_31
    bill = cents_per_kWh * daily_use_kWh * number_billing_days
print('${:.2f}'.format(bill))
