from __future__ import annotations


def print_conversation(msgs):
    """
    Print the conversation in a readable format.

    Parameters:
    -----------
    msg: list
        The conversation messages to print.
    """
    from wasabi import msg

    for turn in msgs:
        icon = '🤖' if turn['role'] == 'assistant' else (
            '⚙️' if turn['role'] == 'system' else '👤'
        )
        msg.divider(icon)
        print(turn['content'])

def buf_img(
    image: Image.Image
    ) -> bytes:
    import io
    img_buf = io.BytesIO()
    image.save(img_buf, format='PNG')
    img_buf.seek(0)
    return img_buf.read()

def open_image(
    b64_str: str
    ) -> Image.Image:
    import base64
    import io
    from PIL import Image
        
    img_data = base64.b64decode(b64_str)
    image = Image.open(io.BytesIO(img_data))
    return image
    
def res_to_image(
    response: dict
    ) -> Image.Image:
    b64_str = response.data[0].b64_json
    image = open_image(b64_str)
    return image