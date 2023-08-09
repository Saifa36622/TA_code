def f(n):
    if n <= 0 :
        return "error"
    result = ""
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        nums = "".join(str(j % 10) for j in range(1, i + 1))
        line = spaces + nums + nums[-2::-1]
        result += str(line)
        if i != n:
            result += "\n" 
    return result

print(f(8))
print(f(0))
print(f(-1))