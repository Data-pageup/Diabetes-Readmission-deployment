import streamlit as st
from PIL import Image
import plotly.graph_objects as go

# ======================
# Page Configuration
# ======================
st.set_page_config(
    page_title="Diabetes Readmission Analysis",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# ======================
# Sidebar
# ======================
st.sidebar.image("https://img.icons8.com/color/96/000000/hospital-3.png", width=100)
st.sidebar.title("🏥 Diabetes Readmission Project")
st.sidebar.markdown("---")
section = st.sidebar.radio(
    "📊 Navigate to:",
    ["🏠 Home", "📁 Dataset Overview", "🤖 Classification Models", "🔍 Clustering Results"],
    index=0
)
st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip**: Use this dashboard to explore diabetes readmission predictions and patterns.")

# ======================
# 🏠 Home Page
# ======================
if section == "🏠 Home":
    st.markdown("<h1 class='main-header'>🏥 Diabetes Readmission Analysis Dashboard</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Total Records", "101,766", "Dataset Size")
    with col2:
        st.metric("📋 Features", "47", "Attributes")
    with col3:
        st.metric("🎯 Target Classes", "3", "Readmission Types")
    
    st.markdown("---")
    
    st.markdown("""
    ### 🎯 Project Overview
    This dashboard presents a comprehensive analysis of **diabetes patient readmission** patterns using 
    the **Diabetes 130-US Hospitals dataset**. 
    
    #### 🔬 What We Did:
    - **Data Preprocessing**: Cleaned and engineered features from 47 attributes
    - **Classification**: Built ensemble models (Bagging & Boosting) to predict readmission
    - **Clustering**: Discovered patient patterns using K-Means and Hierarchical clustering
    
    #### 🎯 Target Variable:
    - **NO**: No readmission
    - **>30**: Readmitted after 30 days
    - **<30**: Readmitted within 30 days
    
    #### 👈 Use the sidebar to explore different sections!
    """)
    
    # Target distribution visualization
    st.markdown("### 📊 Target Distribution")
    
    # Create a simple bar chart showing distribution
    fig = go.Figure(data=[
        go.Bar(
            x=['NO (0)', '>30 (1)', '<30 (2)'],
            y=[10973, 7109, 2272],
            marker_color=['#636EFA', '#EF553B', '#00CC96'],
            text=[10973, 7109, 2272],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Readmission Class Distribution (Test Set)",
        xaxis_title="Readmission Class",
        yaxis_title="Number of Patients",
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

# ======================
# 📁 Dataset Overview
# ======================
elif section == "📁 Dataset Overview":
    st.markdown("<h1 class='main-header'>📁 Dataset Overview</h1>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📊 Data Summary", "🛠️ Preprocessing"])
    
    with tab1:
        st.markdown("### 📊 Dataset Statistics")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='info-box'>", unsafe_allow_html=True)
            st.markdown("""
            **📈 Key Statistics:**
            - **Total Records**: 101,766
            - **Features**: 47
            - **Missing Values**: Handled ✅
            - **Data Source**: 130 US Hospitals
            - **Time Period**: 1999-2008
            """)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='info-box'>", unsafe_allow_html=True)
            st.markdown("""
            **🎯 Target Classes:**
            - **NO**: No readmission (53.9%)
            - **>30**: Readmitted after 30 days (34.9%)
            - **<30**: Readmitted within 30 days (11.2%)
            """)
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("### 📏 Dataset Information")
        st.markdown("""
        <div class='info-box'>
        
        **Key Features Include:**
        - **Patient Demographics**: Age, gender, race
        - **Admission Details**: Admission type, source, discharge disposition
        - **Medical History**: Number of diagnoses, procedures, medications
        - **Lab Results**: A1C test results, glucose levels
        - **Medications**: Changes in medication, diabetic medications prescribed
        - **Hospital Stay**: Time in hospital, number of lab procedures
        
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 🛠️ Preprocessing Pipeline")
        st.markdown("""
        <div class='info-box'>
        
        #### 1️⃣ Data Cleaning
        - Removed ID columns: `encounter_id`, `patient_nbr`
        - Handled missing values with appropriate imputation
        - Removed duplicates and outliers
        - Dropped columns with >50% missing values
        
        #### 2️⃣ Feature Engineering
        - **Categorical Encoding**: One-Hot and Label encoding
        - **Ordinal Features**: Mapped age ranges, A1C results to numeric scales
        - **Feature Scaling**: StandardScaler for numeric features
        - Created interaction features between medications and diagnoses
        
        #### 3️⃣ Data Splitting
        - **Train Set**: 80% (81,413 records)
        - **Test Set**: 20% (20,354 records)
        - Stratified split to maintain class distribution
        
        #### 4️⃣ Feature Selection
        - Removed low-variance features
        - Correlation analysis for redundancy
        - Selected most important features for modeling
        - Final feature count: 47 → 35 features used
        
        </div>
        """, unsafe_allow_html=True)

# ======================
# 🤖 Classification Models
# ======================
elif section == "🤖 Classification Models":
    st.markdown("<h1 class='main-header'>🤖 Classification Models</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    ### 🎯 Objective
    Predict whether a diabetes patient will be readmitted using ensemble learning techniques.
    """)
    
    # Model comparison
    st.markdown("### 📊 Model Performance Comparison")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.markdown("### 🌳 Bagging Classifier")
        st.markdown("#### 68.7%")
        st.markdown("Random Forest Base")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.markdown("### 🚀 Gradient Boosting")
        st.markdown("#### 69.8%")
        st.markdown("Best Performer 🏆")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Detailed metrics
    tab1, tab2, tab3 = st.tabs(["📈 Bagging Results", "🚀 Boosting Results", "⚖️ Comparison"])
    
    with tab1:
        st.markdown("### 🌳 Bagging Classifier (Random Forest)")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            **Model Details:**
            - **Algorithm**: Bagging with Random Forest
            - **Accuracy**: 68.68%
            - **Macro F1-Score**: 0.73
            - **Weighted F1-Score**: 0.67
            """)
        
        with col2:
            st.markdown("#### Classification Report")
            st.markdown("""
            | Class | Precision | Recall | F1-Score | Support |
            |-------|-----------|--------|----------|---------|
            | NO (0) | 0.67 | 0.84 | 0.74 | 10,973 |
            | >30 (1) | 0.59 | 0.35 | 0.44 | 7,109 |
            | <30 (2) | 1.00 | 1.00 | 1.00 | 2,272 |
            | **Accuracy** | | | **0.69** | **20,354** |
            """)
        
        st.markdown("### 📊 Confusion Matrix")
        try:
            bagging_img = Image.open("bagging_classifier.png")
            st.image(bagging_img, caption="Bagging Classifier Confusion Matrix", use_container_width=True)
        except:
            st.warning("⚠️ Confusion matrix image not found. Please ensure 'bagging_classifier.png' exists in the same directory.")
    
    with tab2:
        st.markdown("### 🚀 Gradient Boosting Classifier")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            **Model Details:**
            - **Algorithm**: Gradient Boosting
            - **Accuracy**: 69.82% 🏆
            - **Macro F1-Score**: 0.73
            - **Weighted F1-Score**: 0.67
            """)
        
        with col2:
            st.markdown("#### Classification Report")
            st.markdown("""
            | Class | Precision | Recall | F1-Score | Support |
            |-------|-----------|--------|----------|---------|
            | NO (0) | 0.67 | 0.87 | 0.76 | 10,973 |
            | >30 (1) | 0.62 | 0.34 | 0.44 | 7,109 |
            | <30 (2) | 1.00 | 1.00 | 1.00 | 2,272 |
            | **Accuracy** | | | **0.70** | **20,354** |
            """)
        
        st.markdown("### 📊 Confusion Matrix")
        try:
            boosting_img = Image.open("gradient_boosting.png")
            st.image(boosting_img, caption="Gradient Boosting Confusion Matrix", use_container_width=True)
        except:
            st.warning("⚠️ Confusion matrix image not found. Please ensure 'gradient_boosting.png' exists in the same directory.")
    
    with tab3:
        st.markdown("### ⚖️ Model Comparison")
        
        # Create comparison chart
        fig = go.Figure()
        
        models = ['Bagging', 'Boosting']
        accuracy = [68.68, 69.82]
        precision = [75, 76]
        recall = [73, 74]
        f1 = [73, 73]
        
        fig.add_trace(go.Bar(name='Accuracy', x=models, y=accuracy, text=accuracy, textposition='auto'))
        fig.add_trace(go.Bar(name='Macro Precision', x=models, y=precision, text=precision, textposition='auto'))
        fig.add_trace(go.Bar(name='Macro Recall', x=models, y=recall, text=recall, textposition='auto'))
        fig.add_trace(go.Bar(name='Macro F1', x=models, y=f1, text=f1, textposition='auto'))
        
        fig.update_layout(
            title="Model Performance Comparison (%)",
            xaxis_title="Model",
            yaxis_title="Score (%)",
            barmode='group',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("🏆 **Winner**: Gradient Boosting with 69.82% accuracy!")
        
        st.markdown("""
        ### 💡 Key Insights:
        - Both models achieve **perfect precision and recall (1.00)** for Class 2 (<30 days readmission)
        - **Gradient Boosting** slightly outperforms Bagging in overall accuracy (+1.14%)
        - Class 1 (>30 days) remains the most challenging to predict (lowest F1-score: 0.44)
        - Class 0 (NO readmission) has the best recall, especially in Boosting (0.87)
        - Boosting shows better precision for Class 1 (0.62 vs 0.59)
        
        ### 🎯 Model Strengths:
        - **Bagging**: Better balance between precision and recall for Class 0
        - **Boosting**: Superior overall accuracy and better Class 0 recall
        
        ### 📊 Class Imbalance Impact:
        - Class 2 (smallest class) has perfect scores, possibly due to distinct patterns
        - Class 1 (middle-sized) is most difficult to predict accurately
        - Both models struggle with Class 1, suggesting feature overlap with Class 0
        """)

# ======================
# 🔍 Clustering Results
# ======================
elif section == "🔍 Clustering Results":
    st.markdown("<h1 class='main-header'>🔍 Clustering Analysis</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    ### 🎯 Objective
    Discover hidden patterns and group similar patients using unsupervised learning techniques.
    """)
    
    tab1, tab2, tab3 = st.tabs(["🔵 K-Means", "🌳 Hierarchical", "📊 Insights"])
    
    with tab1:
        st.markdown("### 🔵 K-Means Clustering")
        st.markdown("""
        <div class='info-box'>
        
        **Algorithm**: K-Means  
        **Number of Clusters**: 3 (matching target classes)  
        **Purpose**: Partition patients into distinct groups based on feature similarity  
        **Visualization**: 2D PCA projection of clusters
        
        **How it works:**
        - Assigns each patient to the nearest cluster centroid
        - Iteratively refines cluster centers to minimize variance
        - Fast and efficient for large datasets
        
        </div>
        """, unsafe_allow_html=True)
        
        try:
            kmeans_img = Image.open("K-Means Clustering.png")
            st.image(kmeans_img, caption="K-Means Clustering (PCA Projection)", use_container_width=True)
        except:
            st.warning("⚠️ K-Means clustering image not found. Please ensure 'K-Means Clustering.png' exists in the same directory.")
    
    with tab2:
        st.markdown("### 🌳 Hierarchical Clustering")
        st.markdown("""
        <div class='info-box'>
        
        **Algorithm**: Agglomerative Hierarchical Clustering  
        **Linkage Method**: Ward (minimizes variance)  
        **Purpose**: Build a hierarchy of clusters to understand patient relationships  
        **Visualization**: Dendrogram showing cluster formation process
        
        **How it works:**
        - Starts with each patient as a separate cluster
        - Iteratively merges the closest clusters
        - Creates a tree structure (dendrogram) showing relationships
        - Can cut at different heights for varying cluster numbers
        
        </div>
        """, unsafe_allow_html=True)
        
        try:
            hierarchical_img = Image.open("Hierarchical Clustering Dendrogram.png")
            st.image(hierarchical_img, caption="Hierarchical Clustering Dendrogram", use_container_width=True)
        except:
            st.warning("⚠️ Hierarchical clustering image not found. Please ensure 'Hierarchical Clustering Dendrogram.png' exists in the same directory.")
    
    with tab3:
        st.markdown("### 📊 Clustering vs Actual Classes")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🎯 Actual Readmission Classes")
            try:
                actual_img = Image.open("Actual Readmission Classes.png")
                st.image(actual_img, use_container_width=True)
            except:
                st.warning("⚠️ Actual classes image not found. Please ensure 'Actual Readmission Classes.png' exists in the same directory.")
        
        with col2:
            st.markdown("#### 🔍 Key Findings")
            st.markdown("""
            <div class='info-box'>
            
            **Clustering Results:**
            - Clusters reveal distinct patient groups based on medical history and treatment
            - Some overlap between readmission types suggests similarity in patient characteristics
            - Clustering identifies patterns not immediately obvious from supervised learning
            
            **Clinical Applications:**
            - 🎯 Patient segmentation for targeted care programs
            - 📊 Resource allocation optimization
            - 🏥 Personalized treatment planning
            - 💊 Medication management strategies
            - 🔔 Early warning system for high-risk patients
            
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("""
        ### 💡 Clustering Insights & Comparison:
        
        #### 🔵 K-Means Advantages:
        - Fast computation, scalable to large datasets
        - Works well when clusters are spherical and similar in size
        - Easy to implement and interpret
        - Good for patient segmentation in real-time systems
        
        #### 🌳 Hierarchical Advantages:
        - Provides complete hierarchy of relationships
        - No need to specify number of clusters upfront
        - Dendrogram visualization helps understand data structure
        - Better for understanding patient similarity at multiple levels
        
        #### 🎯 Practical Use Cases:
        1. **Risk Stratification**: Group patients by readmission risk level
        2. **Care Pathways**: Design targeted interventions for each cluster
        3. **Resource Planning**: Allocate medical resources based on cluster needs
        4. **Quality Improvement**: Identify clusters with poor outcomes for focused improvement
        
        #### 📈 Model Performance Note:
        While clustering is unsupervised, comparing clusters to actual readmission classes helps:
        - Validate if natural patient groups align with readmission outcomes
        - Identify additional risk factors not captured by readmission labels
        - Support development of more nuanced patient classification systems
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🏥 Diabetes Readmission Analysis Dashboard | Built with Streamlit</p>
    <p style='font-size: 0.8rem;'>Dataset: Diabetes 130-US Hospitals (1999-2008) | Models: Bagging & Boosting Classifiers</p>
</div>
""", unsafe_allow_html=True)