from image_mat_util import file2mat, mat2display
from transform import *

TEST_FILE = "img01.png"
TEST_MAT, TEST_COLS = file2mat(TEST_FILE)
TEST_W, TEST_H = 166, 189
BASE_TRANSLATION = translation(500, 500)

def task_4_15_1():
    """
    Task 4.15.1: Download a .png image file, then use file2mat to load it and mat2display to display it on the screen.
    """
    mat2display(BASE_TRANSLATION * TEST_MAT, TEST_COLS)


def task_4_15_2():
    """
    Task 4.15.2: Write a procedure identity() which takes no arguments and returns an identity matrix for location vectors.
    Verify that this matrix works by applying it first to some points and then to an image, making sure that nothing changes.
    (Hint: Think about the correct row and column labels.)
    """
    M = identity()
    mat2display(BASE_TRANSLATION * M * TEST_MAT, TEST_COLS)


def task_4_15_3():
    """
    Task 4.15.3: Write a procedure translation(alpha, beta) that takes two translation parameters and returns the corresponding 3 x 3 translation matrix.
    Test it on some images.
    """
    M = translation(200, 100)
    mat2display(BASE_TRANSLATION * M * TEST_MAT, TEST_COLS)


def task_4_15_4():
    """
    Task 4.15.4: Write a procedure scale(alpha, beta) that takes x- and y-scaling parameters and returns the corresponding 3 x 3 scaling matrix that multiplies a vector [x y 1].
    """
    M = scale(2, 3)
    mat2display(BASE_TRANSLATION * M * TEST_MAT, TEST_COLS)


def task_4_15_5():
    """
    Task 4.15.5: Write a procedure rotation(theta) that takes an angle in radians and returns the corresponding rotation matrix.
    Hint: Both sin(.) and cos(.) are available in the math module.
    """
    M = rotation(tau / 3)
    mat2display(BASE_TRANSLATION * M * TEST_MAT, TEST_COLS)


def task_4_15_6():
    """
    Task 4.15.6: Write a procedure rotation_about(theta, x, y) that takes three parameters---an angle theta in radians, an x coordinate and a y coordinate---and returns the matrix that rotates counterclockwise about (x,y) by theta.
    Hint: Use procedures you've already written.
    """
    M = rotation_about(tau / 3, TEST_W / 2, TEST_H / 2)
    mat2display(BASE_TRANSLATION * M * TEST_MAT, TEST_COLS)


def task_4_15_7():
    """
    Write a procedure reflect_y() that takes no parameters and returns the matrix which corresponds to a reflection about the y axis.
    """
    M = reflect_y()
    mat2display(BASE_TRANSLATION * M * TEST_MAT, TEST_COLS)


def task_4_15_8():
    """
    Write a procedure reflect_x() that takes no parameters and returns the matrix which corresponds to a reflection about the x axis.
    """
    M = reflect_x()
    mat2display(BASE_TRANSLATION * M * TEST_MAT, TEST_COLS)


def main():
    tasks = {
        1: task_4_15_1,
        2: task_4_15_2,
        3: task_4_15_3,
        4: task_4_15_4,
        5: task_4_15_5,
        6: task_4_15_6,
        7: task_4_15_7,
        8: task_4_15_8,
    }
    while (line := input(f'Enter task [1-{len(tasks)}] or q to exit: ').strip()) != 'q':
        try:
            i = int(line)
            t = tasks[i]
            t()
        except:
            print(f'Must be a number from 1 to {len(tasks)}.')



if __name__ == "__main__":
    main()
