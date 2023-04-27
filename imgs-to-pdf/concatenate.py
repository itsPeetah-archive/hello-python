from PIL import Image
from os import path, mkdir

IMAGE_PATHS = ["input/IMG_1804.JPG",
               "input/IMG_1808.JPG", "input/IMG_1809.JPG", "input/IMG_1810.JPG", "input/IMG_1811.JPG"]
OUTPUT_FILENAME = "output.pdf"

if __name__ == "__main__":

    # Skip if empty
    if len(IMAGE_PATHS) < 1:
        print("Input filename list is empty.\nExiting...")
        exit(1)

    print("Loading images...")
    images = [Image.open(path) for path in IMAGE_PATHS]

    # make sure name is not empty
    pdf_path = OUTPUT_FILENAME + ("output" if len(OUTPUT_FILENAME) < 1 else "")
    pdf_path = pdf_path.split("/")[-1]  # only take filename from path
    if pdf_path[-4:].lower() != ".pdf":
        pdf_path += ".pdf"  # add extension if missing

    # create output directory
    if not path.isdir("./out"):
        mkdir("./out")
        print("Created output directory (./out).")

    pdf_path = "./out/" + pdf_path
    open(pdf_path, "w").close()

    print("Saving pdf with concatenated images...")
    baseImage, *otherImages = images  # extract base image and images to append
    baseImage.save(pdf_path, "PDF", resolution=100.0,
                   save_all=True, append_images=otherImages)

    print("Done.")
