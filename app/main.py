from fastapi import FastAPI, Query, Request
import httpx
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

from .utils import is_prime, is_armstrong, get_number_properties

load_dotenv()

app = FastAPI(title="Number Classification API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"number": request.query_params.get("number", ""), "error": True}
    )

@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="Enter a valid integer")):
    try:
        is_armstrong_number = is_armstrong(number)
        is_prime_number = is_prime(number)
        digit_sum = sum(int(digit) for digit in str(number))
        properties = await get_number_properties(number, is_armstrong_number)

        fun_fact_url = f"http://numbersapi.com/{number}/math"
        async with httpx.AsyncClient() as client:
            response = await client.get(fun_fact_url)
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
        return JSONResponse(status_code=500, content={"error": f"Something went wrong: {str(e)}"})
