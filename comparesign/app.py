import streamlit as st
import cv2
import numpy as np
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
from skimage.metrics import structural_similarity as ssim
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Banking Signature Verification AI", layout="wide")

st.title("Banking Signature Verification AI")
st.markdown("Simulate automated banking clearance protocols using Deep Learning and Computer Vision.")

# 1. Load Pretrained Deep Learning Model
@st.cache_resource
def load_feature_extractor():
    weights = models.ResNet50_Weights.DEFAULT
    model = models.resnet50(weights=weights)
    model.fc = torch.nn.Identity()
    model.eval()
    return model, weights

try:
    model, weights = load_feature_extractor()
    preprocess_transform = weights.transforms()
except Exception as e:
    st.error(f"Error loading model: {e}")

# 2. Helper Image Processing Functions
def preprocess_for_ssim(image_pil, target_size=(300, 300)):
    img_np = np.array(image_pil)
    if len(img_np.shape) == 3:
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    else:
        gray = img_np
    resized = cv2.resize(gray, target_size)
    return resized

def extract_deep_features(image_pil, model, transform):
    img_rgb = image_pil.convert("RGB")
    tensor = transform(img_rgb).unsqueeze(0)
    with torch.no_grad():
        embedding = model(tensor).flatten().numpy()
    return embedding

# 3. Sidebar Frontend Controls
st.sidebar.header("Upload Signatures")
old_file = st.sidebar.file_uploader("Baseline Reference (old.jpeg)", type=["jpg", "jpeg", "png"])
new_file = st.sidebar.file_uploader("Verification Target (new.jpg)", type=["jpg", "jpeg", "png"])

st.sidebar.write("---")
st.sidebar.header("⚙️ Banking Risk Controls")

# Interactive Sliders mimicking Automated Signature Verification (ASV) tuning
auto_pass_threshold = st.sidebar.slider(
    "Auto-Approval Threshold (%)", 
    min_value=70, max_value=95, value=80, step=1,
    help="Signatures matching above this score are instantly cleared without human eyes."
)

manual_review_threshold = st.sidebar.slider(
    "Manual Review Floor (%)", 
    min_value=40, max_value=69, value=60, step=1,
    help="Scores between this floor and the auto-pass setting go to a human queue. Scores below are instantly rejected."
)

# 4. Main App Processing Pipeline
if old_file and new_file:
    img_old = Image.open(old_file)
    img_new = Image.open(new_file)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Reference Signature")
        st.image(img_old, use_container_width=True)
    with col2:
        st.subheader("Verification Target")
        st.image(img_new, use_container_width=True)
        
    st.write("---")
    st.subheader("Automated Clearance Verdict")
    
    with st.spinner("Processing dual-track analytics pipeline..."):
        gray_old = preprocess_for_ssim(img_old)
        gray_new = preprocess_for_ssim(img_new)
        
        # Track A: Structural Match
        ssim_score, diff_map = ssim(gray_old, gray_new, full=True)
        structural_match_pct = max(0.0, min(100.0, ssim_score * 100))
        
        # Track B: Deep Geometric Style Match
        feat_old = extract_deep_features(img_old, model, preprocess_transform)
        feat_new = extract_deep_features(img_new, model, preprocess_transform)
        cosine_sim = np.dot(feat_old, feat_new) / (np.linalg.norm(feat_old) * np.linalg.norm(feat_new))
        deep_match_pct = max(0.0, min(100.0, cosine_sim * 100))
        
        # Dynamic Weighted Blend (70% Deep Style / 30% Rigid Alignment)
        final_confidence = (deep_match_pct * 0.7) + (structural_match_pct * 0.3)

    # 5. Core Banking 3-Tier Threshold Logic Execution
    if final_confidence >= auto_pass_threshold:
        st.success(f"### **VERDICT: AUTO-APPROVED**")
        st.markdown(f"**Confidence Score:** `{final_confidence:.2f}%` (Exceeds custom {auto_pass_threshold}% threshold). This transaction bypasses the manual queue and is cleared instantly.")
    elif manual_review_threshold <= final_confidence < auto_pass_threshold:
        st.warning(f"### **VERDICT: ROUTED TO MANUAL REVIEW**")
        st.markdown(f"**Confidence Score:** `{final_confidence:.2f}%` (Falls within grey-zone variance). Transaction held. Route to bank officer for dual-card ocular validation.")
    else:
        st.error(f"### **VERDICT: TRANSACTION REJECTED**")
        st.markdown(f"**Confidence Score:** `{final_confidence:.2f}%` (Below security floor of {manual_review_threshold}%). High geometric deviance detected. Fraud protocols triggered.")

    # 100% Match Anomaly Alert (Tracer Detection)
    if final_confidence > 99.5:
        st.info("**ANTI-FRAUD ALERT:** The match score is near 100%. Natural physical signatures never match perfectly down to the pixel layer. Investigate for digital copy-paste or tracing fraud.")

    # Visual Analytics Expanders
    st.write("---")
    with st.expander("🔍 View Structural Deviations and Core Vectors"):
        m1, m2 = st.columns(2)
        m1.metric("Deep Feature Core Match", f"{deep_match_pct:.2f}%")
        m2.metric("Structural Alignment Match", f"{structural_match_pct:.2f}%")
        
        inverted_diff = 255 - (diff_map * 255).astype(np.uint8)
        fig = px.imshow(inverted_diff, color_continuous_scale='Jet')
        fig.update_layout(title="Signature Deviation Heatmap", width=700, height=400)
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Drop `old.jpeg` and `new.jpg` into the sidebar to compute real-time banking clearance scores.")