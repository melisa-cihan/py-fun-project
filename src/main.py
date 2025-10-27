from .calculator.Calculator import Calculator

def main():
    # instantiate calculators
    c1 = Calculator()
    c2 = Calculator()
    # 
    # print("same Calculator instance" if (id(c1) == id(c2)) else "different Calculator instances")
    if (id(c1) == id(c2)):
        print("same Calculator instance")
    else:
        print("different Calculator instances")
    # 
    print(f' 1: c1.add(1, 2)\t-> {c1.add(1, 2)}')
    print(f' 2: c2.add(8, 3)\t-> {c2.add(8, 3)}')
    print(f' 3: c1.add("1", "1")\t-> {c1.add("1", "1")}')     # <-- uncomment
    print(f' 4: c1.add("X", "V")\t-> {c1.add("X", "V")}')
    print(f' 5: c2.factorize(99)\t-> {c1.factorize(99)}')
    _offset=6
    # 
    print(f' 6: c1.add("1", "1.600")\t-> {c1.add("1", "1.600")}')
    print(f' 7: c1.add("three", "1.600")\t-> {c1.add("three", "1.600")}')
    print(f' 8: c1.add("cinco", "siete")\t-> {c1.add("cinco", "siete")}')
    print(f' 9: c1.add("семь", "восемь")\t-> {c1.add("семь", "восемь")}')
    print(f'10: c1.add("III", "   VIII")\t-> {c1.add("III", "   VIII")}')
    print(f'11: c1.add("三", "五")\t\t-> {c1.add("三", "五")}')

    # set True to run the examples from the expression list
    _run_list=False
    expr=[
        'c1.add("1", "1.600")',         # 2.6
        'c1.add("three", "1.600")',     # 4.6
        'c1.add("cinco", "siete")',     # 12
        'c1.add("семь", "восемь")',     # 15
        'c1.add("III", "   VIII")',     # 11
        'c1.add("三", "五")',            # 8
        'c1.add("0", "X")',             # 10
        'c2.add("ocho", "nueve")',      # 17
        'c2.sub("ocho", "nueve")',      # -1
        'c2.mul("ocho", "nueve")',      # 72
        'c2.div("ocho", "dos")',        # 4.0
        '',
        'c2.factorize("три")',          # [3]
        'c2.factorize("X")',            # [2, 5]
        'c2.factorize("ocho")',         # [2, 2, 2]
        'c2.factorize(3+5)',            # [2, 2, 2]
        'c2.factorize(27)',             # [3, 3, 3]
        'c2.factorize(1092)',           # [2, 2, 3, 7, 13]
        'c2.factorize(32768)',          # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        'c2.factorize(10952347)',       # [7, 23, 59, 1153]
        'c2.factorize(100000039)',      # [100000039] (prime number)
        '',
    ] if _run_list else []
    # 
    for i in range(len(expr)):
        e = expr[i].strip()
        if len(e) > 0:
            spacer="\t\t" if len(e) < 20 else "\t"
            print(f'{i+_offset:2d}: {e}{spacer}-> {eval(e)}')
