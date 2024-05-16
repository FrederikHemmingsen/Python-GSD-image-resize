from PIL import Image

def resize_image(image_path, output_path, percentage):
    with Image.open(image_path) as img:
        # Calculate the new dimensions
        new_width = int(img.width * (percentage / 100))
        new_height = int(img.height * (percentage / 100))

        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

        # Save the resized image
        resized_img.save(output_path)
        return new_width, new_height

def calculate_new_gsd(start_gsd, percentage):
    return start_gsd * (percentage / 100)

if __name__ == "__main__":
    image_path = "input.jpg"        # imagepath
    output_base_path = "output"     # outputbase
    start_gsd = 1                 # Starting GSD

    for percentage in range(100, 50, -10):  # Resize from 100% to X% increments of of -X%
        new_gsd = calculate_new_gsd(start_gsd, percentage)
        output_path = f"{output_base_path}_{new_gsd:.2f}.jpg"
        new_width, new_height = resize_image(image_path, output_path, percentage)
        print(f"Image saved to {output_path} with new GSD: {new_gsd:.2f} and size {new_width}x{new_height}")
