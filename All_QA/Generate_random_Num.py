import random

# random module ko import kiya
# random numbers generate karne ke liye use hota hai

num = random.randint(1, 10)

# randint(1, 10) → 1 se 10 ke beech koi bhi random number
# Example: 4, 7, 1, 10 etc.

print("Your number is", num)

# generated random number ko print karega




# Interview Questions

# Q1. Why do we use the random module?
# Answer: We use the random module to generate random numbers.

# Q2. What does randint() do?
# Answer: randint() generates a random integer in the given range.

# Q3. What does random.randint(1, 10) do?
# Answer: It generates a random number from 1 to 10.

# Q4. Can randint(1, 10) generate 11?
# Answer: No, it cannot generate 11.

# Q5. How to generate a random number from 1 to 100?
# Answer:

num = random.randint(1, 100)

# 1 and 100 both are included.

# Q6. Will the same number come every time?
# Answer: No, a different random number can be generated each time.

# Q7. What type of value does randint() return?
# Answer: It returns an integer.

# Q8. What is the difference between random and randint()?
# Answer: random is the module and randint() is a function inside it.

# Remember:
# random = module
# randint() = function
# randint(1, 10) = 1 to 10, both included