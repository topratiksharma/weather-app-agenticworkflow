from crewai_tools import ScrapeWebsiteTool

docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://www.aqi.in/in/dashboard/india/maharashtra/pune"
)
