import json
from typing import List, Dict, Callable, Set, Any


def calculate_mean(numbers: List[float]) -> float:
    """
    Calculate the mean (average) of a list of numbers.
    
    Parameters:
        numbers (List[float]): List of numerical values.
        
    Returns:
        float: Mean of the numbers.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_median(numbers: List[float]) -> float:
    """
    Calculate the median of a list of numbers.
    
    Parameters:
        numbers (List[float]): List of numerical values.
        
    Returns:
        float: Median of the numbers.
    """
    if not numbers:
        return 0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]


def load_data(filename: str) -> List[Dict[str, Any]]:
    """
    Load JSON data from a file where each line is a JSON dictionary.
    
    Parameters:
        filename (str): Path to the file containing JSON lines.
        
    Returns:
        List[Dict[str, Any]]: List of dictionaries parsed from the file.
    """
    data = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


def filter_data(dataset: List[Dict[str, Any]], condition: Callable[[Dict[str, Any]], bool]) -> List[Dict[str, Any]]:
    """
    Filter the dataset using a lambda or any callable condition.
    
    Parameters:
        dataset (List[Dict[str, Any]]): List of data records (dictionaries).
        condition (Callable): A function returning True/False for each item.
        
    Returns:
        List[Dict[str, Any]]: Filtered list of dictionaries.
    """
    return [item for item in dataset if condition(item)]


def get_unique_values(dataset: List[Dict[str, Any]], key: str) -> Set[Any]:
    """
    Get unique values for a specified key in the dataset.
    
    Parameters:
        dataset (List[Dict[str, Any]]): List of data records.
        key (str): Key for which to find unique values.
        
    Returns:
        Set[Any]: Set of unique values.
    """
    return set(item[key] for item in dataset if key in item)


def transform_data(dataset: List[Dict[str, Any]], key: str, transform: Callable[[Any], Any]) -> List[Dict[str, Any]]:
    """
    Transform values of a specific key in the dataset using the transform function.
    
    Parameters:
        dataset (List[Dict[str, Any]]): List of data records.
        key (str): Key whose values should be transformed.
        transform (Callable): Function applied to each value.
        
    Returns:
        List[Dict[str, Any]]: Dataset with transformed values.
    """
    for item in dataset:
        if key in item:
            item[key] = transform(item[key])
    return dataset


def describe_data(dataset: List[Dict[str, Any]], key: str) -> None:
    """
    Calculate and print mean and median for the numerical data associated with the key.
    
    Parameters:
        dataset (List[Dict[str, Any]]): List of data records.
        key (str): Key for numerical data.
    """
    values = [item[key] for item in dataset if key in item and isinstance(item[key], (int, float))]
    mean = calculate_mean(values)
    median = calculate_median(values)
    print(f"Mean of {key}: {mean}")
    print(f"Median of {key}: {median}")


def aggregate_data(dataset: List[Dict[str, Any]], key1: str, key2: str) -> Dict[Any, float]:
    """
    Aggregate data by summing the values of key2 grouped by unique values of key1.
    
    Parameters:
        dataset (List[Dict[str, Any]]): List of data records.
        key1 (str): Key to group by.
        key2 (str): Key whose values to sum.
        
    Returns:
        Dict[Any, float]: Dictionary with key1 unique values and summed key2 values.
    """
    aggregation = {}
    for item in dataset:
        if key1 in item and key2 in item:
            aggregation[item[key1]] = aggregation.get(item[key1], 0) + item[key2]
    return aggregation