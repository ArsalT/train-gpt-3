# THIS IS THE MAIN FILE TO ACCESS THE GPT-3 FROM OPENAI

import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

openai.api_key = '<<YOUR API KEY>>'

# HERE YOU SHOULD PROVIDE THE NAME OF THE MODEL 
def gpt3_completion(prompt, engine='davinci:ft-review-grower-2022-12-22-14-33-51', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=[' END'])
    text = response['choices'][0]['text'].strip()
    return text


if __name__ == '__main__':
    conversation = list()
    
    while True:
        user_input = input('USER: ') + '\n\nIntent:\n\n'
        # conversation.append('USER: %s' % user_input)
        # text_block = '\n'.join(conversation)
        # prompt = open_file('prompt_chat.txt').replace('<<BLOCK>>', text_block)
        # prompt = prompt + '\nJAX:'
        response = gpt3_completion(user_input)
        print('JAX:', response)
        # conversation.append('JAX: %s' % response)
        # print(conversation)