# pytest 6.x.x

# def dodawanie():
#     a = 5
#     b = 10
#     c = a + b
#     return c
#
# print(dodawanie())


class TestMultiple:


    def test_dodawanie(self):
        a = 5
        b = 10
        assert a + b == 11

    def test_odejmowanie(self):
        a = 10
        b = 12
        assert a - b == 9
        print("test nr 2 wykoanany poprawie")


#---------------------------------------



testy = TestMultiple()



print("Proszę wybrać pozycje do testów:")
print("---------------------------------")
print("1. dodawanie")
print("2. odejmowanie")
print("---------------------------------")
wybor = input("Wprowadź cyfrę(1-2): ")

if wybor == "1":
    testy.test_dodawanie()
elif wybor == "2":
    testy.test_odejmowanie()
else:
    print("Zła opcja!")


