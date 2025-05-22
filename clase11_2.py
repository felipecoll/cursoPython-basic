x = 15
y = 20

if x > 10 and y > 25:       
    print("x is greater than y and less than 30")
elif x > 10 or y > 25:
    print("x is greater than 10 or y is greater than 25")
else:
    print("x is less than 10 and y is less than 25")

is_member = True
age = 15

if is_member and age > 18:
    print("You are a member and older than 18")
elif is_member and age < 18:
    print("You are a member but younger than 18")
elif not is_member and age > 18:
    print("You are not a member but older than 18")
else:
    print("You are not a member and younger than 18")