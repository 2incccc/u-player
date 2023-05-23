import openai
openai.api_key = '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'
response = openai.Image.create(
    prompt="A fluffy white cat with blue eyes sitting in a basket of flowers, looking up adorably at the camera",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
