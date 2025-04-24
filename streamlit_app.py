import streamlit as st

col1, col2 = st.columns([1, 5])
# with col1:
#     st.image("Yeni klasör/logo.jpg", width=100)

with col2:
    st.title("Project OPT-0158")

title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">Truck Based Laboratory Container (BSL3)</p>'
st.markdown(title, unsafe_allow_html=True)


st.title("BSL 3 Cabinet")
with open("1. BSL III cabinet .pdf", "rb") as f:
    pdf_bytes = f.read()

if st.button("📄 Datasheet"):
    st.download_button(
        label="Download",
        data=pdf_bytes,
        file_name="kullanim_kilavuzu.pdf",
        mime="application/pdf"
    )
