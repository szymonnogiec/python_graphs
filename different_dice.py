import pygal

from die import Die

die_1 = Die()
die_2 = Die(10)

# Make some rolls and store results in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
array_of_labels = []
for value in range(2, 17):
    array_of_labels.append(str(value))

hist.x_labels = array_of_labels
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
