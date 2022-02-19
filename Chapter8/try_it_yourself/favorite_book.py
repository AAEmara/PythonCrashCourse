# Defining the function.
def favorite_book(title):
    """This function prints your favorite book title within a message.
    (input)::
    title: This is the parameter where you enter your book title.

    (output)::
    a print statement that includes "One of my favorite books is ..."
    before your input argument.
    """
    print(f"One of my favorite books is {title.title()}.")

favorite_book("Python Crash Course")