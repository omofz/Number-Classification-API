from fastapi import FastAPI, Query
import requests
from dotenv import load_dotenv

from utils import is_prime, is_armstrong, get_number_properties

load_dotenv()

app = FastAPI(title="Number Classification API", version="1.0")

@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="Enter a valid integer")):
    try:
        is_armstrong_number = is_armstrong(number)
        is_prime_number = is_prime(get_number_properties)
        digit_sum = sum(int(digit) for digit in str(number))
        properties = get_number_properties(number, is_armstrong_number)

        fun_fact_url = f"http://numbersapi.com/{number}/math"
        response = requests.get(fun_fact_url)
        fun_fact = response.text if response.status_code == 200 else "No fun fact available."

        return {
            "number": number,
            "is_prime": is_prime_number,
            "is_perfect": False,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }
    except Exception as e:
        return {"error": f"Something went wrong: {str{e}}"}