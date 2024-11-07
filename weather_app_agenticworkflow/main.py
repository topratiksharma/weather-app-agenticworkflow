from .agents.air_quality_reporter import air_quality_report_agent
from .agents.quality_assurance import quality_assurance_agent
from .tasks.research import research_task
from .tasks.quality_assurance import quality_assurance_review

# Warning control
# from google.colab import userdata
from crewai import Crew
import os
from IPython.display import Markdown

import warnings
warnings.filterwarnings('ignore')


OPENAI_API_KEY = "4"
openai_api_key = OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'


def init():
    crew = Crew(
        agents=[air_quality_report_agent, quality_assurance_agent],
        tasks=[research_task, quality_assurance_review],
        verbose=2,
        memory=True
    )

    inputs = {
        "city": "Pune"
    }
    result = crew.kickoff(inputs=inputs)

    Markdown(result)


if __name__ == '__main__':
    init()
