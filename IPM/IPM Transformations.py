import numpy as np

def inverse_perspective_mapping(u, v, H):
    """
    u, v: These are the pixel coordinates from our image
    H: Our 3x3 homography matrix 
    """
    # 1st operation: LIFT 
    # Lifiting the 2D coordinates into a 3D coordinate space to create a homogenous vector

    pixel_vector = np.array([
                                    [u],
                                    [v],
                                    [1]
                                    ])
    
    # 2nd operation: TRANSFORM
    # Matrix multiplication (The change of 'Basis')
    # H rotates and tilts the vector.
    ground_vector = H @ pixel_vector

    print(f"The matrix multiplication of H: \n{H}\n and our Pixel vector: \n{pixel_vector}\n is:\n {ground_vector}")

    # This is what the raw output will look like of our matrix
    x_prime = ground_vector[0, 0]
    y_prime = ground_vector[1, 0]
    w_prime = ground_vector[2, 0]

    print("x_prime: ", x_prime)
    print("y_prime: ", y_prime)
    print("w_prime: ", w_prime)

    # 3rd operation: PROJECT
    # This is our normalization step. We divide by the third component to flatten the vector back to our 2D space

    x_ground = x_prime / w_prime
    y_ground = y_prime / w_prime

    return x_ground, y_ground

# Lets try our function out with an example
# We are supposed to perform Camera Calibration to get this homography matrix. Lets choose a dummy matrix for now

H_dummy = np.array([
    [0.5  , -0.2 ,  100],
    [0.1  ,  0.8 ,  50 ],
    [0.001,  0.002, 1  ]
])

# Now we can try mapping our pixels to the ground
u, v = 480, 360
x, y = inverse_perspective_mapping(u, v, H_dummy)

print(print(f"Pixel ({u}, {v}) maps to Ground Coordinates: x={x:.2f}, y={y:.2f}"))
# Do not worry about 1.e-01, 5.e+01, etc. Numpy uses scientific notation
# The format is: a.e^b = a x 10^b, therefore 1.e-01 is just 0.1. Similarly, 5.e+01 is 50

