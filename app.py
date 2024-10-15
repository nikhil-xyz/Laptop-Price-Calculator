import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run

from typing import Optional

from laptop_project.constants import APP_HOST, APP_PORT
from laptop_project.pipeline.prediction_pipeline import LaptopData, LaptopRegressor

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.Brand = None
        self.Screen_Size = None
        self.CPU_Model = None
        self.Ram = None
        self.Graphics = None
        self.Disk_Size = None
    

    async def get_laptop_data(self):
        form = await self.request.form()
        self.Brand = form.get("Brand")
        self.Screen_Size = form.get("Screen_Size")
        self.CPU_Model = form.get("CPU_Model")
        self.Ram = form.get("Ram")
        self.Graphics = form.get("Graphics")
        self.Disk_Size = form.get("Disk_Size")
        

@app.get("/", tags=["authentication"])
async def index(request: Request):

    return templates.TemplateResponse(
            "laptop.html",{"request": request, "context": "Rendering"})


@app.get("/train")
async def trainRouteClient():
    try:
        os.system("python laptop_project\pipeline\model_pusher_pipeline.py")
        
        #   For executing dvc pipeline
        #   os.system("dvc repro")

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/")
async def predictRouteClient(request: Request):
    try:
        form = DataForm(request)
        await form.get_laptop_data()
        
        laptop_data = LaptopData(
                                Brand= form.Brand,
                                Screen_Size = form.Screen_Size,
                                CPU_Model = form.CPU_Model,
                                Ram = form.Ram,
                                Graphics= form.Graphics,
                                Disk_Size = form.Disk_Size
                                )
        
        laptop_df = laptop_data.get_laptop_input_data_frame()

        model_predictor = LaptopRegressor()

        value = model_predictor.predict(dataframe=laptop_df)[0]

        return templates.TemplateResponse(
            "laptop.html",
            {"request": request, "context": value},
        )
        
    except Exception as e:
        return {"status": False, "error": f"{e}"}


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)