# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



print('David Morar')


t1="Liga Națiunilor. Cipru-Romania 0-3: Tricolorii au trei victorii "
t2="din trei meciuri cu Lucescu antrenor și conduc grupa"

def articol(text1):
    print(text1.upper())
    print(text1.strip())
    print(text1.swapcase())
    print(text1.title())
    print(t1+t2)

articol(t1)
articol(t2)