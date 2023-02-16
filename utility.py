from string import ascii_lowercase

# Function to print available options in format "a) option"
def validate_option(validation_list, user_input, error_message):
    while True:
        label = input(user_input).strip().lower()
        if label in validation_list:
            return label
        print(error_message)

# Function to check if the input provided from the user is valid
# Takes the input prompt and value, the list where you want to check if the value exists, the error message to display if the input is not valid
def print_options(options_list):
    labeled_options = dict(zip(ascii_lowercase, options_list))
    for label, option in labeled_options.items():
        print(f" {label}) {option}")
    return labeled_options
