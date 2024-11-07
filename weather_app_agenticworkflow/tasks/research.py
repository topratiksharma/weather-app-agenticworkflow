from crewai import Agent, Task, Crew

research_task = Task(
    description=(
        "Quickly do a thourough research for the following {city}:\n"

		"Make sure to use everything you know "
        "to provide the best and comprehensive news article as possible."
		"You must strive to provide a complete "
        "and accurate response with all references"
    ),
    expected_output=(
	    "A detailed, informative response to the "
        "customer's inquiry that addresses "
        "all aspects of their question.\n"
        "The response should include references "
        "to everything you used to find the answer, "
        "including external data or solutions. "
        "Ensure the answer is complete, "
		"leaving no questions unanswered, and maintain a helpful and friendly "
		"tone throughout."
    ),
	tools=[docs_scrape_tool],
    agent=air_quality_report_agent,
)