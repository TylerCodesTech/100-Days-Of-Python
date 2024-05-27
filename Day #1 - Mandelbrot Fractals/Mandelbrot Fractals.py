import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mandelbrot(c, max_iter):
    """
    Calculates the number of iterations it takes for a point c in the complex plane to escape the Mandelbrot set.

    Parameters:
        c (complex): The complex coordinate.
        max_iter (int): The maximum number of iterations to perform.

    Returns:
        int: The number of iterations it took for the point to escape.
    """
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_fractal(min_x, max_x, min_y, max_y, width, height, max_iter):
    """
    Generates a fractal grid representing the Mandelbrot set.

    Parameters:
        min_x (float): The minimum x-coordinate.
        max_x (float): The maximum x-coordinate.
        min_y (float): The minimum y-coordinate.
        max_y (float): The maximum y-coordinate.
        width (int): The number of columns in the grid.
        height (int): The number of rows in the grid.
        max_iter (int): The maximum number of iterations to perform.

    Returns:
        numpy.ndarray: A 2D array representing the fractal grid.
    """
    r1d = np.linspace(min_x, max_x, width)
    r2d = np.linspace(min_y, max_y, height)
    grid = np.zeros((width, height), dtype=int)

    for i in range(width):
        for j in range(height):
            c = complex(r1d[i], r2d[j])
            m = mandelbrot(c, max_iter)
            grid[i][j] = m

    return grid

def plot_fractal(grid, min_x, max_x, min_y, max_y):
    """
    Plots the fractal grid as a 3D surface.

    Parameters:
        grid (numpy.ndarray): The fractal grid.
        min_x (float): The minimum x-coordinate.
        max_x (float): The maximum x-coordinate.
        min_y (float): The minimum y-coordinate.
        max_y (float): The maximum y-coordinate.

    Returns:
        None
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_range = np.linspace(min_x, max_x, 800)
    y_range = np.linspace(min_y, max_y, 800)

    X, Y = np.meshgrid(x_range, y_range)
    Z = grid.reshape((800, 800))

    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

    plt.show()

def main():
    """
    Main function to generate and plot a fractal.
    """
    min_x, max_x, min_y, max_y = -2.5, 1.0, -2.0, 2.0
    width, height, max_iter = 800, 800, 256

    grid = generate_fractal(min_x, max_x, min_y, max_y, width, height, max_iter)

    plot_fractal(grid, min_x, max_x, min_y, max_y)

if __name__ == "__main__":
    main()
