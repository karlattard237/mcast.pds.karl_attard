import DataScienceBasics as dsb


def main():
    # Load data from file
    data = dsb.load_data("data.txt")
    
    # Filter out records with score of 100
    new_data = dsb.filter_data(data, lambda x: x.get("score") != 100)
    
    # Deduct 5 points from all players' scores
    new_data = dsb.transform_data(new_data, "score", lambda x: x - 5)
    
    # Calculate mean and median of the score
    scores = [item["score"] for item in new_data]
    mean = dsb.calculate_mean(scores)
    median = dsb.calculate_median(scores)
    stats = (mean, median)
    
    # Print unique player names
    unique_names = dsb.get_unique_values(new_data, "name")
    print("Unique player names:", unique_names)
    
    # Print mean and median
    print(f"Mean score: {mean}")
    print(f"Median score: {median}")
    
    # Aggregate total number of players by age
    age_aggregation = dsb.aggregate_data(new_data, "age", "score")
    print("Total scores by age:", age_aggregation)


if __name__ == "__main__":
    main()