import pandas as pd

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                self.table[index][i] = (key, value)
                break
        else:
            self.table[index].append((key, value))
        
        # Save data to the Excel file immediately after the insertion
        self.save_to_excel()

    def get(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            return self._binary_search(key, self.table[index])
        return None

    def remove(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    break
            # Save data to the Excel file after removal
            self.save_to_excel()

    def save_to_excel(self):
        data = []
        for index in self.table:
            if index is not None:
                data.extend(index)
        df = pd.DataFrame(data, columns=["Key", "Value"])
        df.to_excel("database.xlsx", index=False)

    def load_from_excel(self):
        try:
            df = pd.read_excel("database.xlsx")
            data = df.values
            for key, value in data:
                self.insert(key, value)
        except FileNotFoundError:
            print("The 'database.xlsx' file does not exist.")

    def _binary_search(self, key, key_value_pairs):
        left, right = 0, len(key_value_pairs) - 1
        while left <= right:
            mid = (left + right) // 2
            if key_value_pairs[mid][0] == key:
                return key_value_pairs[mid][1]
            elif key_value_pairs[mid][0] < key:
                left = mid + 1
            else:
                right = mid - 1
        return None

def main():
    size = int(input("Enter the size of the hash table: "))
    hash_table = HashTable(size)

    # Load data from the Excel file if it exists
    hash_table.load_from_excel()

    while True:
        print("\nMenu:")
        print("1. Insert key-value pair")
        print("2. Get value by key")
        print("3. Remove key")
        print("4. Save to Excel")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            hash_table.insert(key, value)
        elif choice == "2":
            key = input("Enter the key: ")
            value = hash_table.get(key)
            if value is not None:
                print(f"Value for key '{key}': {value}")
            else:
                print(f"Key '{key}' not found.")
        elif choice == "3":
            key = input("Enter the key to remove: ")
            hash_table.remove(key)
        elif choice == "4":
            # Save data to Excel when requested
            hash_table.save_to_excel()
            print("Data saved to 'database.xlsx'.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
