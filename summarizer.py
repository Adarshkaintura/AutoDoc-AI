from transformers import pipeline
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

summarizer = pipeline("summarization", model="t5-small")

def abstractive_summary(text):
    sentences = sent_tokenize(text)
    
    max_chunk_size = 5000
    summaries = []
    
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) > max_chunk_size:
            if current_chunk.strip():
                summary = summarizer(current_chunk, max_length=150, min_length=40, do_sample=False)
                summaries.append(summary[0]['summary_text'])
            current_chunk = sentence
        else:
            current_chunk += " " + sentence
    
    # Summarize 
    if current_chunk.strip():
        summary = summarizer(current_chunk, max_length=150, min_length=40, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    
    final_summary = " ".join(summaries)
    return final_summary
    
    # if len(summaries) > 1:
    #     final_summary = summarizer(final_summary, max_length=200, min_length=50, do_sample=False)[0]['summary_text']
    
    # return final_summary