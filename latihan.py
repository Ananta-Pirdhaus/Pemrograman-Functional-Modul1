# fungsi pengurangan
def minus (x, y) :
    return x - y
# fungsi penambahan
def plus (x, y) :
    return x - y
# fungsi perkalian
def mult (x, y) :
    return x * y
# fungsi pembagian
def div (x, y) :
    return x / y

# Definisikan pohon ekspresi sebagai fungsi
def tree(node):
    if type(node) in (int, float):
        return node
    elif type (node) is tuple and len(node) == 3:
        print(node)
        left_operand, operator, right_operand = node
        if operator == '+':
            return plus(tree(left_operand), tree(right_operand))
        elif operator == '-':   
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*' :
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/' :
            return div(tree(left_operand), tree(right_operand))
        

# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

print('Hasil evaluasi pohon ekspresi: ', result)