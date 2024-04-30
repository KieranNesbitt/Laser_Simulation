import numpy as np
class Circle:
    def __init__(self, a:int, b:int, r:int):
        """
        Draw a filled circle onto a 2D array.

        Parameters:
            map_ (numpy.ndarray): The 2D array representing the map.
            a (int): x-coordinate of the center of the circle.
            b (int): y-coordinate of the center of the circle.
            r (int): Radius of the circle.

        Explanation:
            - Get the height and width of the map.
            - Create coordinate grids for x and y.
            - Calculate the squared distance from each point on the map to the center of the circle using the equation of a circle: (x-a)^2 + (y-b)^2.
            - Create a mask where True values indicate that the corresponding point is within the circle (i.e., the distance is less than or equal to r^2).
            - Update the map where the mask is True to fill all cells within the circle.
        Equation:
            \(Distnace = (x - a)^2 + (y - b)^2)\)
        Returns:
            None (The map is modified in place).
        """
        self.a, self.b,self.r =a,b,r
    def create(self, map_: np.ndarray, value: float):
        # Get the height and width of the map
        height, width = map_.shape

        # Create coordinate grids for x and y
        x_coords = np.arange(width)
        y_coords = np.arange(height)
        x_grid, y_grid = np.meshgrid(x_coords, y_coords)

        # Calculate the squared distance from each point to the center of the circle
        distances = (x_grid - self.a)**2 + (y_grid - self.b)**2

        # Check if the distance is less than or equal to r^2
        mask = distances < self.r**2

        # Update the map where the mask is True
        map_[mask] = value

class Square:
    def __init__(self, center: tuple, side_length):
        self.center,self.side_length= center, side_length

    def create(self, map_, value):
        # Calculate the coordinates of the square's corners
        top_left = (self.center[0] - self.side_length // 2, self.center[1] - self.side_length // 2)
        bottom_right = (self.center[0] + self.side_length // 2, self.center[1] + self.side_length // 2)
        # Set the values in the map within the square's boundaries to 1
        map_[top_left[0]:bottom_right[0]+1, top_left[1]:bottom_right[1]+1] = value
class Ellipsoid:
    def __init__(self, a: int, b: int, r_x: int, r_y: int):
        """
        Draw a filled ellipsoid onto a 2D array.

        Parameters:
            map_ (numpy.ndarray): The 2D array representing the map.
            a (int): x-coordinate of the center of the ellipsoid.
            b (int): y-coordinate of the center of the ellipsoid.
            r_x (int): Radius of the ellipsoid along the x-axis.
            r_y (int): Radius of the ellipsoid along the y-axis.

        Explanation:
            - Get the height and width of the map.
            - Create coordinate grids for x and y.
            - Calculate the distance from each point on the map to the center of the ellipsoid using the equation of an ellipsoid.
            - Create a mask where True values indicate that the corresponding point is within the ellipsoid.
            - Update the map where the mask is True to fill all cells within the ellipsoid.

        Returns:
            None (The map is modified in place).
        """
        self.a, self.b, self.r_x, self.r_y = a, b, r_x, r_y

    def create(self, map_: np.ndarray, value: float):
        # Get the height and width of the map
        height, width = map_.shape

        # Create coordinate grids for x and y
        x_coords = np.arange(width)
        y_coords = np.arange(height)
        x_grid, y_grid = np.meshgrid(x_coords, y_coords)

        # Calculate the distance from each point to the center of the ellipsoid
        distances = ((x_grid - self.a) / self.r_x)**2 + ((y_grid - self.b) / self.r_y)**2

        # Check if the distance is less than or equal to 1 (for points inside the ellipsoid)
        mask = distances < 1

        # Update the map where the mask is True
        map_[mask] = value
class Custom:
    def __init__(self):
        pass
    def create(self, map_, value):
        pass