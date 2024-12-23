# Sales Data Analysis with Scenario Modeling and Visualization
This project allows users to upload historical sales data, ask questions, and perform scenario analysis using LangChain and ChatGroq for fast inference. The results are visualized using Altair, with a focus on interactive plots rather than tables.

## Features
- *Upload Sales Data*: Upload CSV files containing historical sales data.
- *Q&A on Sales Data*: Ask questions about the sales data and get concise answers.
- *Scenario Analysis*: Analyze different scenarios (e.g., sales increase) and view visualized results through bar charts.
- *Visualization*: Automatically generate visualizations (charts) for scenario analysis results.

## Requirements
```
llama-cpp-python
streamlit
langchain
transformers
sentence-transformers
fastapi
pydantic
matplotlib
pandas
langchain-community
langchain-core
langchain-groq
python-dotenv
```

## Installation
1. *Clone the repository*:

```bash
git clone https://github.com/yourusername/sales-analysis.git
cd sales-analysis
```

2. *Install dependencies*:

```bash
pip install -r requirements.txt
```

3. *Create a .env file in the root directory and add your Groq API key*:

```plaintext
GROQ_API_KEY=your_groq_api_key
```

## Running the Application
*To run the application locally*:

1. Make sure the .env file is properly set up with the Groq API key.

2. Launch the Streamlit app:

```bash
streamlit run app.py
```

3. Open the application in your browser at http://localhost:8501.

## How It Works
1. *Upload CSV File*: Users can upload CSV files containing historical sales data, which will be displayed in the app.

2. *Ask Questions*: Users can enter questions related to the sales data, and the application will return answers using LangChain and ChatGroq for inference.

3. *Scenario Analysis*: Users can input different scenarios (e.g., a 20% increase in sales for a region) and visualize the results through a bar chart using Altair.

4. *Visualization*: Instead of showing tables, scenario analysis results are visualized through interactive plots to make the insights more accessible and engaging.

## Example Scenarios
- "What was the best-performing region last quarter?"
- "What if sales increase by 20% in the North region?"


## License
This project is licensed under the MIT License - see the LICENSE file for details.