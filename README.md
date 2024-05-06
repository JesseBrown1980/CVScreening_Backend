## CV Checker: An AI Driven CV Screening Tool

## About

CV Checker is an efficient recruitment assistant powered by OpenAI's GPT-3.5. The tool allows recruiters to upload  CV along with a job description.  As a result, the tool will provide an evaluation of resume against the provided job description and give insights into the suitability of the candidate for the role.

## Requirements
- Flask
- OpenAI Python Client

## Setup

1. Clone the repository.
```
https://github.com/JesseBrown1980/CVScreening_Backend.git
```
2. Change directory to the cloned repository.
```
cd CVScreening_Backend
```
3. Install the required packages.
```
pip install -r requirements.txt
```
4. Update the OpenAI API key in the openai.api_key = "OPEN AI KEY" line with your own key.
5. Run the application.
```
python app.py
```

## Limitations

1. As the tool uses the OpenAI API, you will need a valid API key which might have associated costs.
2. The current version supports CV in PDF format only.

## Contributing

Feel free to submit pull requests, raise issues, or give feedback. Your contributions are welcome!