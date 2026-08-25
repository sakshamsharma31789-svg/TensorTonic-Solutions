def color_to_grayscale(image: list) -> list:
    """
    Returns the luminance value of every RGB pixel.
    """
    grayscale_image = []
    for row in image:
        gray_row = []
        for r,g,b in row:
            y = 0.299*r+0.587*g+0.114*b
            gray_row.append(y)
        grayscale_image.append(gray_row)
    return grayscale_image
    pass