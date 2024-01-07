from openai.types.chat import ChatCompletion


def serialize_chat_completion(chat_completion: ChatCompletion):
    return {
        "id": chat_completion.id,
        "object": chat_completion.object,
        "created": chat_completion.created,
        "model": chat_completion.model,
        "choices": [
            {
                "index": choice.index,
                "message": {
                    "role": choice.message.role,
                    "content": choice.message.content
                }
            } for choice in chat_completion.choices
        ]
    }
