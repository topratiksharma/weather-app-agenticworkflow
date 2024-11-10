from crewai import Crew
from IPython.display import Markdown
import warnings

from air_quality_reporter import air_quality_report_agent
from quality_assurance_agent import quality_assurance_agent
from research import research_task
from quality_assurance_review import quality_assurance_review

warnings.filterwarnings('ignore')

def init():
    crew = Crew(
        agents=[air_quality_report_agent, quality_assurance_agent],
        tasks=[research_task, quality_assurance_review],
        verbose=True
    )
    inputs = {"city": "Pune"}
    result = crew.kickoff(inputs=inputs)
    print(result)
    Markdown(result)

if __name__ == '__main__':
    init()
