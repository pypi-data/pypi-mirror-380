from syngular_ai import (
    entrypoint, dev_listen, StatusUpdate, MarkdownMessage, OptionFeedback, TextInput, FileInput, ThumbsFeedback, TextFeedback
)

@entrypoint('@helloworld')
def helloworld(prompt: str):
    for char in 'hello':
        yield MarkdownMessage(
            content=f'{char}',
            feedback=[ThumbsFeedback(name='ratings')]
        )

@entrypoint(
    '@syngular/analyse', 
    inputs=[
        TextInput(name='url', placeholder='Enter company URL'),
        FileInput(name='file')
    ]
)
def analyse(prompt: str, inputs: list):
    # Process the inputs
    url = inputs[0]  # TextInput
    file_content = inputs[1].get_file_content()  # FileInput
    print(url, file_content)
    
    # Show status update
    yield StatusUpdate(
        icon='info', 
        text='Starting the process...'
    )
    
    # Stream response with feedback options
    for char in 'processing':
        yield MarkdownMessage(
            content=f'{char}',
            feedback=[
                OptionFeedback(
                    name='multioption', 
                    options=['Complete', 'Relevant'],
                    allow_multiple=True
                ),
                ThumbsFeedback(name='ratings'),
                TextFeedback(name='Leave a comment')
            ]
        )

# TODO: Fix async entrypoints
# @async_entrypoint('@sales/two')
# async def two(prompt: str):
#     for x in 'two':
#         raise Exception('This is an error')


# @async_entrypoint('@syngular/async-agent')
# async def three(prompt: str):
#     for x in 'two':
#         yield MarkdownMessage(content=f'{x}')


# listen(api_key='sk-proj-1234567890', port=8080, host='0.0.0.0')
dev_listen('010105f0-8133-4061-92e6-28ecf9ee85cd', api_url='ws://localhost:8000')
# dev_listen(2)
