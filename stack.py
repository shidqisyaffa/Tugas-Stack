def precedence(operator):
    """Mengembalikan prioritas operator."""
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return 0

def infix_to_postfix(infix_expr):
    """Konversi ekspresi infix ke postfix."""
    stack = []
    postfix = []
    steps = []

    for token in infix_expr:
        if token.isalnum():
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(token):
                postfix.append(stack.pop())
            stack.append(token)

        steps.append([token, ''.join(stack), ' '.join(postfix)])

    while stack:
        postfix.append(stack.pop())
        steps.append(['', ''.join(stack), ' '.join(postfix)])

    return postfix, steps

def print_table(steps):
    """Mencetak tabel langkah-langkah konversi infix ke postfix."""
    print("{:<15} {:<15} {:<15}".format("Token", "Stack", "Output"))
    print("=" * 45)

    for step in steps:
        print("{:<15} {:<15} {:<15}".format(step[0], step[1], step[2]))

if __name__ == "__main__":
    while True:
        infix_expr = input("Masukkan ekspresi infix (atau ketik 'exit' untuk keluar): ")

        if infix_expr.lower() == 'exit':
            break

        infix_expr = infix_expr.replace(" ", "")
        infix_expr = list(infix_expr)

        postfix_result, steps = infix_to_postfix(infix_expr)

        print("\nLangkah-langkah konversi ke postfix:")
        print("=" * 45)
        print_table(steps)

        print("\nHasil postfix: {}\n".format(' '.join(postfix_result)))