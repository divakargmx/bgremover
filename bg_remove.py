import streamlit as st
import cv2
from rembg import remove

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Remove background from your image")
st.write(
    ":dog: Try uploading an image to watch the background magically removed. Full quality images can be downloaded from the sidebar. This code is open source and available [here](<https://github.com/tyler-simons/BackgroundRemoval>) on GitHub. Special thanks to the [rembg library](<https://github.com/danielgatis/rembg>) :grin:"
)
st.sidebar.write("## Upload and download :gear:")

# Create the columns
col1, col2 = st.columns(2)


 Package the transform into a function
def fix_image(upload):
    image1 = Image.open(upload)
    image= cv2.imread(image1)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\\n")
    st.sidebar.download_button(
        "Download fixed image", convert_image(fixed), "fixed.png", "image/png"
    )

# Create the file uploader
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Fix the image!
if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./wallaby.png")
