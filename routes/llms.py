from fastapi import APIRouter, HTTPException
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


gpt2_router = APIRouter()


# This function generates text using GPT-2
def generate_text_for_gpt2(prompt: str):
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")

    # inp = "The dog is a good animal."
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(
        input_ids=input_ids, do_sample=True, temperature=0.7, max_length=600
    )
    Generated_text = tokenizer.batch_decode(outputs[0])
    
    return "".join(Generated_text)


def chunk_text(text, max_length=600):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

def translate_text_from_english_to_french(text: str):
    try:
        pipe_t = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
        chunks = chunk_text(text)
        translated_chunks = [pipe_t(chunk)[0]['translation_text'] for chunk in chunks]
        return " ".join(translated_chunks)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cannot translate text: {e}")

# This function generates text using GPT-2 model
@gpt2_router.post("/gpt2/translate", tags=["Helsinki-NLP/opus-mt-en-fr"])
async def translate_text(text: str) -> dict:
    try:
        translated_text = translate_text_from_english_to_french(text)
        return {"text_translated": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cannot translate text \n{e}")
    

# This function generates text using GPT-2 model
@gpt2_router.post("/gpt2/generate_text", tags=["gpt2"])
async def generate_text(text: str) -> dict:
    try:
        generated_text = generate_text_for_gpt2(text)
        return {"text": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cannot generate text: {e}")
