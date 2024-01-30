def solution(nums, target):
    # Example function - you can modify it as per your requirement
    print("Received numbers:", nums)
    print("Received target integer:", target)
    # Add your solution logic here
    hashtable = {i:nums[i] for i in range (len(nums))}

    for i in range(len(nums)):
        current_num = nums[i]
        check = target-current_num
        print_key_for_value(hashtable, check, i)




def print_key_for_value(hashtable, target_value, current_index):
    for key, value in hashtable.items():
        if value == target_value:
            print(f"Current Index: {current_index}")
            print(f"Key for the value {target_value}: {key}")
            break


def get_input():
    # Get a list of numbers from the user
    nums_input = input("Enter numbers separated by spaces: ")
    # Convert the string input into a list of integers
    nums = list(map(int, nums_input.split()))

    # Get an integer from the user
    target_input = input("Enter an integer: ")
    # Convert the string input into an integer
    target = int(target_input)

    return nums, target

def main():
    nums, target = get_input()
    solution(nums, target)

if __name__ == "__main__":
    main()
