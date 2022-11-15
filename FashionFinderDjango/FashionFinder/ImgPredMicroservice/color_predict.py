import cv2
import numpy as np
import scipy
from sklearn.cluster import KMeans


def gaussian_kernel(img_height, img_width, kernel_relative_size=0.1, verbose=False):
    xs = scipy.signal.gaussian(img_width, std=img_width * kernel_relative_size)
    ys = scipy.signal.gaussian(img_height, std=img_height * kernel_relative_size)
    kernel = np.array([[x * y for x in xs] for y in ys])
    return kernel


def get_flatted_normalized_gaussian_kernel(kernel):
    kernel = kernel.reshape(-1)
    kernel = kernel / np.sum(kernel)
    return kernel


def get_draw(img_colors, normed_kernel=None, sample_size=1000):
    if normed_kernel is not None:
        draw_idx = np.random.choice(a=224 ** 2, size=sample_size, replace=True, p=normed_kernel)
    else:
        draw_idx = np.random.choice(a=224 ** 2, size=sample_size, replace=True)
    # Get rows specified by draw idx for img_colors
    return img_colors[draw_idx]


def readImg(filepath, resize_shape=(224, 224)):
    img = cv2.imread(filepath)
    if img is not None:
        r_img = cv2.resize(img, resize_shape)
        return r_img
    else:
        return img


def rgb_to_hex(r, g, b):
    return ('{:02X}' * 3).format(r, g, b)


def get_knn_for_colors_list(colors):
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(colors)
    return kmeans.cluster_centers_


def get_dominant_colors(img, normed_kernel=None):
    # img = readImg(filepath=filepath, resize_shape=(224,224))
    # if img is None:
    # return list()
    if normed_kernel is None:
        kernel = gaussian_kernel(224, 224, kernel_relative_size=0.1, verbose=False)
        normed_kernel = get_flatted_normalized_gaussian_kernel(kernel)
    # Resize the image input to be a list of lenght width*height
    img_colors = np.array(img.reshape((-1, 3)), dtype=float)

    draw = get_draw(img_colors=img_colors, normed_kernel=normed_kernel, sample_size=200)
    # return draw
    print(np.shape(draw))
    print(draw[0:5])
    knn_colors = get_knn_for_colors_list(draw)
    # knn_colors = []
    hex_vals = list()
    for color in knn_colors:
        # These colors are encoded with BGR
        red = int(color[0])
        green = int(color[1])
        blue = int(color[2])
        hex_val = rgb_to_hex(red, green, blue)
        hex_vals.append(hex_val)
    return hex_vals
