
#todo: if sharing code, then tell ppl to install Pillow from git
from PIL import Image

# set of ASCII charatcers
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    # Calculate new height to maintain the aspect ratio
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def convert_to_grayscale(image):
    # Convert the image to grayscale
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    # Convert pix to ASCII on what pix
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    try:
        # Open img file
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Resize image/ maintaining  aspct ratio
    resized_image = resize_image(image, new_width)

    #  resized image to graysacle
    grayscale_image = convert_to_grayscale(resized_image)

    # Convert grayscale img pix to ASCII
    ascii_pixels = pixels_to_ascii(grayscale_image)

    len_pixels = len(ascii_pixels)

    # string  of ASCII img
    ascii_image = ""
    for i in range(0, len_pixels, new_width):
        ascii_image += ascii_pixels[i:i + new_width] + "\n"

    print(ascii_image)

# Replace 'image_path' with path of img file
image_to_ascii('C:\\Users\\K\\Downloads\\test.jpg', new_width=100)

#todo: try to add links for path img
