import yaml

from openai import AsyncOpenAI

# from nonebot import get_plugin_config
# from .config import Config

OPENAI_ASYNC_CLIENT: dict[str, AsyncOpenAI] = {}
try:
    with open("configs/chatgpt-vision/keys.yaml") as f:
        for i in yaml.safe_load(f):
            OPENAI_ASYNC_CLIENT[i.get("model")] = AsyncOpenAI(
                api_key=i.get("key"),
                base_url=i.get("url"),
            )
except Exception:
    pass


async def chat(messages: list, model: str, times: int = 3, temperature: float = 0.65):
    """
    Chat with ChatGPT

    Parameters
    ----------
    message : list
        The message you want to send to ChatGPT
    model : str
        The model you want to use
    times : int
        The times you want to try
    """
    if model not in OPENAI_ASYNC_CLIENT:
        raise ValueError(f"The model {model} is not supported.")
    try:
        rsp = await OPENAI_ASYNC_CLIENT[model].chat.completions.create(
            messages=messages, model=model, temperature=temperature
        )
        if not rsp:
            raise ValueError("The Response is Null.")
        if not rsp.choices:
            raise ValueError("The Choice is Null.")
        return rsp
    except ValueError:
        pass
