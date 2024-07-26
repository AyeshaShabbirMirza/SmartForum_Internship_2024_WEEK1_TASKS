import matplotlib.pyplot as plt

# SAMPLE DATA
fruits = ['MANGOES', 'STRAWBERRIES', 'ORANGE', 'GRAPES', 'PEACH']
quantities = [4,12,7,9,2]

# 1. LINE PLOT
print("\n1. LINE PLOT: CREATED LINE PLOT OF FRUIT QUANTITIES")
plt.figure(figsize=(10, 6))
plt.plot(fruits, quantities, marker='o', linestyle='-', color='b')
plt.title('LINE PLOT OF FRUIT QUANTITIES')
plt.xlabel('FRUIT')
plt.ylabel('QUANTITY')
plt.grid(True)
plt.show()

# 2. SCATTER PLOT
print("\n2. SCATTER PLOT: CREATED SCATTER PLOT OF FRUIT QUANTITIES")
plt.figure(figsize=(10, 6))
plt.scatter(fruits, quantities, color='r')
plt.title('SCATTER PLOT OF FRUIT QUANTITIES')
plt.xlabel('FRUIT')
plt.ylabel('QUANTITY')
plt.grid(True)
plt.show()

# 3. BAR PLOT
print("\n3. BAR PLOT: CREATED BAR PLOT OF FRUIT QUANTITIES")
plt.figure(figsize=(10, 6))
plt.bar(fruits, quantities, color='g')
plt.title('BAR PLOT OF FRUIT QUANTITIES')
plt.xlabel('FRUIT')
plt.ylabel('QUANTITY')
plt.grid(True)
plt.show()

# 4. HISTOGRAM
print("\n4. HISTOGRAM: CREATED HISTOGRAM OF FRUIT QUANTITIES")
plt.figure(figsize=(10, 6))
plt.hist(quantities, bins=5, color='purple', edgecolor='black')
plt.title('HISTOGRAM OF FRUIT QUANTITIES')
plt.xlabel('QUANTITY')
plt.ylabel('FREQUENCY')
plt.grid(True)
plt.show()

# 5. PIE CHART
print("\n5. PIE CHART: CREATED PIE CHART OF FRUIT QUANTITIES")
plt.figure(figsize=(8, 8))
plt.pie(quantities, labels=fruits, autopct='%1.1f%%', startangle=140)
plt.title('PIE CHART OF FRUIT QUANTITIES')
plt.show()


