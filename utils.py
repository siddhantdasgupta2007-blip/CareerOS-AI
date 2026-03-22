import anthropic

def get_career_response(prompt, api_key):
    client = anthropic.Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text
