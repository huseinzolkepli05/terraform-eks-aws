from fastapi import FastAPI, Request, Query
from fastapi import HTTPException
from pydantic import BaseModel
import malaya


class FormTranslate(BaseModel):
    text: str
    to_lang: str = 'ms'


model = malaya.translation.huggingface(use_ctranslate2=True)

app = FastAPI()


@app.get('/')
async def get():
    return 'hello'


@app.post('/translate')
async def translate(
    form: FormTranslate,
    request: Request = None,
    apikey: str = Query(None, description='API key, required.'),
):
    form = form.dict()
    if form['to_lang'] not in {'en', 'ms'}:
        raise HTTPException(
            status_code=500,
            detail='`to_lang` only accept `en` or `ms`.',
        )
    r = model.generate(
        [form['text']],
        to_lang=form['to_lang'],
        max_input_length=2048,
        max_decoding_length=2048,
        disable_unk=True,
    )
    return {'result': r[0]}
