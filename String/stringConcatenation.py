    # String Concatenation
    # To concatenate, or combine, two strings you can use the + operator.

    a = "Hello"
    b = "World"
    c = a + b
    print(c)

    # String Format
    # age = 36
    # txt = "My name is John, I am " + age
    # print(txt)

    # F-Strings

    '''
    F-Strings
    F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

    To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
    '''

    age = 36
    txt = f"My name is John, I am {age}"
    print(txt)


    name = "muhammad ali"
    result = f"My Name is {name}"
    print(result)


    # Escape Character
    # To insert characters that are illegal in a string, use an escape character.
    # An escape character is a backslash \ followed by the character you want to insert.

    txt = "We are the so-called \"Vikings\" from the north."


