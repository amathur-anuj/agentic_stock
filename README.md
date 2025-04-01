# AgenticStock Crew

Welcome to the AgenticStock Crew project, powered by [crewAI](https://crewai.com). This project, named "agentic_stock" and versioned at 0.1.0, is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

This project requires Python >=3.10 and <3.13. It depends on the crewai[tools] package, version >=0.108.0 and <1.0.0.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
pip install crewai crewai[tools]
pip install lanchain_groq
pip install panel
pip install -e .
```

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
## Running the Application
To start the chat application, run the following command:

```bash
panel serve src/agentic_stock/main.py
```
This command initializes the agentic-stock Crew, assembling the agents and assigning them tasks as defined in your configuration. The project provides a chat interface for interacting with the crew. You can start a new analysis by typing a stock ticker, and restart the analysis by typing '/restart'.

### Customizing

**Add your `GROQ_API_KEY` into the `.env` file**

- Modify `src/agentic_stock/config/agents.yaml` to define your agents
- Modify `src/agentic_stock/config/tasks.yaml` to define your tasks
- Modify `src/agentic_stock/crew.py` to add your own logic, tools and specific args
- Modify `src/agentic_stock/main.py` to add custom inputs for your agents and tasks

## The Crew and Their Tasks

The AgenticStock Crew consists of several specialized agents, each designed to perform specific tasks related to stock analysis. Here's a breakdown of the agents and their responsibilities:

**Agents:**

*   **Researcher:** Conducts thorough stock research to uncover relevant insights and developments.
*   **Sentiment Analyst:** Analyzes public sentiment using news, social media, and forums to gauge market mood.
*   **Fundamental Analyst:** Assesses financial health, valuation metrics, and competitive positioning.
*   **Technical Analyst:** Analyzes historical price movements, trading volume, and chart patterns.
*   **Risk Manager:** Identifies and assesses risks associated with stock investment.
*   **Recommendation Engine:** Consolidates insights from all analyses to generate a final buy, hold, or sell recommendation.

**Tasks:**

*   **Research Task:** Conducts a thorough stock research.
*   **Sentiment Analysis Task:** Analyzes the sentiment surrounding the stock.
*   **Fundamental Analysis Task:** Evaluates the stock's financial health.
*   **Technical Analysis Task:** Analyzes the stock's historical price movements.
*   **Risk Assessment Task:** Identifies the key risks associated with investing in the stock.
*   **Final Recommendation Task:** Consolidates insights to generate a final buy, hold, or sell recommendation.
