import logging



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
