# 🧠 Smart NLP Analyzer

## 📌 Project Overview

Smart NLP Analyzer is an AI-powered web application developed using Python, Gradio, and Hugging Face Inference API. It uses Natural Language Processing (NLP) techniques to analyze text and extract meaningful information.

The application combines three important NLP functionalities into a single interactive interface:

- **Text Summarization:** Generates concise summaries from lengthy text or articles.
- **Sentiment Analysis:** Identifies whether the given text expresses Positive, Negative, or Neutral sentiment, along with a confidence score.
- **Question Answering:** Provides relevant answers to user questions based on the context of the supplied text.

The application integrates pre-trained Transformer models from Hugging Face to perform these tasks efficiently.

## ✨ Features

- Automatic text summarization.
- Sentiment classification with confidence scores.
- Context-based question answering.
- Interactive web interface using Gradio.
- Integration with Hugging Face Inference API.
- Pre-trained Transformer model integration.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Web Interface:** Gradio
- **NLP Platform:** Hugging Face
- **API Integration:** Hugging Face Inference API
- **Libraries:** 
  - `os`
  - `gradio`
  - `huggingface_hub`

## 🤖 Pre-trained Models

| NLP Task | Model |
|---|---|
| Text Summarization | `facebook/bart-large-cnn` |
| Sentiment Analysis | `cardiffnlp/twitter-roberta-base-sentiment` |
| Question Answering | `deepset/roberta-base-squad2` |

## 📂 Project Structure

```text
smart-nlp-analyzer/
│
├── .vscode/
├── nlp.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Lakshanika1/smart-nlp-analyzer.git
```

### 2. Navigate to the Project Directory

```bash
cd smart-nlp-analyzer
```

### 3. Install Dependencies

```bash
pip install gradio huggingface_hub
```

Alternatively, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure Hugging Face API Token

1. Create an account on [Hugging Face](https://huggingface.co/).
2. Generate an access token from [Hugging Face Settings](https://huggingface.co/settings/tokens).
3. Set the token as an environment variable.

**Windows (Command Prompt):**

```cmd
set HF_TOKEN=your_huggingface_token
```

**Windows (PowerShell):**

```powershell
$env:HF_TOKEN="your_huggingface_token"
```

**Linux / macOS:**

```bash
export HF_TOKEN=your_huggingface_token
```

Replace `your_huggingface_token` with your actual access token.

### 5. Run the Application

```bash
python nlp.py
```

After execution, Gradio generates a local URL. Open the URL in your browser to access the application.

## 🚀 How to Use

1. Launch the Smart NLP Analyzer application.
2. Paste an article or text into the input textbox.
3. Enter a question related to the provided text (optional).
4. Submit the input for analysis.
5. View the three generated results:
   - **Sentiment:** Predicted sentiment and confidence score.
   - **Summary:** Concise summary of the input text.
   - **Answer:** Answer generated based on the provided context.

## 🎯 Applications

- News article analysis.
- Customer feedback analysis.
- Document summarization.
- Sentiment identification.
- Information extraction from textual content.

## 🔮 Future Enhancements

- Support for PDF and DOCX document uploads.
- Multilingual text analysis.
- Downloadable analysis reports.
- Improved data visualization.
- Enhanced user interface.

## 🎓 Learning Outcomes

- Gained practical knowledge of Natural Language Processing.
- Learned to integrate pre-trained Transformer models.
- Worked with Hugging Face Inference API.
- Implemented text summarization, sentiment analysis, and question answering.
- Developed an interactive AI application using Gradio.
- Learned to manage API credentials using environment variables.

## 📝 Conclusion

The Smart NLP Analyzer project demonstrates the practical application of Natural Language Processing by combining text summarization, sentiment analysis, and question answering into a single web application.

By integrating pre-trained models from Hugging Face with Gradio, the project provides an interactive platform for extracting meaningful insights from textual data.

This project enhanced my understanding of NLP concepts, AI model integration, API usage, and Python application development.

## 👩‍💻 Author

**Lakshanika A P**

B.E. Computer Science and Engineering

---

⭐ If you find this project useful, consider giving this repository a star!
