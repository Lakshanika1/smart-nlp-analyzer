import os
import gradio as gr
from huggingface_hub import InferenceClient
HF_TOKEN = os.environ.get("HF_TOKEN")
client = InferenceClient(api_key=HF_TOKEN)
def analyze(text, question):
    summary_response = client.summarization(
        text,
        model="facebook/bart-large-cnn"
    )
    if isinstance(summary_response, list):
        summary = summary_response[0]["summary_text"]
    else:
        summary = summary_response
    sentiment_response = client.text_classification(
        text,
        model="cardiffnlp/twitter-roberta-base-sentiment"
    )
    if isinstance(sentiment_response, list):
        sentiment = f"{sentiment_response[0]['label']} (Score: {round(sentiment_response[0]['score'],3)})"
    else:
        sentiment = str(sentiment_response)
    if question.strip() != "":
        qa_response = client.question_answering(
            question=question,
            context=text,
            model="deepset/roberta-base-squad2"
        )
        if isinstance(qa_response, list):
            answer = qa_response[0]["answer"]
        else:
            answer = qa_response.get("answer", "No answer found")
    else:
        answer = "No question provided"

    return sentiment, summary, answer
demo = gr.Interface(
    fn=analyze,
    inputs=[
        gr.Textbox(lines=10, label="Paste your article/text"),
        gr.Textbox(label="Ask a question from the text"),
    ],
    outputs=[
        gr.Textbox(label="Sentiment"),
        gr.Textbox(label="Summary"),
        gr.Textbox(label="Answer"),
    ],
    title="🧠 Smart NLP Analyzer",
)
demo.launch()