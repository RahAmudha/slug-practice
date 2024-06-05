Backend README ( subject to change NOT FINAL)

## Prerequisites
- Python 3.x
- pip (Python package manager)

- ## Installation
1. Clone the repository:
2. Navigate to the backend directory:
3. Create a virtual environment (optional but recommended):
4. Activate the virtual environment:
- For Unix/Linux:
  ```
  source venv/bin/activate
  ```
- For Windows:
  ```
  venv\Scripts\activate
  ```
  5. Install the required dependencies:
     pip install -r requirements.txt
  ## Configuration
1. Create a `.env` file in the backend directory.

2. Open the `.env` file and add the following environment variables:
   OPENAI_SLUG_PRACTICE_API_KEY=your-openai-api-key
   // REMEMBER TO EXPORT
Replace `your-openai-api-key` with your actual OpenAI API key.

## Running the Server
1. Make sure you are in the backend directory and the virtual environment is activated.

2. Run the following command to start the server:
   python app.py or python3 app.y
3. The server should now be running on `http://localhost:5000`.

## API Endpoints
- `/openai/generate` (POST): Generates practice problems based on what format 'mc/simple/tf'.

## Troubleshooting
- If you encounter any issues, make sure you have installed all the dependencies listed in the `requirements.txt` file.
- Ensure that your OpenAI API key is valid and correctly set in the `.env` file.
