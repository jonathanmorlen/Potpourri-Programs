from fractions import Fraction


# dot product of two vectors
# if one vector is longer than the other, it is truncated to be the same size
def dot(a, b):
    product = []
    for i in zip(a, b):
        product.append(i[0] * i[1])
    return sum(product)


# orthogonal projection of a vector on a subspace
if __name__ == '__main__':
    # take input of any length vector
    # input space separated numbers of the form "a b c ... x y z"
    vector = input("Input vector: ")
    vector = [float(i) for i in vector.split(' ')]
    length = len(vector)

    # take the columns of the subspace one at a time
    # each column is of the form "a b c ... x y z"
    # signal the end of the subspace with the character 'd'
    answer = ""
    subspace = []
    while answer != 'd':
        answer = input("Input subspace, enter \'d\' when done: ")
        if answer == 'd':
            break
        element = [float(i) for i in answer.split(' ')]
        subspace.append(element)

    # find the orthogonal projection of the vector on all columns of the subspace
    y = []
    for column in subspace:
        scalar = dot(vector, column) / dot(column, column)
        x = [scalar * i for i in column]
        y.append(x)

    # add all orthogonal projections of the columns together
    final = [sum(row[i] for row in y) for i in range(len(y[0]))]

    # turn the decimals into fractions
    formatted = [str(Fraction(i).limit_denominator()) for i in final]
    print(formatted)
