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
st.set_page_config(page_title="Signature Verification AI", layout="wide")

st.title("✒️ Deep Signature Analysis & Verification")
st.markdown("Upload a baseline signature and a new signature to analyze structural drift, visual variances, and deep AI match metrics.")

# 1. Load Pretrained Deep Learning Model
@st.cache_resource
def load_feature_extractor():
    # Using ResNet50 weights for robust geometric feature extraction
    weights = models.ResNet50_Weights.DEFAULT
    model = models.resnet50(weights=weights)
    # Mutate the network to act as a feature extractor instead of a classifier
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
    """Convert to grayscale, resize, and normalize for structural comparison."""
    img_np = np.array(image_pil)
    if len(img_np.shape) == 3:
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    else:
        gray = img_np
    resized = cv2.resize(gray, target_size)
    return resized

def extract_deep_features(image_pil, model, transform):
    """Pass image through ResNet to extract the deep latent feature vector."""
    # Ensure 3-channel RGB image for CNN
    img_rgb = image_pil.convert("RGB")
    tensor = transform(img_rgb).unsqueeze(0) # Add batch dimension
    with torch.no_grad():
        embedding = model(tensor).flatten().numpy()
    return embedding

# 3. Sidebar Frontend Layout for File Uploads
st.sidebar.header("📥 Upload Signatures")
old_file = st.sidebar.file_uploader("Upload Baseline Signature (old.jpeg)", type=["jpg", "jpeg", "png"])
new_file = st.sidebar.file_uploader("Upload Verification Signature (new.jpg)", type=["jpg", "jpeg", "png"])

# 4. Main App Logic
if old_file and new_file:
    # Load PIL Images
    img_old = Image.open(old_file)
    img_new = Image.open(new_file)
    
    # Display Inputs Side-by-Side
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Reference Signature (Old)")
        st.image(img_old, use_container_width=True)
    with col2:
        st.subheader("Verification Signature (New)")
        st.image(img_new, use_container_width=True)
        
    st.write("---")
    st.subheader("🔬 Deep Analysis Metrics")
    
    with st.spinner("Running deep tensor analysis and structural evaluation..."):
        # Process for CV analysis
        gray_old = preprocess_for_ssim(img_old)
        gray_new = preprocess_for_ssim(img_new)
        
        # Track 1: Structural Similarity
        ssim_score, diff_map = ssim(gray_old, gray_new, full=True)
        
        # Track 2: Deep Feature Extraction & Cosine Similarity
        feat_old = extract_deep_features(img_old, model, preprocess_transform)
        feat_new = extract_deep_features(img_new, model, preprocess_transform)
        
        cosine_sim = np.dot(feat_old, feat_new) / (np.linalg.norm(feat_old) * np.linalg.norm(feat_new))
        
        # Scale to clean percentages
        deep_match_pct = max(0.0, min(100.0, cosine_sim * 100))
        structural_match_pct = max(0.0, min(100.0, ssim_score * 100))
        
        # Hybrid Metric (Weighted Blend)
        final_confidence = (deep_match_pct * 0.7) + (structural_match_pct * 0.3)
        
    # Display KPI Metrics Dashboard
    m1, m2, m3 = st.columns(3)
    m1.metric(label="AI Deep Feature Match", value=f"{deep_match_pct:.2f}%")
    m2.metric(label="Structural Topology Match", value=f"{structural_match_pct:.2f}%")
    
    if final_confidence > 85:
        m3.metric(label="Verification Verdict", value="VERIFIED", delta="High Confidence Match")
    elif final_confidence > 70:
        m3.metric(label="Verification Verdict", value="SUSPICIOUS", delta="- Marginal Variance Found", delta_color="inverse")
    else:
        m3.metric(label="Verification Verdict", value="MISMATCH", delta="- Low Pattern Similarity", delta_color="inverse")

    st.write("---")
    st.subheader("🗺️ Spatial Discrepancies & Stroke Heatmap")
    st.markdown("The heatmap below flags specific regions where the strokes deviate. **Bright areas/peaks** indicate major variations in line weight, curves, or missing stroke intersections.")
    
    # Generate Visual Difference Heatmap using Plotly
    # Invert the difference map so disparities light up brightly
    inverted_diff = 255 - (diff_map * 255).astype(np.uint8)
    
    # Create interactive surface/heatmap using Plotly for precision inspection
    fig = px.imshow(
        inverted_diff, 
        color_continuous_scale='Jet', 
        labels=dict(color="Variance Intensity")
    )
    fig.update_layout(coloraxis_showscale=True, width=800, height=500)
    st.plotly_chart(fig, use_container_width=True)

    # Detailed AI Insights Log
    st.write("### 📝 Detailed Diagnostics")
    with st.expander("See Complete Technical Breakdown"):
        st.write(f"**Structural Drift Description:** The basic canvas alignment shares a `{structural_match_pct:.2f}%` structural alignment. This flags macro-level scale discrepancies or major angle tilts.")
        st.write(f"**Deep Behavioral Vectors:** The latent neural response scored `{deep_match_pct:.2f}%`. Because this filters out light variance and focuses exclusively on fine geometric features, it heavily dictates the final verification verdict.")
        
else:
    st.info("💡 Please upload both standard files from the sidebar menu to begin pipeline execution.")