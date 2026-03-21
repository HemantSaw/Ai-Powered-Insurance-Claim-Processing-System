from flask import Blueprint, jsonify
import os, json
from dotenv import load_dotenv
import httpx, requests
from langchain_openai import AzureChatOpenAI
from db import db
from langchain.agents import create_agent
load_dotenv()
client = httpx.Client(verify=False)
llm = AzureChatOpenAI(
    model = "gpt-4",
    azure_endpoint = os.getenv("AZURE_OPENAI_GPT_4_ENDPOINT"),
    openai_api_version = os.getenv("AZURE_OPENAI_GPT_4_VERSION"),
    deployment_name = os.getenv("AZURE_OPENAI_GPT_4_DEPLOYMENT_NAME"),
    openai_api_key = os.getenv("AZURE_OPENAI_GPT_4_API_KEY"),
    openai_api_type = "azure",
    temperature = 0.1,
    max_tokens = 1000,
    http_client = client,
)

class Agent():

    def text_extraction_llm(combined_text):
        system_prompt = f"""
        You are a medical insurance document extraction system.

        Extract the following fields and return ONLY valid JSON.
        If a field is missing, use null.

        Fields:
        - patient_name
        - hospital_name
        - admission_date
        - discharge_date
        - diagnosis
        - total_bill_amount

        TEXT:
        {combined_text}
        """


        text = llm.invoke(system_prompt)
        return text
    
    def policy_reason_llm(policy_text, claim_form_data, claim_extracted_data, claim_evaluation_result):
        prompt = f"""
            You are an insurance claim decision agent.

            Use the POLICY to decide coverage.

            POLICY:
            {policy_text}

            CLAIM FORM DATA:
            {claim_form_data}

            EXTRACTED MEDICAL DATA:
            {claim_extracted_data}

            RULE EVALUATION:
            {claim_evaluation_result}

            TASK:
            1. Decide if the claim is covered by the policy.
            2. Cite relevant policy clauses (if any).
            3. Recommend next action.

            Return ONLY valid JSON in this format:
            {{
            "coverage_decision": "COVERED | NOT_COVERED | UNCLEAR",
            "policy_references": [],
            "reasoning": "",
            "recommended_action": "SEND_TO_HUMAN | REQUEST_DOCS | REJECT"
            }}

            also remove the ```json or ``` from the response.
            """

        response = llm.invoke(prompt)
        print("...ll response", repr(response.content))
        return json.loads(response.content)