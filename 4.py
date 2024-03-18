def pancake_sort(stack):
    # Начиная с нижней части стопки, несколько раз переверните самые большие блины к вершине
    for i in range(len(stack), 0, -1):
        max_index = i - 1  # Индекс самого большого блина в текущем подмассиве
        for j in range(i - 1, -1, -1):
            if stack[j] > stack[max_index]:
                max_index = j
        # Переверните самый большой блин на вершину stack
        if max_index != i - 1:
            stack[:i] = stack[:i][::-1]

    return stack

stack = [5, 3, 8, 4, 6]
sorted_stack = pancake_sort(stack)
print(sorted_stack)