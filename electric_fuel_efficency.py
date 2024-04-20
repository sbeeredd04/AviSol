altitude = 3000# current altitude in meters 1500 - 5000
average_kWh = 1 # 0.1 kilowatt-hours per mile
air_resistance = True

#boieng cora 
intial_kWh = average_kWh
# Calculate electricity consumption based on altitude
if altitude > 2500:
    average_kWh -= altitude * 0.0001 # decrease electricity consumption by 0.0001 kWh per foot of altitude
elif altitude < 2500:
    average_kWh += altitude * 0.0001 # increase electricity consumption by 0.0001 kWh per foot of negative altitude

print(average_kWh)
# Calculate electricity consumption based on air resistance
if air_resistance:
    average_kWh = 1.1 * average_kWh # increase electricity consumption by 0.1 kWh per mile of air resistance


# Print the final average kWh
print("Average kWh:", average_kWh)