import streamlit as st
import pandas as pd
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize LlamaCpp
model_path = "/Users/srikanth.gadicherla/git_repos/personal_projects/scenario-llm/models/llama-2-13b-chat.Q2_K.gguf"
llm = LlamaCpp(model_path=model_path)

# Define LangChain components
scenario_prompt = PromptTemplate(
    input_variables=["scenario_description"],
    template=(
        """
        [INST] <<SYS>>
        You are an expert in sensitivity and scenario modeling for a paperboard manufacturing company. You are helpful, respectful and honest assistant. 
        Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, 
        toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. 
        If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. 
        If you don't know the answer to a question, please don't share false information.
        Do not include any explanations or apologies in your responses and only respond to the task above.
        Use bullets points to answer.

        <</SYS>>
         Analyze the following scenario and provide insights: {scenario_description}[/INST]
        """
    )
)
scenario_chain = LLMChain(llm=llm, prompt=scenario_prompt)

# Streamlit UI
st.title("Scenario and Sensitivity Modeling with GenAI")

# Input: Scenario Description
scenario_description = st.text_area(
    "Enter the description of the scenario you want to model:",
    "What if we increase or decrease the production capacity?"
)

# Input: Sensitivity Variable and Changes
variable = st.text_input("Enter the variable to analyze (e.g., 'capacity', 'demand', 'forecast')", "capacity")
changes = st.text_input(
    "Enter a comma-separated list of changes (e.g., '10, 20, -10')",
    "10, 20, -10"
)
changes = [float(change.strip()) for change in changes.split(",")]

# Button to Run Analysis
if st.button("Run Analysis"):
    # Perform Sensitivity Analysis
    results = []
    for change in changes:
        modified_scenario = scenario_description + f"Use the {change} for the {variable} variable"
        result = scenario_chain.run({"scenario_description": modified_scenario})
        results.append({"Change": change, "Output": result})

    # Convert results to DataFrame
    results_df = pd.DataFrame(results)

    # Display Results
    st.subheader("Results")
    st.dataframe(results_df)

    # Plot Results
    st.subheader("Visualization")
    st.line_chart(data=results_df.set_index("Change"))
