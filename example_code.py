# Example code file with intentional bugs for testing

def calculate_average(numbers):
    """Calculate average of numbers - has bugs!"""
    total = sum(numbers)
    average = total / len(numbers)  # Potential division by zero
    return average

def process_data(data):
    """Process data - inefficient and has issues"""
    result = []
    for i in range(len(data)):
        # Inefficient string concatenation
        item = "Item: " + str(data[i]) + " Index: " + str(i)
        result.append(item)
    return result

def database_query(user_id):
    """Simulated database query - has security issue!"""
    # SQL Injection vulnerability!
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    return query

def memory_leak_example():
    """Example with potential memory leak"""
    large_list = []
    for i in range(1000000):
        large_list.append(i)  # Never released
    return len(large_list)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(calculate_average(nums))
    
    data = ['apple', 'banana', 'orange']
    print(process_data(data))
    
    query = database_query(123)
    print(query)
