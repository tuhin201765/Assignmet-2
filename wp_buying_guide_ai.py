import requests
from wp_funcs import wp_ai_content, wp_h2, wp_headers

with open('keywords.txt', 'r') as file:
    data=file.readlines()
    for line in data:
        first_title = f'{line} buying guide'.title()
        intro = wp_ai_content(f"write a introduction about{line}")
        question = wp_ai_content(f"write a one question about{line}")
        question_title =wp_h2(question).title()
        question_content =wp_ai_content(f'write paragraph about{question_title}')
        tips_title =wp_h2(f'how to choose {line}').title()
        tips_content = wp_ai_content(f'write a parahraph about {tips_title}')
        conclusion_title = wp_h2("Summary")
        conclution_content = wp_ai_content(f'write an advice about{line}')
        slug =line.replace(' ', '-').strip()

        content = f'{intro}{question_title}{question_content}{tips_title}{tips_content}{conclusion_title}{conclution_content}'

        data = {

          'title':first_title,
          'content':content,
          'categories': 17,
          'format' : 'standard',
          'status':'publish',
          'slug':slug

        }

        headers= wp_headers('nahid', 'iJBa neHb 24h2 btyS WSXM vf7v')
        post_url = 'https://birds.local/wp-json/wp/v2/posts'
        response=requests.post(post_url, data=data, headers=headers, verify=False)
        print(response)
