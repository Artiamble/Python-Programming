#Creating a Valid Identifier
StudentId=101
print(StudentId)

Output:
101

#Creating an Invalid Identifier
$tudentId=101
print($tudentId)

Output:
 Cell In[5], line 2
    $tudentId=101
    ^
SyntaxError: invalid syntax


"""We can write an identifier with number but identifier should not start 
with digit."""

#Creating Valid Identifier
StudentId1=101
print(StudentId1)

Output:
101

#Creating Invalid Identifier
1StudentId=101
print(1StudentId)

Output:
Cell In[7], line 2
    1StudentId=101
    ^
SyntaxError: invalid decimal literal


#Identifier are case sensitive

#Creating Valid Identifier
Value=100
print(Value)

Output:
101

#Creating Invalid Identifier
Value=100
print(VALUE)

Output:
NameError                                 Traceback (most recent call last)
Cell In[10], line 3
      1 #Creating Invalid Identifier
      2 Value=100
----> 3 print(VALUE)

NameError: name 'VALUE' is not defined


# We cannot use keywords as identifiers.
if=100
print(if)

Output:
Cell In[11], line 2
    if=100
      ^
SyntaxError: invalid syntax


# Spaces are not allowed in between the identifier.
Student Id=101
print(Student Id)

Output:
Cell In[12], line 2
    Student Id=101
            ^
SyntaxError: invalid syntax