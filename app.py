import streamlit as st
import pandas as pd
import plotly.express as px
from transformers import pipeline
import time
from datetime import datetime
import json
import asyncio
from edge_tts import Communicate
from io import BytesIO
import os

# Set page config
st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stTitle {
        color: #1f77b4;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False
if 'audio_cache' not in st.session_state:
    st.session_state.audio_cache = {}

# Text-to-speech function with caching
async def generate_tts_audio(text: str) -> BytesIO:
    """Generate audio using edge-tts with caching"""
    # Use en-US-AriaNeural for better compatibility
    communicate = Communicate(text, voice="en-US-AriaNeural")
    audio_stream = BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_stream.write(chunk["data"])
    audio_stream.seek(0)
    return audio_stream

# Load model with caching
@st.cache_resource
def load_sentiment_model():
    """Load the pre-trained sentiment analysis model"""
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Main title
st.markdown("<h1 class='stTitle'>🤖 AI Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings & Controls")
    st.markdown("---")
    
    # Model info
    st.subheader("📊 Model Information")
    st.info("""
    **Model**: DistilBERT (Fine-tuned on SST-2)
    
    **Task**: Sentiment Analysis (Positive/Negative)
    
    **Type**: Pre-trained Transformer
    
    **Size**: Lightweight & Fast
    """)
    
    st.markdown("---")
    
    # Clear history button
    if st.button("🗑️ Clear History", use_container_width=True):
        st.session_state.history = []
        st.success("History cleared!")
    
    st.markdown("---")
    
    # About section
    st.subheader("ℹ️ About")
    st.write("""
    This AI application uses a pre-trained DistilBERT model 
    to analyze the sentiment of text input. It can classify 
    text as positive or negative with confidence scores.
    
    Simply enter your text and get instant sentiment analysis!
    """)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Input Text Analysis")
    
    # Text input area
    user_text = st.text_area(
        label="Enter text to analyze:",
        placeholder="Type your text here... (minimum 5 characters)",
        height=150,
        key="text_input"
    )

    if st.button("🔊 Read text aloud", key="read_aloud"):
        if user_text and user_text.strip():
            try:
                with st.spinner("🔊 Generating audio..."):
                    # Check cache first
                    text_hash = hash(user_text)
                    if text_hash in st.session_state.audio_cache:
                        audio_data = st.session_state.audio_cache[text_hash]
                    else:
                        # Generate new audio
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                        try:
                            audio_stream = loop.run_until_complete(generate_tts_audio(user_text))
                            audio_data = audio_stream.getvalue()
                            # Cache it
                            st.session_state.audio_cache[text_hash] = audio_data
                        finally:
                            loop.close()
                    
                    # Play the audio
                    st.audio(audio_data, format="audio/mp3")
                    st.success("✅ Audio generated!")
            except Exception as e:
                st.error(f"❌ Error generating audio: {str(e)}\n\nTry again or check your internet connection.")
        else:
            st.warning("Please enter text before using the voice reader.")

with col2:
    st.subheader("🎯 Analysis Options")
    
    analysis_type = st.radio(
        "Select analysis mode:",
        ["Single Text", "Multiple Texts"],
        key="analysis_type"
    )
    
    confidence_threshold = st.slider(
        "Confidence Threshold:",
        0.0, 1.0, 0.5,
        step=0.05,
        help="Filter results with confidence above this value"
    )

st.markdown("---")

# Analysis button and results
col1, col2, col3 = st.columns(3)

with col2:
    analyze_button = st.button(
        "🚀 Analyze Sentiment",
        use_container_width=True,
        key="analyze_btn"
    )

st.markdown("---")

if analyze_button:
    if not user_text or len(user_text.strip()) < 5:
        st.error("❌ Please enter at least 5 characters to analyze!")
    else:
        with st.spinner("🔄 Loading model and analyzing..."):
            try:
                # Load model
                sentiment_pipeline = load_sentiment_model()
                
                # Perform analysis
                start_time = time.time()
                result = sentiment_pipeline(user_text)
                end_time = time.time()
                
                # Extract results
                sentiment = result[0]['label']
                confidence = result[0]['score']
                processing_time = end_time - start_time
                
                # Add to history
                st.session_state.history.append({
                    'text': user_text,
                    'sentiment': sentiment,
                    'confidence': confidence,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                
                # Display results
                st.success("✅ Analysis Complete!")
                
                # Results in columns
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        "Sentiment",
                        f"{'😊 POSITIVE' if sentiment == 'POSITIVE' else '😞 NEGATIVE'}",
                        delta=None
                    )
                
                with col2:
                    st.metric(
                        "Confidence",
                        f"{confidence:.2%}",
                        delta=f"{(confidence-0.5)*100:.1f}%"
                    )
                
                with col3:
                    st.metric(
                        "Processing Time",
                        f"{processing_time:.3f}s",
                        delta=None
                    )
                
                # Detailed result box
                st.markdown("### 📊 Detailed Results")
                
                result_col1, result_col2 = st.columns(2)
                
                with result_col1:
                    # Color-coded sentiment badge
                    sentiment_color = "🟢" if sentiment == "POSITIVE" else "🔴"
                    st.markdown(f"""
                    **Input Text:**
                    > {user_text}
                    
                    **Sentiment Classification:** {sentiment_color} **{sentiment}**
                    """)
                
                with result_col2:
                    # Confidence visualization
                    fig = px.bar(
                        x=['Confidence'],
                        y=[confidence],
                        range_y=[0, 1],
                        labels={'y': 'Score', 'x': ''},
                        title="Confidence Score",
                        color=[confidence],
                        color_continuous_scale="RdYlGn",
                        text_auto='.2%'
                    )
                    fig.update_traces(textposition='outside')
                    st.plotly_chart(fig, use_container_width=True)
                
            except Exception as e:
                st.error(f"❌ Error during analysis: {str(e)}")

# History section
st.markdown("---")
st.subheader("📜 Analysis History")

if st.session_state.history:
    # Convert history to DataFrame
    history_df = pd.DataFrame(st.session_state.history)
    
    # Statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Analyses", len(history_df))
    
    with col2:
        positive_count = len(history_df[history_df['sentiment'] == 'POSITIVE'])
        st.metric("Positive", positive_count)
    
    with col3:
        negative_count = len(history_df[history_df['sentiment'] == 'NEGATIVE'])
        st.metric("Negative", negative_count)
    
    with col4:
        avg_confidence = history_df['confidence'].mean()
        st.metric("Avg Confidence", f"{avg_confidence:.2%}")
    
    st.markdown("---")
    
    # Sentiment distribution chart
    col1, col2 = st.columns(2)
    
    with col1:
        sentiment_counts = history_df['sentiment'].value_counts()
        fig1 = px.pie(
            values=sentiment_counts.values,
            names=sentiment_counts.index,
            title="Sentiment Distribution",
            color_discrete_map={'POSITIVE': '#00cc96', 'NEGATIVE': '#ff6b6b'}
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.scatter(
            history_df,
            x=range(len(history_df)),
            y='confidence',
            color='sentiment',
            title="Confidence Over Time",
            labels={'x': 'Analysis #', 'y': 'Confidence Score'},
            color_discrete_map={'POSITIVE': '#00cc96', 'NEGATIVE': '#ff6b6b'}
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Display history table
    st.markdown("### 📋 Detailed History")
    
    # Make table interactive
    display_df = history_df.copy()
    display_df['confidence'] = display_df['confidence'].apply(lambda x: f"{x:.2%}")
    display_df = display_df[['timestamp', 'text', 'sentiment', 'confidence']]
    display_df.columns = ['Timestamp', 'Text', 'Sentiment', 'Confidence']
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # Download history as CSV
    csv = display_df.to_csv(index=False)
    st.download_button(
        label="📥 Download History as CSV",
        data=csv,
        file_name=f"sentiment_analysis_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        use_container_width=True
    )
else:
    st.info("📭 No analysis history yet. Start by analyzing some text above!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8rem;'>
    <p>🤖 AI Sentiment Analyzer | Powered by Streamlit & Hugging Face Transformers</p>
    <p>© 2026 | Built with ❤️ for AI enthusiasts</p>
</div>
""", unsafe_allow_html=True)
