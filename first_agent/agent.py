from google.adk.agents.llm_agent import LlmAgent


def get_capital_city(country: str) -> str:
    """ Return the capital city of a given country."""
    capitals = {
        "france": "Paris",
        "germany": "Berlin",
        "italy": "Rome",
        "spain": "Madrid",
        "india": "New Delhi",
        "usa": "Washington, D.C.",
    }

    return capitals.get(country.lower(), f"Capital city not found for {country}.")


root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='capital_agent',
    description='Answer questions about the capital cities of countries.',
    instruction=(
        "You provide country capital.\n"
        "when asked for a capital city, call get_capital_city(country) to retrieve the capital city of the specified country.\n"
        "Respond concisely."

    ),
    tools=[get_capital_city],
)
