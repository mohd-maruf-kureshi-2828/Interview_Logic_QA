# ============================================================
# PYTHON FUNCTIONS - BASICS
# ============================================================


# ============================================================
# What is a Function?
# ============================================================

# A function is a reusable block of code
# that performs a specific task.
#
# Simple meaning:
# Ek particular kaam ke code ko function ke andar rakhte hain.
# Jab zarurat ho, function ko call karte hain.


# ============================================================
# Basic Syntax
# ============================================================

# def function_name():
#     code


# ============================================================
# Example 1: Simple Function
# ============================================================

def greet():
    print("Hello Bhai")


# Function call
greet()

# Output:
# Hello Bhai


# ============================================================
# How it works
# ============================================================

# def
# -> Function banane ke liye use hota hai.
#
# greet
# -> Function ka naam.
#
# ()
# -> Parameters yahan likhe ja sakte hain.
#
# :
# -> Function ka code start hota hai.
#
# print()
# -> Function ka actual kaam.
#
# greet()
# -> Function ko call/run karta hai.


# ============================================================
# Function Define vs Function Call
# ============================================================

# Define = Function banana

def hello():
    print("Hello")


# Call = Function chalana

hello()


# ============================================================
# Example 2: Function ko multiple times call karna
# ============================================================

def welcome():
    print("Welcome")


welcome()
welcome()
welcome()

# Output:
# Welcome
# Welcome
# Welcome


# ============================================================
# Why do we use Functions?
# ============================================================

# 1. Code reuse
# 2. Same code baar-baar likhne ki zarurat nahi
# 3. Code ko organize karne me help karta hai
# 4. Code ko easy to understand banata hai


# ============================================================
# Example 3: Reusable Function
# ============================================================

def say_hello():
    print("Hello")


say_hello()
say_hello()

# Output:
# Hello
# Hello


# ============================================================
# Function Naming
# ============================================================

# Function ka naam meaningful rakhna chahiye.

# Good:
#
# def calculate_total():
#     pass
#
# def get_name():
#     pass
#
# def print_message():
#     pass


# ============================================================
# Function with no parameter
# ============================================================

def message():
    print("Python is easy")


message()

# Output:
# Python is easy


# ============================================================
# INTERVIEW QUESTIONS
# ============================================================

# Q1. What is a function in Python?
#
# Answer:
# A function is a reusable block of code
# that performs a specific task.


# Q2. Which keyword is used to create a function?
#
# Answer:
# The "def" keyword is used to create a function.


# Q3. How do you call a function?
#
# Answer:
# We call a function by writing its name followed by ().
#
# Example:
#
# greet()


# Q4. Does defining a function execute it?
#
# Answer:
# No.
# We need to call the function to execute it.


# Q5. Why are functions useful?
#
# Answer:
# Functions help us reuse code and organize our program.


# ============================================================
# EASY MEMORY
# ============================================================

# def     = function banana
#
# name    = function ka naam
#
# ()      = parameters ke liye
#
# call()  = function ko run karna
#
#
# Example:
#
# def greet():
#     print("Hello")
#
# greet()


# ============================================================
# FUNCTION BASIC FLOW
# ============================================================

# Function define
#       ↓
# def greet():
#       ↓
# Function call
#       ↓
# greet()
#       ↓
# Code execute
#       ↓
# Hello


# ============================================================
# BASIC FUNCTION COMPLETE ✅
# ============================================================