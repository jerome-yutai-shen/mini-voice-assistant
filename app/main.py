# -*- coding: utf-8 -*-
"""
Created on Sep 18 08:45:35 2025

@author: Jerome Yutai Shen


"""
from fastapi import FastAPI
from app.api.routes import router


def create_app() -> FastAPI:
    app = FastAPI(title = "Mini Voice Assistant API", version = "0.1.0")
    app.include_router(router)
    return app


app = create_app()