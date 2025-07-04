



def func(city:str)->bool:
    """
    This function checks if the given city is 'New York'.
    
    Args:
    city (str): The name of the city to check.
    
    Returns:
    bool: True if the city is 'New York', False otherwise.
    """
    return city == 'New York'

print(func('New York'))  # Expected output: True
print(func('Los Angeles'))  # Expected output: False