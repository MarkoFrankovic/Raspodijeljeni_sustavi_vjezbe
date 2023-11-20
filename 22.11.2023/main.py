from fastapi import FastAPI
import httpx
from pydantic import BaseModel

app = FastAPI()


class CountryDetails(BaseModel):
    ime_drzave: str
    glavni_grad: str
    independent: bool
    status: str
    region: str


class CountryStore:
    stored_countries = {}


async def fetch_country_data(ime_drzave: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://restcountries.com/v3.1/name/{ime_drzave}/")
        return response.json()


@app.get("/async_country/{ime_drzave}", response_model=dict)
async def async_country(ime_drzave: str):
    country_data = await fetch_country_data(ime_drzave)
    country_details = CountryDetails(ime_drzave=ime_drzave, glavni_grad=country_data[0]["capital"][0], independent=country_data[0]["independent"], status=country_data[0]["status"][0], region=country_data[0]["region"][0])
    CountryStore.stored_countries[ime_drzave] = country_details
    return {"country_data": country_data, "stored_countries": CountryStore.stored_countries}


@app.get("/get_countries", response_model=dict)
async def get_country_store():
    return {"stored_countries": CountryStore.stored_countries}


@app.delete("/delete_countries/{ime_drzave}", response_model=dict)
async def get_country_store(ime_drzave):
    Removed_Country = CountryStore.stored_countries.pop[ime_drzave] 
    return {"Removed_country": Removed_Country}

