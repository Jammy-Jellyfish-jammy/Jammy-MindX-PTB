def times(a, b):
    return a*b

def input_output():
    a, b= map(int, input().split())
    return times(a, b)

print("Do dai can nha (a b)")
nha = input_output()
print("Do dai vien gach (a b)")
gach = input_output()
print(f"So vien gach can la {nha/gach}")
    