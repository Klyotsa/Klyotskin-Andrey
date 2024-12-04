def read_matrix_from_file(input_file):
    with open(input_file, 'r') as file:
        matrix = []
        for line in file:
            row = list(map(float, line.strip().split()))
            matrix.append(row)
    return matrix
def process_matrix(matrix):
    new_matrix = []
    for row in matrix:
        min_element = min(row)
        if int(min_element) % 2 == 0:
            replacement = 0
        else:
            replacement = 1
        transformed_row = [
            replacement if x == min_element else x for x in row
        ]
        new_matrix.append(transformed_row)
    return new_matrix
def write_matrix_to_file(output_file, matrix):
    with open(output_file, 'w') as file:
        for row in matrix:
            file.write(" ".join(map(str, row)) + "\n")
input_filename = 'Klyotskin_y-244_vvod.txt'
output_filename = 'Klyotskin_y-244_vbIvod.txt'
matrix = read_matrix_from_file(input_filename)
processed_matrix = process_matrix(matrix)
write_matrix_to_file(output_filename, processed_matrix)
print(f"Результаты записаны в файл: {output_filename}")


