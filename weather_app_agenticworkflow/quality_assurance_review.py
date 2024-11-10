from crewai import Task
from quality_assurance_agent import quality_assurance_agent

quality_assurance_review = Task(
    description=(
        "Review the response drafted by the air quality report agent for city: {city}. "
        "Ensure that the answer is comprehensive, accurate, and adheres to the "
        "high-quality standards expected for a news report.\n"
        "Verify that all parts such as source of the information of the city {city} "
        "have been addressed "
        "thoroughly, with a news reporting tone.\n"
        "Check for references and sources used to "
        " find the information, "
        "ensuring the response is well-supported from a news perspective and "
        "leaves no questions unanswered."
    ),
    expected_output=(
        "A final, detailed, and informative news article response "
        "ready to be published as a news report.\n"
        "Please maintain a very formal tone throughout. "
    ),
    agent=quality_assurance_agent
)
