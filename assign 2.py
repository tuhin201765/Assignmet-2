import openai
import base64
import requests
openai.api_key = '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'


def heading_two(text):
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code


def oai_ans(promt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=promt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response.get('choices')[0].get('text')
    return output


with open('keywords.txt','r') as file:
    data = file.readlines()
    for keyword in data:
        first_title = f'{keyword} buying guide.'
        intro = oai_ans(f'Write a introduction about {keyword}')
        question = oai_ans(f'Write a question about {keyword}')
        question_title = heading_two(question)
        question_answer = oai_ans(f'Write a paragraph about {question_title}')
        question_two = heading_two(f'Why {keyword} is important?')
        question_two_answer = oai_ans(f'Write a paragraph about {question_two}')
        question_three = heading_two(f'How to choose best {keyword}')
        question_three_answer = oai_ans(f'Write 50 words about {question_three}')
        question_four = heading_two(f'What features should be considered while buying {keyword}')
        answer_four = oai_ans(f'Write 200 words about {question_four}')
        slug = keyword.replace(' ','-').strip()
        content = f'{intro}{question_title}{question_answer}{question_two}{question_two_answer}{question_three}{question_three_answer}{question_four}{answer_four}'

        data = {
            'title': first_title,
            'content': content,
            'slug' : slug
        }


        user = 'Mjujahidultuhin'
        password = 'oJDN m7RS lkmr PSdY 6g9A DDQS'
        credential = f'{user}:{password}'
        token = base64.b64encode(credential.encode())
        headers = {"Authorization": f'Basic {token.decode("utf-8")}'}
        api_url = 'https://mysite.local/wp-json/wp/v2/posts'
        r = requests.post(api_url, data=data, headers=headers, verify=False)

        print(r)












