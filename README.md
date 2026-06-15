# 🤖 AI Sentiment Analyzer

A modern, interactive web application for real-time sentiment analysis using pre-trained AI models. Built with **Streamlit** and powered by **Hugging Face Transformers**.

## 🌟 Features

- ✅ **Real-time Sentiment Analysis** - Classify text as Positive or Negative
- 📊 **Interactive Visualizations** - Beautiful charts and metrics using Plotly
- 💾 **Analysis History** - Track all your analyses with timestamps
- 📈 **Statistics Dashboard** - View sentiment distribution and confidence trends
- 📥 **Export Results** - Download analysis history as CSV
- ⚡ **Fast Processing** - Lightweight DistilBERT model for quick responses
- 🎨 **Modern UI** - Clean, intuitive interface with custom styling

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/muhammadJawadktk/streamlink-appl.git
cd streamlink-appl
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📦 Project Structure

```
streamlink-appl/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🤖 AI Model Details

- **Model Name**: DistilBERT (Fine-tuned on SST-2)
- **Task**: Binary Sentiment Classification (Positive/Negative)
- **Type**: Pre-trained Transformer
- **Library**: Hugging Face Transformers
- **Advantages**: 
  - Fast inference
  - Lightweight (~268MB)
  - 97% accuracy on SST-2 benchmark
  - Works offline after first download

## 💻 Technology Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| Streamlit | 1.31.1 | Web framework |
| Transformers | 4.36.2 | Pre-trained models |
| PyTorch | 2.1.2 | Deep learning backend |
| Plotly | 5.18.0 | Interactive visualizations |
| Pandas | 2.1.3 | Data manipulation |
| Numpy | 1.26.3 | Numerical computing |

## 📊 How It Works

1. **Input Processing**: User enters text in the text area
2. **Model Inference**: Text is sent to the DistilBERT model
3. **Sentiment Classification**: Model predicts sentiment (Positive/Negative)
4. **Confidence Scoring**: Returns confidence score (0-1)
5. **Visualization**: Results displayed with interactive charts
6. **History Tracking**: Analysis saved to session history

## 🎯 Use Cases

- 📱 **Social Media Monitoring** - Analyze sentiment of tweets or comments
- 💬 **Customer Feedback Analysis** - Evaluate customer reviews and feedback
- 📰 **News Sentiment Analysis** - Determine tone of articles or headlines
- 🎓 **Educational Tool** - Learn about NLP and AI models
- 💼 **Business Intelligence** - Track brand sentiment over time

## 📈 Features in Detail

### 1. Single Text Analysis
- Enter any text and get instant sentiment classification
- View confidence scores and processing time
- Color-coded sentiment indicators (Green for Positive, Red for Negative)

### 2. Analysis History
- Automatically tracks all analyses in the session
- View statistics: total analyses, positive/negative counts
- Sentiment distribution pie chart
- Confidence trend line chart

### 3. Data Export
- Download complete analysis history as CSV
- Includes timestamps, original text, sentiment, and confidence
- Ready for further analysis in Excel or other tools

### 4. Interactive Dashboard
- Real-time metric cards showing key statistics
- Plotly charts for interactive data exploration
- Responsive design for mobile and desktop

## 🔧 Configuration

You can customize the application by modifying these variables in `app.py`:

```python
# Confidence threshold (default: 0.5)
confidence_threshold = st.slider("Confidence Threshold:", 0.0, 1.0, 0.5)

# Model selection (can be changed to other Hugging Face models)
# Current: distilbert-base-uncased-finetuned-sst-2-english
```

## 📝 Example Usage

1. Open the application
2. Enter text: "I love this product, it works amazing!"
3. Click "🚀 Analyze Sentiment"
4. View results: Positive sentiment with 99% confidence
5. Check history to see all previous analyses

## 🌐 Deployment

### Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository and `app.py`
6. Click "Deploy"

### Deploy on Hugging Face Spaces

1. Create a new Space on Hugging Face
2. Upload your files
3. Add `streamlit run app.py` as the startup command
4. Your app will be live!

## ⚠️ Limitations

- Model works best with English text
- Maximum input length: ~512 tokens
- Binary classification (Positive/Negative only)
- Sentiment scores can vary based on context

## 🚀 Future Enhancements

- [ ] Multi-language support
- [ ] Aspect-based sentiment analysis
- [ ] Emotion detection (beyond positive/negative)
- [ ] Batch processing for multiple texts
- [ ] Custom model fine-tuning
- [ ] API endpoint for external integrations
- [ ] Database for persistent history storage

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Muhammad Jawad**
- GitHub: [@muhammadJawadktk](https://github.com/muhammadJawadktk)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - Amazing web framework
- [Hugging Face](https://huggingface.co/) - Pre-trained models
- [Plotly](https://plotly.com/) - Interactive visualizations
- [PyTorch](https://pytorch.org/) - Deep learning framework

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Streamlit documentation](https://docs.streamlit.io/)
2. Visit [Hugging Face Hub](https://huggingface.co/)
3. Open an issue on GitHub

## 📊 Metrics & Performance

- **Model Size**: ~268 MB
- **Inference Time**: ~0.1-0.3 seconds per text
- **Accuracy**: ~97% on SST-2 benchmark
- **Memory Usage**: ~1-2 GB (with model loaded)
- **Supported Languages**: English (primarily)

---

**Made with ❤️ for the AI community**

Happy Analyzing! 🚀
