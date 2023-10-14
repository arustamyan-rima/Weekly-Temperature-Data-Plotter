# Weekly Temperature Data Plotter

This project involves processing a text file that contains weekly temperature data and creating a plot of the temperatures. The script parses the data, creates a dictionary with temperature lists, and generates a plot using the matplotlib library.

### Project Structure

- The main script is named `weekly_temperature_data_plotter.py`.
- A text file named `wetterdaten.txt` is used as the input file.
- The script includes functions for reading the file, parsing the data, creating a dictionary, and plotting the data.
- The `matplotlib` library is used for generating the plot.

### Usage

Ensure you have the necessary libraries installed to run the code. You can run the script using Python.

The script will read the data from the text file, process it, and generate a plot of the weekly temperatures.

### Functions  
The script includes the following functions:  

get_data_list: Opens a file and returns its content as a list.  
parse_row: Splits a row at spaces and parses elements, returning the week and a list of numeric temperature values.  
get_data_dict: Creates a dictionary with temperature lists from the input data list.  
plot_data: Plots the weekly temperatures using the matplotlib library.  
