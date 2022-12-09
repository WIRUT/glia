import copy
import html
import random
from collections import deque
from fastapi import FastAPI
from pydantic import BaseModel

# Assumptions:
# 1. We're getting jumbled strings. There can only be one jumbled string for each input word.
# 2. We're not wanting to save all calls, so we're going to set a limit, disregarding any older calls.
# 3. When calling audit_api, does not include the call to itself in the list returned
# 4. If given a sentence, will take the first word and scramble. Disregarding the remaining words.
# 5. Words are defined as characters between two spaces of the English language.
# 7. Remove all capitalizations.


app = FastAPI()
capacity = 10
cache = deque()


class Key(BaseModel):
    key: str


@app.post("/jumble-api")
async def jumble_str(data: Key):
    if not data:
        return None

    str_input = _clean_input(data.key)
    jumbled_str = _scramble_word(str_input)
    payload = _build_payload(str_input, jumbled_str)
    _update_cache('jumble-api', payload)
    return jumbled_str


@app.get("/audit-api")
async def audit_api():
    old_cache = copy.deepcopy(cache)
    _update_cache('audit-api', list(old_cache))
    return list(old_cache)


def _update_cache(api_call, payload):
    cache.appendleft({'api_called': api_call, 'payload': payload})
    while len(cache) > capacity:
        cache.pop()


def _clean_input(data):
    # Sanitizes for html
    word = data.split()
    output = html.escape(word[0])
    return output.lower()


def _scramble_word(str_input):
    scrambled = ''.join(random.sample(str_input, len(str_input)))
    return scrambled


def _build_payload(str_input, jumbled_str):
    payload = {'src_str': str_input, 'jumbled_str': jumbled_str}
    return payload
