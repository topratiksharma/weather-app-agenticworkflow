import os
from crewai import LLM

def getLLM():
    return LLM(
        model="azure/modelname",
        api_version="version",
        api_key="key",
        base_url="base-url"
    )
