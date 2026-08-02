from ollama import chat

def evaluate_project(proposal_text):

    prompt = f"""
You are an expert engineering project evaluator.

Evaluate this final year project proposal.

Provide:

1. Project Summary
2. Innovation Score (/10)
3. Technical Feasibility
4. Technology Stack
5. Strengths
6. Weaknesses
7. Future Scope
8. Overall Rating (/10)

Proposal:

{proposal_text}
"""

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]