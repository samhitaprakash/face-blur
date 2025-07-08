import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="FaceGuard – Live Face Blur", layout="centered")

st.markdown("""
# 🛡️ FaceGuard
**Live AI Face Blur & Pixelate App**

Protect your identity. Toggle blur or pixelate mode in real time.  
Built with OpenCV + Streamlit.
""")

# Sidebar controls
pixelate_mode = st.sidebar.toggle("Use Pixelation?", value=False)
st.write("Toggle State:", pixelate_mode)
st.sidebar.markdown(f"**Current Mode:** {'🟦 Pixelate' if pixelate_mode else '🌀 Blur'}")

# Load face cascade
face_cascade = cv2.CascadeClassifier('models\haarcascade_frontalface_default.xml')
if face_cascade.empty():
    st.error("❌ Failed to load face detection model.")


# Streamlit Webcam Processor
class FaceProcessor(VideoTransformerBase):
    def __init__(self, pixelate):
        self.pixelate = pixelate
        self.result_frame = None

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        if len(faces) == 0:
            cv2.putText(img, "❌ No Face Detected", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        for (x, y, w, h) in faces:
            face_roi = img[y:y+h, x:x+w]
            if self.pixelate:
                small = cv2.resize(face_roi, (10, 10), interpolation=cv2.INTER_LINEAR)
                face_roi = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
            else:
                face_roi = cv2.GaussianBlur(face_roi, (99, 99), 30)
            img[y:y+h, x:x+w] = face_roi

        self.result_frame = img
        return img

# Stream and capture logic
ctx = webrtc_streamer(
    key=f"faceguard-{pixelate_mode}",
    video_processor_factory=lambda: FaceProcessor(pixelate_mode),
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)


# Capture & download button logic
if ctx.video_processor and st.sidebar.button("📸 Capture Screenshot", key="capture_btn"):
    
    img_bgr = ctx.video_processor.result_frame
    if img_bgr is not None:
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)
        st.image(pil_img, caption="📸 Captured Screenshot", use_container_width=True)

        buffer = BytesIO()
        pil_img.save(buffer, format="JPEG")
        buffer.seek(0)

        st.download_button("Download Image", buffer.getvalue(), file_name="faceguard_capture.jpg", mime="image/jpeg")
    else:
        st.warning("⚠️ No frame captured yet.")
