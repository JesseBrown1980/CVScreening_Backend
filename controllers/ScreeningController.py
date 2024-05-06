from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
from flask import jsonify
import openai
import re
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
print(API_KEY)
openai.api_key = API_KEY
def process_cv(cv, job_description):
    """
    Function to generate response
    Args:
        resume (file): Uploaded CV pdf
        job_description (file): Uploaded job description pdf
    """
    try:
        cv_text = get_text_from_pdf(cv)
        job_text = get_text_from_pdf(job_description)
    except Exception as e:
        return jsonify({
            "error" : "Please provide exact CV or job description file"
        }), 400
    
    conversation = [
        {"role": "system", "content":"The assistant is an experienced recruiter who provides candid evaluations of candidates. It should not hesitate to point out mismatches between a CV and a job description. For identical CV and job description pairs, the assistant is expected to provide the same score every time to ensure consistency in evaluation."},
        {"role": "user", "content" : f"CV: {cv_text}, Job description: {job_text}"},
        {"role": "user", "content": """Please critically evaluate the candidate's CV in relation to the job description.:
         1. Please provide a evaluation of the candidate's CV. Assign a score from 1 to 10, where 1 indicates a poor fit and 10 indicates an exceptional fit. Result type must be Score : interger value
         2. Provide a detailed explanation with 2~4 sentences of the score, highlighting specific areas where the candidate excels or falls short in relation to the job requirements."""}
    ]
    try :
        response = chat_gpt(conversation)
    except Exception as e:
        print(e)
        return jsonify({
            'error' : "Please check OpenAI biling details",
        }), 400
        
    try:
        # Use regular expressions to extract the numerical score
        score_match = re.search(r'\b(score|rating)\s*:\s*(\d+)', response, re.I)
        score = score_match.group(2) if score_match else None

        # Extract the strengths and weaknesses description
        description_match = re.search(r'(Explanation):(.+)', response, re.I | re.DOTALL)
        description = description_match.group(2).strip() if description_match else None
        return jsonify({
            'score' : score,
            'decription' : description
        })
    except Exception as e:
        print(e)
        return jsonify({
            'error' : "server error",
        }), 400
    
def get_text_from_pdf(pdf):
    """
    function to get the pdf content

    Args:
        pdf (file): PDF file that user uploaded
    """
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def chat_gpt(conv):
    response = openai.ChatCompletion.create(
        model ="gpt-3.5-turbo",
        messages = conv
    )
    return response['choices'][0]['message']['content']

