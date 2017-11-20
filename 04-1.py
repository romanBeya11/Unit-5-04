'''Created by Roman Beya
Created on 20,11,17
Created for ICS3U
This program calculates the average of the elements inside of a list
'''
import ui

marks_of_user = []
sum_of_marks = 0
number_of_marks_entered = 0

def disable_button():
	# Disabling certain buttons to aid with control flow of the program
	view['mark_average_button'].enabled = False
	
def enable_button():
	# Enable certain button to aid with control flow
	view['mark_average_button'].enabled = True

def enter_marks_touch_up_inside(sender):
	# When this button is pressed, the mark will be added to the list
	global number_of_marks_entered
	
	number_of_marks_entered = number_of_marks_entered + 1

	# Convert data type 'string' to data type 'int'
	mark_entered = int(view['user_marks_textfield'].text)
	
	# Adding user input to list
	marks_of_user.append(mark_entered)
	
	# Record number of times this button has been pressed
	if number_of_marks_entered >= 2:
		enable_button()
	else:
		disable_button()
	
	# Clear screen once they have inputted mark
	view['user_marks_textfield'].text = ''
	
def calculate_mark_average():
	# When this function is handle, the average of the user inputted marks will be calculated
	global sum_of_marks
	
	for mark in marks_of_user:
		sum_of_marks = sum_of_marks + mark
	avg = sum_of_marks / len(marks_of_user)
	return avg
	
def display_mark_average(sender):
	# Will display the mark average of the user
	gpa = calculate_mark_average()
	view['output_label'].text = 'The average of the inputted marks is: ' + str(gpa)
	
	# Disabling the buttons once average has been calculated
	disable_button()
	view['enter_marks_button'].enabled = False
	
view = ui.load_view()
view.present('sheet')
disable_button()
