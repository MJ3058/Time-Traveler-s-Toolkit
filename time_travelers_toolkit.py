import datetime as dt
from decimal import Decimal as d
import random
import custom_module

# getting date and time
date = dt.date.today()
time = dt.datetime.now().time()
print(f"Today's date: {date}")
print(f"Time: {time}")

# defining base cost
b_cost = d("1000.00")

# getting current year
c_year = dt.date.today().year

# getting target year
t_year = random.randint(1842, 2496)

# list of destinations
locations = ["Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"]

# getting destination based on the locations list
destination = random.choice(locations)
 
# calculate the cost multiplier based on the year difference
difference = abs(c_year - t_year)
multiplier = d(difference) * d("0.05") # 5% increase per year

# calculate final cost and display result
f_cost = b_cost + (b_cost * multiplier)
print(f"The cost of the Time Travel to the year {t_year} is: ${f_cost:.2f}")

# displaying message
print(custom_module.generate_time_travel_message(t_year, destination, f_cost))
