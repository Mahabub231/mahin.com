temperatures = [28, 32, 35, 31, 29, 30, 33, 36, 27, 25, 34, 30, 29, 37, 38, 26, 31, 35,
                33, 32, 36, 34, 29, 28, 27, 35, 32, 30, 31, 33]

above_32 = [temp for temp in temperatures if temp > 32]

classified_temps = [(temp, "Hot" if temp > 35 else "Warm" if temp >= 30 else "Cool") for temp in temperatures]

average_temp = sum(temperatures) / len(temperatures)
temp_differences = [temp - average_temp for temp in temperatures]

print("Temperatures above 32°C:", above_32)
print("Classified Temperatures:", classified_temps)
print("Temperature Differences from Average:", temp_differences)