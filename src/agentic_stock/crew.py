from datetime import date
import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Get the Groq API key from environment variables
groq_api_key = os.environ.get("GROQ_API_KEY")

# Check if the API key exists
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable not found or empty. Please ensure it is set correctly in your .env file.")


# Instantiate the Groq LLM
# Assumes GROQ_API_KEY is set in the environment (.env file)
# You might need to specify a model_name if you don't want the default
llm = ChatGroq(
    api_key=groq_api_key,
    model='deepseek-r1-distill-llama-70b'
)


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class AgenticStock():
    """AgenticStock crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @before_kickoff
    def prepare_inputs(self, inputs):
        #Add current date
        inputs['current_date'] = str(date.today())
        return inputs

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    #@agent
    #def reporting_analyst(self) -> Agent:
    #    return Agent(
    #        config=self.agents_config['reporting_analyst'],
    #        verbose=True
    #    )
      
    @agent
    def Sentiment_Analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['Sentiment_Analyst'],
            verbose=True
        )
    
    @agent
    def Fundamental_Analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['Fundamental_Analyst'],
            verbose=True
        )
    
    @agent
    def Technical_Analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['Technical_Analyst'],
            verbose=True
        )
    
    @agent
    def Risk_Manager(self) -> Agent:
        return Agent(
            config=self.agents_config['Risk_Manager'],
            verbose=True
        )
    
    @agent
    def Recommendation_Engine(self) -> Agent:
        return Agent(
            config=self.agents_config['Recommendation_Engine'],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    # @task
    # def reporting_task(self) -> Task:
    #    return Task(
    #        config=self.tasks_config['reporting_task'],
    #        output_file='report.md'
    #    )

    @task
    def sentiment_task(self) -> Task:
        return Task(
            config=self.tasks_config['sentiment_analysis_task'],
        )
    
    @task
    def fundamental_task(self) -> Task:
        return Task(
            config=self.tasks_config['fundamental_analysis_task'],
        )
    
    @task
    def technical_task(self) -> Task:
        return Task(
            config=self.tasks_config['technical_analysis_task'],
        )
    
    @task
    def risk_task(self) -> Task:
        return Task(
            config=self.tasks_config['risk_assessment_task'],
        )
    
    @task
    def final_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_recommendation_task'],
            output_file='final_recommendation.md'
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AgenticStock crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
            llm=llm # Set the default Groq LLM for the crew
        )
