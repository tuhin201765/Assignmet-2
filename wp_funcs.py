def wp_ai_content(text):
    """
    This code will create content from api and make gutenburg paragraph code.

    """
    import os
    import openai
    from dotenv import load_dotenv
    load_dotenv()

    openai.api_key = os.getenv("api_key")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    code = response.get('choices')[0].get('text').strip()
    para_code = f'<!-- wp:paragraph --><p>{code}</p><!-- /wp:paragraph -->'
    return para_code


def wp_h2(text):
    """
    This code will make gutenburg heading two code.
    """
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code


def wp_headers(username, password):
    """
    This code will make wp headers.
    """
    import base64
    credintial = f"{username}:{password}"
    token = base64.b64encode(credintial.encode())
    code = {'Authorization': f'Basic {token.decode("utf-8")}'}
    return code