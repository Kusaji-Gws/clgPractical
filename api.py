import logging

# Critical Function: process and double data
def critical_function(data):
    """
    This critical function processes a list of integers, 
    sums the values, and returns the doubled sum.
    
    Args:
        data (list of int): A list of integers to process.

    Returns:
        int: The doubled sum of the integers.
    """
    if not data:
        raise ValueError("Data list cannot be empty")

    total = sum(data)  # Summing the data
    result = total * 2  # Doubling the sum
    return result

# Helper Function: Log error
def log_error(error_message):
    """
    This helper function logs errors with a timestamp.
    
    Args:
        error_message (str): The error message to log.
    """
    logging.basicConfig(filename='app.log', level=logging.ERROR)
    logging.error(f"Error occurred: {error_message}")
    
# Example usage
try:
    data = [10, 20, 30]
    result = critical_function(data)
    print(f"Processed result: {result}")
except ValueError as e:
    log_error(str(e))
    print(f"Error: {e}")
