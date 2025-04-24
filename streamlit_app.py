import streamlit as st

col1, col2 = st.columns([1, 5])
# with col1:
#     st.image("Yeni klasör/logo.jpg", width=100)

with col2:
    st.title("Project OPT-0158")

title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">Truck Based Laboratory Container (BSL3)</p>'
st.markdown(title, unsafe_allow_html=True)



st.title("BSL 3 Cabinet")
with open("Gine Lab/1. BSL III cabinet .pdf", "rb") as f:
    pdf_bytes1 = f.read()

if st.button("📄 Datasheet"):
    st.download_button(
        label="Download",
        data=pdf_bytes1,
        file_name="BSLIIICabinet.pdf",
        mime="application/pdf"
    )

st.title("Laboratory Refriagerator & Freezer")
with open("Gine Lab/2. Laboratory refrigerator and freezer .pdf", "rb") as f:
    pdf_bytes2 = f.read()

if st.button("📄 Datasheet"):
    st.download_button(
        label="Download",
        data=pdf_bytes2,
        file_name="LaboratoryRefrigeratorFreezer.pdf",
        mime="application/pdf"
    )


