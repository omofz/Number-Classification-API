# Number Classification API

This project implements a FastAPI-based API that classifies a given number by determining interesting mathematical properties and retrieving a fun fact from the [Numbers API](http://numbersapi.com/).

## Features

- **Number Analysis:**
  - Checks if the number is a **prime**.
  - Determines if the number is an **Armstrong number**.
  - Identifies the number's **parity** (odd or even) and returns combined properties.
  - Calculates the **sum of the digits**.
- **Fun Fact:**
  - Retrieves a math-related fun fact using the Numbers API.
- **CORS Support:**
  - Allows requests from any origin.
- **JSON Responses:**
  - All responses are returned in JSON format.
- **Error Handling:**
  - Provides a `400 Bad Request` error response when input validation fails.

## API Endpoint

### Classify Number

- **Endpoint:** `GET /api/classify-number`
- **Query Parameter:**
  - `number` (integer, required): The number to classify.

#### Successful Response (200 OK)

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
