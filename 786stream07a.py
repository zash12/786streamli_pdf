import streamlit as st
from PyPDF2 import PdfReader, PdfWriter

st.title("PDF Splitter Tool")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file:
    start_page = st.number_input("Start Page", min_value=1, step=1)
    end_page = st.number_input("End Page (Leave blank for all pages)", min_value=1, step=1)

    if st.button("Split PDF"):
        reader = PdfReader(uploaded_file)
        writer = PdfWriter()

        end_page = end_page or len(reader.pages)
        for i in range(start_page - 1, end_page):
            writer.add_page(reader.pages[i])

        output_filename = "split_output.pdf"
        with open(output_filename, "wb") as f:
            writer.write(f)

        with open(output_filename, "rb") as f:
            st.download_button("Download Split PDF", data=f, file_name=output_filename)
