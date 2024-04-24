import imgcompare

# Function to calculate average percentage comparison
def average_comparison(folder1, folder2, prefix1, prefix2, num_images):
    total_percentage = 0
    for i in range(1, num_images+1):
        img1_path = f"{folder1}/{prefix1}{i}.png"
        img2_path = f"{folder2}/{prefix2}{i}.png"
        percentage = imgcompare.image_diff_percent(img1_path, img2_path)
        total_percentage += percentage
    average_percentage = total_percentage / num_images
    return average_percentage

rr_average_percentage = average_comparison("resultoutser", "big", "rr", "b", 15)
print("Average similarity percentage for 15 encoded images using image steganography:", 100-rr_average_percentage)

ts_average_percentage = average_comparison("textserout", "small", "ts", "s", 15)
print("Average similarity percentage 15 encoded images using text steganography:", 100-ts_average_percentage)
