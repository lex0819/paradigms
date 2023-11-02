def mult_table(n):
    if n < 1 or n > 9:
        return "Please enter digit form 1 to 9"
    else:
        result = []
        for i in range(1, n+1):
            for j in range(1, 10):
                result.append(f"{i} * {j} = {i * j}")
            result.append("--------------------------")
        return result



print(*mult_table(11), sep='\n')
