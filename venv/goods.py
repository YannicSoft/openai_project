from openai import OpenAI
import os

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)
COMPLETION_MODEL = "text-davinci-003"

# 1.要求gpt写几个亚马逊上可读的标题
# 2.写5个卖点
prompt = """
Consideration product : 工厂现货PVC充气青蛙夜市地摊热卖充气玩具发光蛙儿童水上玩具

1. Compose human readable product title used on Amazon in english within 20 words.
2. Write 5 selling points for the products in Amazon.
3. Evaluate a price range for this product in U.S.

Output the result in json format with three properties called title, selling_points and price_range
"""

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    generated_text = response.choices[0].message.content
    return generated_text

if __name__ == '__main__':
    print(get_response(prompt))
