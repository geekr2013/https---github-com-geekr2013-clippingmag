import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# 이미지 업로드
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # API 호출
    response = requests.post(
        'https://ko.clippingmagic.com/api/v1/images',
        files={'image': uploaded_file.getvalue()},
        data={
            'format': 'json',
            'test': 'true'
        },
        auth=('18918', 'cq0gll75k8g7urv8qbepi6dd3arhpg2gef010kn1l31bsh70loi5')
    )
    if response.status_code == requests.codes.ok:
        r = json.loads(response.content)
        imageId = r["image"]["id"]
        imageSecret = r["image"]["secret"]

        # 이미지 처리 및 표시
        # TODO: 여기에 이미지 처리 코드를 추가하세요.
        # 예를 들어, 배경을 제거하거나, 이미지를 리사이징하거나, 각도를 조절하거나, 해상도를 변경하는 등의 작업을 수행할 수 있습니다.
        processed_image = image  # 이 예시에서는 처리된 이미지를 원본 이미지로 가정합니다.
        st.image(processed_image, caption='Processed Image.', use_column_width=True)
    else:
        st.write("Error:", response.status_code, response.text)
