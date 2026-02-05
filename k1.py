marks = [ 85, 92, 78, 90, 88 ,95, 89, 91]
print ("Marks:", marks)
print(f"First 3 marks:{marks[:3]}")
print(f"Last 3 marks:{marks[-3:]}")
highest_mark = max(marks)
lowest_mark = min(marks)
print(f"Highest mark: {highest_mark}")
print(f"Lowest mark: {lowest_mark}")
averaege_mark = sum(marks) / len(marks)
print(f"Average mark: {averaege_mark:.2f}")
      