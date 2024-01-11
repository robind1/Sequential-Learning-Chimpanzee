import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

######################################first chart################################################################
def create_line_chart(x_values, y_values, x_label, y_label, title):
    data = {'x': x_values, 'y': y_values}
    df = pd.DataFrame(data)

    # Set style
    sns.set(style="white")

    # Plotting the chart
    sns.lineplot(x='x', y='y', data=df, marker='o')

    # Adding labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.xlabel(x_label, fontsize=12)  # Adjust fontsize
    plt.ylabel(y_label, fontsize=12)  # Adjust fontsize
    plt.title(title, fontsize=14, fontweight='bold')  # Adjust fontsize and fontweight
    plt.xticks(x_values, map(int, x_values))  # No decimal

    # Display the chart
    plt.show()


# Input data
x_values = [2, 3, 4, 5, 6]
y_values = [3, 14, 17, 25, 36]

# Customize labels and title
x_label = "Number of Colored Objects"
y_label = "Number of Sessions"
title = "Sessions Needed"

create_line_chart(x_values, y_values, x_label, y_label, title)

######################################second chart################################################################

def create_line_chart(x_values_list, y_values_list, x_label, y_label, title, respondents):
    # Create a DataFrame from the data
    data = {'x': [], 'y': [], 'Respondent': []}

    for i, (x_values, y_values) in enumerate(zip(x_values_list, y_values_list)):
        data['x'].extend(x_values)
        data['y'].extend(y_values)
        data['Respondent'].extend([respondents[i]] * len(x_values))

    df = pd.DataFrame(data)

    # Set the style of seaborn without grid
    sns.set_style("white")

    # Plotting the line chart
    sns.lineplot(x='x', y='y', hue='Respondent', data=df, marker='o')

    # Adding labels and title with custom font properties
    plt.xlabel(x_label, fontsize=10)  # Adjust fontsize
    plt.ylabel(y_label, fontsize=10)  # Adjust fontsize
    plt.title(title, fontsize=12, fontweight='bold')  # Adjust the fontsize and fontweight

    plt.xticks(data['x'], map(int, data['x']))

    # Display the chart
    plt.legend(title='Respondents', loc='upper left')
    plt.show()

# Input data
respondents = ['Monica', 'Chloe', 'Akira']

x_values_list = [
    [2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6]
]

y_values_list = [
    [3, 14, 17, 25, 36],
    [7, 31, 114, 76, 140],
    [15, 32, 56, 36, 55]
]

# Customize labels and title
x_label = "Number of Objects"
y_label = "Number of Sessions Needed"
title = "Sessions Needed"

create_line_chart(x_values_list, y_values_list, x_label, y_label, title, respondents)