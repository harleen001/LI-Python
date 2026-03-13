import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

    # define the x-data, which is square footage of a home
x = [2100, 2378, 1983, 1422, 2764, 1901, 1198, 1785, 1556, 2931, 3071, 1688]

    # define the y-data, which is the corresponding home price in 000
y = [390, 427, 350, 285, 479, 299, 250, 310, 290, 495, 515, 284]

    # define the z-data, which is the corresponding distance from city center
z = [4.8, 0.5, 0.9, 1.5, 0.8, 4.2, 3.1, 0.1, 2.2, 1.5, 4.1, 0.7]

    # use the scatter function to generate a time series graph
    # specify that the color of the data point will be based on revenue (y)
    # specify the hot color palette
plt.scatter(x, y, c = z, cmap='hot')

    # also plot a color bar so user can interpret the color scale
plt.colorbar()

    # Add a title using the title function
plt.title("Home Price versus Square Footage (Color = Miles from Center City)")

    # Add labels to the x and y axes by using xlabel and ylabel functions
plt.xlabel("Square Footage")
plt.ylabel ("Home Price $000")

    # Define a function to format the ticks with commas as thousands separators
def format_ticks(value, tick_number):
    return f'{value:,.0f}'

    # Apply the custom formatter to the x-axis
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_ticks))