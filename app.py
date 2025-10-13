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

# Custom CSS for better styling with new color scheme
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary: #2E86AB;
        --secondary: #A23B72;
        --accent: #F18F01;
        --success: #06A77D;
        --dark: #1A1A2E;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
    }
    
    /* Headers */
    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        padding: 20px 0;
    }
    
    .section-header {
        font-size: 2rem;
        font-weight: 700;
        color: #2E86AB;
        margin: 30px 0 20px 0;
        padding-bottom: 10px;
        border-bottom: 3px solid #F18F01;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #2E86AB 0%, #A23B72 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(to right, #ffffff 0%, #f8f9fa 100%);
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #2E86AB;
        color: #1A1A2E;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        margin: 15px 0;
    }
    
    .info-box h4 {
        color: #2E86AB;
        margin-top: 0;
    }
    
    /* Highlight box */
    .highlight-box {
        background: linear-gradient(135deg, #F18F01 0%, #F9A825 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        box-shadow: 0 6px 12px rgba(241, 143, 1, 0.3);
        margin: 20px 0;
    }
    
    /* Success box */
    .success-box {
        background: linear-gradient(135deg, #06A77D 0%, #00BFA5 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        box-shadow: 0 6px 12px rgba(6, 167, 125, 0.3);
        margin: 20px 0;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2E86AB 0%, #1A5F7A 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Stats container */
    .stats-container {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        margin: 15px 0;
    }
    
    /* Table styling */
    .dataframe {
        border-radius: 8px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ======================
# Sidebar
# ======================
st.sidebar.markdown("""
    <div style='text-align: center; padding: 30px 20px; background: rgba(255,255,255,0.1); border-radius: 10px; margin-bottom: 20px;'>
        <h1 style='color: white; font-size: 1.8rem; margin: 0; font-weight: 700; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
            Diabetes Readmission
        </h1>
        <p style='color: #E0E0E0; font-size: 0.95rem; margin-top: 8px; font-weight: 300;'>
            Machine Learning Analysis
        </p>
    </div>
""", unsafe_allow_html=True)

section = st.sidebar.radio(
    "📊 Navigate",
    ["🏠 Home", "📁 Dataset Overview", "🤖 Classification Models", "🔍 Clustering Results"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style='background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px;'>
    <p style='margin: 0; font-size: 0.9rem;'>💡 <strong>Tip</strong></p>
    <p style='margin: 5px 0 0 0; font-size: 0.85rem; opacity: 0.9;'>
        Explore predictions and patterns in diabetes patient readmissions
    </p>
</div>
""", unsafe_allow_html=True)

# ======================
# 🏠 Home Page
# ======================
if section == "🏠 Home":
    st.markdown("<h1 class='main-header'>Diabetes Readmission Analysis Dashboard</h1>", unsafe_allow_html=True)
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📊 Total Records", "101,766", "10 Years Data")
    with col2:
        st.metric("🏥 Hospitals", "130", "US Facilities")
    with col3:
        st.metric("📋 Features", "50+", "Attributes")
    with col4:
        st.metric("🎯 Classes", "3", "Outcomes")
    
    st.markdown("---")
    
    # Project Overview
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class='info-box'>
            <h3 style='color: #2E86AB; margin-top: 0;'>🎯 Project Overview</h3>
            <p style='font-size: 1.05rem; line-height: 1.8;'>
                This dashboard presents a comprehensive analysis of <strong>diabetes patient readmission patterns</strong> 
                using advanced machine learning techniques on a decade of clinical data from 130 US hospitals.
            </p>
            <p style='font-size: 1.05rem; line-height: 1.8;'>
                Our goal is to predict early readmission within 30 days of discharge, enabling healthcare providers 
                to implement preventive interventions and improve patient outcomes.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='highlight-box'>
            <h4 style='margin-top: 0;'>🔬 Analysis Pipeline</h4>
            <ul style='margin: 10px 0; line-height: 2;'>
                <li><strong>Data Preprocessing:</strong> Feature engineering from 50+ clinical attributes</li>
                <li><strong>Classification:</strong> Ensemble models (Bagging & Boosting) achieving ~70% accuracy</li>
                <li><strong>Clustering:</strong> Patient segmentation using K-Means and Hierarchical methods</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='success-box'>
            <h4 style='margin-top: 0;'>🎯 Target Classes</h4>
            <div style='margin: 15px 0;'>
                <div style='background: rgba(255,255,255,0.2); padding: 12px; border-radius: 8px; margin: 10px 0;'>
                    <strong>NO (53.9%)</strong><br>
                    <span style='font-size: 0.9rem;'>No readmission after discharge</span>
                </div>
                <div style='background: rgba(255,255,255,0.2); padding: 12px; border-radius: 8px; margin: 10px 0;'>
                    <strong>>30 (34.9%)</strong><br>
                    <span style='font-size: 0.9rem;'>Readmitted after 30 days</span>
                </div>
                <div style='background: rgba(255,255,255,0.2); padding: 12px; border-radius: 8px; margin: 10px 0;'>
                    <strong><30 (11.2%)</strong><br>
                    <span style='font-size: 0.9rem;'>Readmitted within 30 days</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Target distribution visualization
    st.markdown("<h2 class='section-header'>📊 Target Distribution Analysis</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = go.Figure(data=[
            go.Bar(
                x=['NO (0)', '>30 (1)', '<30 (2)'],
                y=[10973, 7109, 2272],
                marker=dict(
                    color=['#2E86AB', '#A23B72', '#F18F01'],
                    line=dict(color='white', width=2)
                ),
                text=[10973, 7109, 2272],
                textposition='auto',
                textfont=dict(size=14, color='white', family='Arial Black')
            )
        ])
        
        fig.update_layout(
            title=dict(
                text="Readmission Class Distribution (Test Set)",
                font=dict(size=20, color='#1A1A2E', family='Arial Black')
            ),
            xaxis_title="Readmission Class",
            yaxis_title="Number of Patients",
            height=400,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12, color='#1A1A2E')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class='info-box'>
            <h4>📈 Key Statistics</h4>
            <ul style='line-height: 2;'>
                <li><strong>Test Set Size:</strong> 20,354 patients</li>
                <li><strong>Majority Class:</strong> NO readmission (54%)</li>
                <li><strong>High Risk:</strong> <30 days (11%)</li>
                <li><strong>Class Imbalance:</strong> Present, addressed in modeling</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ======================
# 📁 Dataset Overview
# ======================
elif section == "📁 Dataset Overview":
    st.markdown("<h1 class='main-header'>📁 Dataset Overview</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 About Dataset", "🔍 Data Summary", "🛠️ Preprocessing"])
    
    with tab1:
        st.markdown("<h2 class='section-header'>📖 About the Dataset</h2>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='info-box'>
            <h4>🏥 Clinical Context</h4>
            <p style='font-size: 1.05rem; line-height: 1.8;'>
                The dataset represents <strong>ten years (1999-2008)</strong> of clinical care at <strong>130 US hospitals</strong> 
                and integrated delivery networks. Each row concerns hospital records of patients diagnosed with diabetes, 
                who underwent laboratory tests, received medications, and stayed up to 14 days.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='highlight-box'>
            <h4 style='margin-top: 0;'>🎯 Problem Statement</h4>
            <p style='line-height: 1.8;'>
                The goal is to determine the <strong>early readmission of the patient within 30 days of discharge</strong>. 
                This problem is critical because despite high-quality evidence showing improved clinical outcomes for 
                diabetic patients who receive various preventive and therapeutic interventions, many patients do not receive them.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class='info-box'>
                <h4>⚠️ Why This Matters</h4>
                <ul style='line-height: 2;'>
                    <li><strong>Arbitrary diabetes management</strong> in hospital environments fails to attend to glycemic control</li>
                    <li><strong>Increased costs</strong> for hospitals due to patient readmissions</li>
                    <li><strong>Higher morbidity and mortality</strong> for patients facing diabetes complications</li>
                    <li><strong>Preventable outcomes</strong> through proper diabetes care protocols</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='info-box'>
                <h4>📋 Inclusion Criteria</h4>
                <ol style='line-height: 2;'>
                    <li><strong>Inpatient encounter</strong> (hospital admission)</li>
                    <li><strong>Diabetic encounter</strong> (diabetes diagnosis entered)</li>
                    <li><strong>Length of stay:</strong> 1-14 days</li>
                    <li><strong>Laboratory tests</strong> performed during encounter</li>
                    <li><strong>Medications</strong> administered during encounter</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='success-box'>
            <h4 style='margin-top: 0;'>📊 Dataset Attributes (50+ Features)</h4>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;'>
                <div>
                    <strong>👤 Patient Demographics:</strong>
                    <ul style='margin-top: 5px;'>
                        <li>Patient number, race, gender, age</li>
                    </ul>
                </div>
                <div>
                    <strong>🏥 Admission Details:</strong>
                    <ul style='margin-top: 5px;'>
                        <li>Admission type, source, discharge disposition</li>
                    </ul>
                </div>
                <div>
                    <strong>🔬 Medical History:</strong>
                    <ul style='margin-top: 5px;'>
                        <li>Number of diagnoses, procedures, medications</li>
                    </ul>
                </div>
                <div>
                    <strong>📈 Lab Results:</strong>
                    <ul style='margin-top: 5px;'>
                        <li>HbA1c test results, glucose levels</li>
                    </ul>
                </div>
                <div>
                    <strong>💊 Medications:</strong>
                    <ul style='margin-top: 5px;'>
                        <li>Changes in medication, diabetic medications prescribed</li>
                    </ul>
                </div>
                <div>
                    <strong>⏱️ Hospital Stay:</strong>
                    <ul style='margin-top: 5px;'>
                        <li>Time in hospital, number of lab procedures</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<h2 class='section-header'>📊 Dataset Statistics</h2>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class='info-box'>
                <h4>📈 Size Metrics</h4>
                <ul style='line-height: 2;'>
                    <li><strong>Total Records:</strong> 101,766</li>
                    <li><strong>Features:</strong> 50+</li>
                    <li><strong>Time Period:</strong> 1999-2008</li>
                    <li><strong>Hospitals:</strong> 130 US facilities</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='info-box'>
                <h4>🎯 Target Distribution</h4>
                <ul style='line-height: 2;'>
                    <li><strong>NO:</strong> 53.9% (No readmission)</li>
                    <li><strong>>30:</strong> 34.9% (After 30 days)</li>
                    <li><strong><30:</strong> 11.2% (Within 30 days)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class='info-box'>
                <h4>✅ Data Quality</h4>
                <ul style='line-height: 2;'>
                    <li><strong>Missing Values:</strong> Handled ✅</li>
                    <li><strong>Duplicates:</strong> Removed ✅</li>
                    <li><strong>Outliers:</strong> Addressed ✅</li>
                    <li><strong>Validation:</strong> Complete ✅</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<h2 class='section-header'>🛠️ Preprocessing Pipeline</h2>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='info-box'>
            <h4>1️⃣ Data Cleaning</h4>
            <ul style='line-height: 2;'>
                <li>Removed ID columns: <code>encounter_id</code>, <code>patient_nbr</code></li>
                <li>Handled missing values with appropriate imputation strategies</li>
                <li>Removed duplicates and statistical outliers</li>
                <li>Dropped columns with >50% missing values</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class='info-box'>
                <h4>2️⃣ Feature Engineering</h4>
                <ul style='line-height: 2;'>
                    <li><strong>Categorical Encoding:</strong> One-Hot and Label encoding</li>
                    <li><strong>Ordinal Features:</strong> Age ranges, A1C results mapped to numeric scales</li>
                    <li><strong>Feature Scaling:</strong> StandardScaler for numeric features</li>
                    <li><strong>Interactions:</strong> Created medication-diagnosis interactions</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='info-box'>
                <h4>3️⃣ Data Splitting</h4>
                <ul style='line-height: 2;'>
                    <li><strong>Train Set:</strong> 80% (81,413 records)</li>
                    <li><strong>Test Set:</strong> 20% (20,354 records)</li>
                    <li><strong>Stratification:</strong> Maintained class distribution</li>
                    <li><strong>Validation:</strong> Cross-validation performed</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='success-box'>
            <h4 style='margin-top: 0;'>4️⃣ Feature Selection</h4>
            <p style='line-height: 1.8;'>
                Applied comprehensive feature selection techniques to optimize model performance:
            </p>
            <ul style='line-height: 2;'>
                <li><strong>Variance Thresholding:</strong> Removed low-variance features</li>
                <li><strong>Correlation Analysis:</strong> Eliminated redundant features (correlation >0.95)</li>
                <li><strong>Feature Importance:</strong> Selected top features using Random Forest importance scores</li>
                <li><strong>Final Feature Count:</strong> 50+ → 35 features used in modeling</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ======================
# 🤖 Classification Models
# ======================
elif section == "🤖 Classification Models":
    st.markdown("<h1 class='main-header'>🤖 Classification Models</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='highlight-box'>
        <h3 style='margin-top: 0;'>🎯 Objective</h3>
        <p style='font-size: 1.1rem; line-height: 1.8; margin: 0;'>
            Predict whether a diabetes patient will be readmitted using ensemble learning techniques,
            enabling healthcare providers to implement preventive interventions for high-risk patients.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Model comparison
    st.markdown("<h2 class='section-header'>📊 Model Performance</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #2E86AB 0%, #1A5F7A 100%); padding: 40px; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(0,0,0,0.1);'>
            <h3 style='color: white; margin: 0;'>🌳 Bagging Classifier</h3>
            <h1 style='color: white; font-size: 4rem; margin: 20px 0;'>68.7%</h1>
            <p style='color: #E0E0E0; font-size: 1.1rem; margin: 0;'>Random Forest Base</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #F18F01 0%, #C46D00 100%); padding: 40px; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(241,143,1,0.3);'>
            <h3 style='color: white; margin: 0;'>🚀 Gradient Boosting</h3>
            <h1 style='color: white; font-size: 4rem; margin: 20px 0;'>69.8%</h1>
            <p style='color: white; font-size: 1.1rem; margin: 0;'>Best Performer 🏆</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Detailed metrics
    tab1, tab2, tab3 = st.tabs(["📈 Bagging Results", "🚀 Boosting Results", "⚖️ Comparison"])
    
    with tab1:
        st.markdown("<h2 class='section-header'>🌳 Bagging Classifier (Random Forest)</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            <div class='info-box'>
                <h4>Model Details</h4>
                <ul style='line-height: 2;'>
                    <li><strong>Algorithm:</strong> Bagging with Random Forest</li>
                    <li><strong>Accuracy:</strong> 68.68%</li>
                    <li><strong>Macro F1:</strong> 0.73</li>
                    <li><strong>Weighted F1:</strong> 0.67</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 📊 Classification Report")
            st.markdown("""
            <div class='stats-container'>
            
            | Class | Precision | Recall | F1-Score | Support |
            |-------|-----------|--------|----------|---------|
            | **NO (0)** | 0.67 | 0.84 | 0.74 | 10,973 |
            | **>30 (1)** | 0.59 | 0.35 | 0.44 | 7,109 |
            | **<30 (2)** | 1.00 | 1.00 | 1.00 | 2,272 |
            | **Accuracy** | | | **0.69** | **20,354** |
            
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 📊 Confusion Matrix")
        try:
            bagging_img = Image.open("bagging_classifier.png")
            st.image(bagging_img, caption="Bagging Classifier Confusion Matrix", use_container_width=True)
        except:
            st.warning("⚠️ Confusion matrix image not found. Please ensure 'bagging_classifier.png' exists in the same directory.")
    
    with tab2:
        st.markdown("<h2 class='section-header'>🚀 Gradient Boosting Classifier</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            <div class='info-box'>
                <h4>Model Details</h4>
                <ul style='line-height: 2;'>
                    <li><strong>Algorithm:</strong> Gradient Boosting</li>
                    <li><strong>Accuracy:</strong> 69.82% 🏆</li>
                    <li><strong>Macro F1:</strong> 0.73</li>
                    <li><strong>Weighted F1:</strong> 0.67</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 📊 Classification Report")
            st.markdown("""
            <div class='stats-container'>
            
            | Class | Precision | Recall | F1-Score | Support |
            |-------|-----------|--------|----------|---------|
            | **NO (0)** | 0.67 | 0.87 | 0.76 | 10,973 |
            | **>30 (1)** | 0.62 | 0.34 | 0.44 | 7,109 |
            | **<30 (2)** | 1.00 | 1.00 | 1.00 | 2,272 |
            | **Accuracy** | | | **0.70** | **20,354** |
            
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 📊 Confusion Matrix")
        try:
            boosting_img = Image.open("gradient_boosting.png")
            st.image(boosting_img, caption="Gradient Boosting Confusion Matrix", use_container_width=True)
        except:
            st.warning("⚠️ Confusion matrix image not found. Please ensure 'gradient_boosting.png' exists in the same directory.")
    
    with tab3:
        st.markdown("<h2 class='section-header'>⚖️ Model Comparison</h2>", unsafe_allow_html=True)
        
        # Create comparison chart
        fig = go.Figure()
        
        models = ['Bagging', 'Boosting']
        accuracy = [68.68, 69.82]
        precision = [75, 76]
        recall = [73, 74]
        f1 = [73, 73]
        
        fig.add_trace(go.Bar(
            name='Accuracy',
            x=models,
            y=accuracy,
            text=accuracy,
            textposition='auto',
            marker_color='#2E86AB'
        ))
        fig.add_trace(go.Bar(
            name='Macro Precision',
            x=models,
            y=precision,
            text=precision,
            textposition='auto',
            marker_color='#A23B72'
        ))
        fig.add_trace(go.Bar(
            name='Macro Recall',
            x=models,
            y=recall,
            text=recall,
            textposition='auto',
            marker_color='#F18F01'
        ))
        fig.add_trace(go.Bar(
            name='Macro F1',
            x=models,
            y=f1,
            text=f1,
            textposition='auto',
            marker_color='#06A77D'
        ))
        
        fig.update_layout(
            title=dict(
                text="Model Performance Comparison (%)",
                font=dict(size=20, color='#1A1A2E')
            ),
            xaxis_title="Model",
            yaxis_title="Score (%)",
            barmode='group',
            height=450,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class='success-box'>
            <h4 style='margin-top: 0;'>🏆 Winner: Gradient Boosting with 69.82% accuracy!</h4>
            <p style='margin: 0; line-height: 1.8;'>
                Gradient Boosting outperforms Bagging by 1.14%, showing better overall prediction capability.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class='info-box'>
                <h4>💡 Key Insights</h4>
                <ul style='line-height: 2;'>
                    <li>Both models achieve <strong>perfect precision and recall (1.00)</strong> for Class 2 (<30 days)</li>
                    <li>Gradient Boosting shows <strong>+1.14% better accuracy</strong></li>
                    <li>Class 1 (>30 days) is most challenging (F1: 0.44)</li>
                    <li>Class 0 has excellent recall in Boosting (0.87)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='info-box'>
                <h4>🎯 Model Strengths</h4>
                <ul style='line-height: 2;'>
                    <li><strong>Bagging:</strong> Better precision-recall balance for Class 0</li>
                    <li><strong>Boosting:</strong> Superior overall accuracy and Class 0 recall</li>
                    <li><strong>Both:</strong> Perfect performance on Class 2 (distinct patterns)</li>
                    <li><strong>Challenge:</strong> Class 1 overlaps with Class 0 features</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# ======================
# 🔍 Clustering Results
# ======================
elif section == "🔍 Clustering Results":
    st.markdown("<h1 class='main-header'>🔍 Clustering Analysis</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='highlight-box'>
        <h3 style='margin-top: 0;'>🎯 Objective</h3>
        <p style='font-size: 1.1rem; line-height: 1.8; margin: 0;'>
            Discover hidden patterns and group similar patients using unsupervised learning techniques
            to enable targeted interventions and personalized care strategies.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🔵 K-Means", "🌳 Hierarchical", "📊 Insights"])
    
    with tab1:
        st.markdown("<h2 class='section-header'>🔵 K-Means Clustering</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div class='info-box'>
                <h4>Algorithm Details</h4>
                <ul style='line-height: 2;'>
                    <li><strong>Method:</strong> K-Means Clustering</li>
                    <li><strong>Number of Clusters:</strong> 3 (matching target classes)</li>
                    <li><strong>Purpose:</strong> Partition patients into distinct groups</li>
                    <li><strong>Visualization:</strong> 2D PCA projection</li>
                </ul>
                
                <h4 style='margin-top: 20px;'>How It Works</h4>
                <ul style='line-height: 2;'>
                    <li>Assigns each patient to nearest cluster centroid</li>
                    <li>Iteratively refines cluster centers to minimize variance</li>
                    <li>Fast and efficient for large datasets</li>
                    <li>Creates spherical, evenly-sized clusters</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='success-box'>
                <h4 style='margin-top: 0;'>✨ Advantages</h4>
                <ul style='line-height: 2; margin: 10px 0;'>
                    <li>⚡ Fast computation</li>
                    <li>📈 Scalable to large datasets</li>
                    <li>💡 Easy to interpret</li>
                    <li>🎯 Good for real-time systems</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 📊 Clustering Visualization")
        try:
            kmeans_img = Image.open("K-Means Clustering.png")
            st.image(kmeans_img, caption="K-Means Clustering (PCA Projection)", use_container_width=True)
        except:
            st.warning("⚠️ K-Means clustering image not found. Please ensure 'K-Means Clustering.png' exists in the same directory.")
    
    with tab2:
        st.markdown("<h2 class='section-header'>🌳 Hierarchical Clustering</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div class='info-box'>
                <h4>Algorithm Details</h4>
                <ul style='line-height: 2;'>
                    <li><strong>Method:</strong> Agglomerative Hierarchical Clustering</li>
                    <li><strong>Linkage Method:</strong> Ward (minimizes variance)</li>
                    <li><strong>Purpose:</strong> Build hierarchy of patient relationships</li>
                    <li><strong>Visualization:</strong> Dendrogram showing cluster formation</li>
                </ul>
                
                <h4 style='margin-top: 20px;'>How It Works</h4>
                <ul style='line-height: 2;'>
                    <li>Starts with each patient as separate cluster</li>
                    <li>Iteratively merges closest clusters</li>
                    <li>Creates tree structure showing relationships</li>
                    <li>Can cut at different heights for varying cluster numbers</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='success-box'>
                <h4 style='margin-top: 0;'>✨ Advantages</h4>
                <ul style='line-height: 2; margin: 10px 0;'>
                    <li>🌲 Complete hierarchy</li>
                    <li>🔍 No preset cluster count</li>
                    <li>📊 Visual dendrogram</li>
                    <li>🎯 Multi-level insights</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 📊 Dendrogram Visualization")
        try:
            hierarchical_img = Image.open("Hierarchical Clustering Dendrogram.png")
            st.image(hierarchical_img, caption="Hierarchical Clustering Dendrogram", use_container_width=True)
        except:
            st.warning("⚠️ Hierarchical clustering image not found. Please ensure 'Hierarchical Clustering Dendrogram.png' exists in the same directory.")
    
    with tab3:
        st.markdown("<h2 class='section-header'>📊 Clustering Insights & Applications</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🎯 Actual Readmission Classes")
            try:
                actual_img = Image.open("Actual Readmission Classes.png")
                st.image(actual_img, use_container_width=True)
            except:
                st.warning("⚠️ Actual classes image not found. Please ensure 'Actual Readmission Classes.png' exists in the same directory.")
        
        with col2:
            st.markdown("""
            <div class='highlight-box'>
                <h4 style='margin-top: 0;'>🔍 Key Findings</h4>
                <ul style='line-height: 2; margin: 10px 0;'>
                    <li>Clusters reveal <strong>distinct patient groups</strong> based on medical history</li>
                    <li>Some overlap suggests <strong>similarity in characteristics</strong></li>
                    <li>Identifies patterns <strong>not obvious from supervised learning</strong></li>
                    <li>Enables <strong>risk stratification</strong> beyond simple labels</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("### 🏥 Clinical Applications")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class='info-box'>
                <h4>🎯 Patient Segmentation</h4>
                <p style='line-height: 1.8;'>
                    Group patients by readmission risk level for targeted care programs
                    and personalized treatment strategies.
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='info-box'>
                <h4>📊 Resource Allocation</h4>
                <p style='line-height: 1.8;'>
                    Optimize hospital resources and medical staff allocation based on
                    cluster-specific needs and risk profiles.
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class='info-box'>
                <h4>💊 Treatment Planning</h4>
                <p style='line-height: 1.8;'>
                    Design cluster-specific medication management strategies and
                    care pathways for improved outcomes.
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("### 💡 Comprehensive Analysis")
        
        st.markdown("""
        <div class='info-box'>
            <h4>🎯 Practical Use Cases</h4>
            <ol style='line-height: 2;'>
                <li><strong>Risk Stratification:</strong> Group patients by readmission risk level for early intervention</li>
                <li><strong>Care Pathways:</strong> Design targeted interventions for each cluster with specific protocols</li>
                <li><strong>Resource Planning:</strong> Allocate medical resources based on cluster needs and capacity</li>
                <li><strong>Quality Improvement:</strong> Identify clusters with poor outcomes for focused improvement efforts</li>
                <li><strong>Preventive Care:</strong> Develop cluster-specific preventive strategies to reduce readmissions</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class='info-box'>
                <h4>📈 Clustering vs Supervised Learning</h4>
                <p style='line-height: 1.8;'>
                    Comparing clusters to actual readmission classes helps:
                </p>
                <ul style='line-height: 2;'>
                    <li>Validate if natural patient groups align with outcomes</li>
                    <li>Identify additional risk factors not captured by labels</li>
                    <li>Support development of nuanced classification systems</li>
                    <li>Discover hidden patterns in patient populations</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='success-box'>
                <h4 style='margin-top: 0;'>🌟 Impact on Patient Care</h4>
                <p style='line-height: 1.8;'>
                    Clustering enables:
                </p>
                <ul style='line-height: 2; margin: 10px 0;'>
                    <li>🔔 <strong>Early Warning Systems</strong> for high-risk patients</li>
                    <li>💊 <strong>Personalized Medication</strong> management</li>
                    <li>📅 <strong>Follow-up Scheduling</strong> optimization</li>
                    <li>🏥 <strong>Discharge Planning</strong> improvements</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 30px 0;'>
    <h3 style='color: #2E86AB; margin: 0;'>🏥 Diabetes Readmission Analysis Dashboard</h3>
    <p style='color: #666; font-size: 0.95rem; margin: 10px 0;'>Built with Streamlit • Powered by Machine Learning</p>
    <p style='color: #999; font-size: 0.85rem; margin: 5px 0;'>Dataset: Diabetes 130-US Hospitals (1999-2008)</p>
    <p style='color: #999; font-size: 0.85rem; margin: 5px 0;'>Models: Bagging & Gradient Boosting Classifiers</p>
</div>
""", unsafe_allow_html=True)
