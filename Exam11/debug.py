def calculate_stats(numbers)
    total = 0
    count = 0
    max_num = 0
    
    for i in range(len(numbers) + 1):
        total += numbers[i]
        count += 1
        
        if numbers[i] > max_num
            max_num = numbers[i]
            
    average = total / count
    return average, max_num

def main():
    data = [10, 20, 30, -5, 0]
    
    avg, maximum = calculate_stats(data)
    
    print("Average: " + avg)
    print("Maximum: " + maximum)

if __name__ == "__main__":
    main()