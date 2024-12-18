
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
        for i in data:
          if isinstance(i, list):
            return sum(i)
          



result = calculate_structure_sum(data_structure)
print(result)