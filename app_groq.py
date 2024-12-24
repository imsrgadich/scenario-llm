import streamlit as st
import pandas as pd
import altair as alt
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Check API Key
if not groq_api_key:
    st.error("Groq API key not found. Add it to your .env file.")
else:
    llm=ChatGroq(
    model="llama3-70b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=groq_api_key,
    # other params...
)
    #llm = ChatGroq(api_key=groq_api_key)

    # LangChain Prompts
    question_prompt = PromptTemplate(
        input_variables=["question", "data"],
        template="Analyze the sales data: {data}. Answer this: {question}"
    )
    scenario_prompt = PromptTemplate(
        input_variables=["scenario", "data"],
        template=(
            "Given the sales data: {data}, analyze the scenario: {scenario}. "
            "Respond with a concise description and show data visualizations "
            "for the impact (preferably bar charts or line charts). Avoid tables."
        )
    )
    question_chain = LLMChain(llm=llm, prompt=question_prompt)
    scenario_chain = LLMChain(llm=llm, prompt=scenario_prompt)

    # Streamlit UI
    st.title("Sales Data Analysis and Scenario Modeling")

    # File Upload
    uploaded_file = st.file_uploader("Upload Sales Data (CSV)", type=["csv"])
    if uploaded_file:
        sales_data = pd.read_csv(uploaded_file)
        st.subheader("Uploaded Sales Data")
        st.write(sales_data)

        # Q&A Section
        st.subheader("Ask a Question")
        question = st.text_input("Enter a question", "What is the best-performing region?")
        if st.button("Answer"):
            data_str = sales_data.to_string(index=False)
            answer = question_chain.run({"question": question, "data": data_str})
            st.write("**Answer:**", answer)

        # Scenario Analysis
        st.subheader("Scenario Analysis")
        scenario = st.text_input("Enter a scenario", "Increase sales by 20% in Norteast region.")
        if st.button("Analyze Scenario"):
            data_str = sales_data.to_string(index=False)
            scenario_response = scenario_chain.run({"scenario": scenario, "data": data_str})
            st.write("**Scenario Analysis:**", scenario_response)

            # Example: Visualize Change
            if "increase" in scenario.lower():
                region, percentage = "Northeast", 20
                modified_data = sales_data.copy()
                modified_data.loc[modified_data['REGION'] == region, 'UNIT_SALES'] *= 1 + percentage / 100
                chart = alt.Chart(modified_data).mark_bar().encode(
                    x='REGION',
                    y='UNIT_SALES',
                    color='REGION'
                ).properties(title="Sales After Scenario")
                st.altair_chart(chart, use_container_width=True)
