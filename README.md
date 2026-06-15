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

The application will open in your default browser at `http://localhost:8501`.

## 📦 Project Structure

```
streamlink-appl/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .streamlit/            # Streamlit configuration
```

## Notes

- The app uses `transformers` with a DistilBERT sentiment analysis model.
- Make sure `requirements.txt` is used by your deployment environment.
