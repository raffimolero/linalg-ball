from image_mat_util import file2mat, mat2display
from transform import *

TEST_FILE = "graphic-design.png"
TEST_MAT, TEST_COLS = file2mat(TEST_FILE)
TEST_W, TEST_H = 263, 149
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


def task_4_15_9():
    """
    Write a procedure scale_color() that takes r, g, and b scaling parameters and returns the corresponding scaling matrix.
    """
    M = scale_color(1, 0.5, 2)
    mat2display(BASE_TRANSLATION * TEST_MAT, M * TEST_COLS)


def task_4_15_10():
    """
    Write a procedure grayscale() that returns a matrix that converts a color image to a grayscale image.
    Note that both images are still represented in RGB.
    If a pixel in the original image had the values r,g,b in each of the color channels, then in the grayscale image it has the value 77r/256 + 151g/256 + 28b/256 in all three color channels.
    """
    M = grayscale()
    mat2display(BASE_TRANSLATION * TEST_MAT, M * TEST_COLS)


def task_4_15_11():
    """
    Write a procedure reflect_about(x1,y1,x2,y2) that takes two points and returns the matrix that reflects about the line defined by the two points.
    (Hint: Use rotations, translations, and a simple reflection).
    """
    M = reflect_about(1, 1, 5, 7)
    mat2display(BASE_TRANSLATION * M * TEST_MAT, TEST_COLS)


def main():
    tasks = {
        "show": task_4_15_1,
        "identity": task_4_15_2,
        "translate": task_4_15_3,
        "scale": task_4_15_4,
        "rotate": task_4_15_5,
        "rotate about": task_4_15_6,
        "reflect y": task_4_15_7,
        "reflect x": task_4_15_8,
        "scale color": task_4_15_9,
        "grayscale": task_4_15_10,
        "reflect about": task_4_15_11,
    }
    prompt = f'Enter task (or exit):\n{'\n'.join(f'> {task}' for task in tasks.keys())}\n> '
    while (line := input(prompt).strip()) != "exit":
        try:
            t = tasks[line]
            t()
        except IndexError:
            pass
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
