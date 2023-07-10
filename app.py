from vvhan.horoscope import HoroscopeTool
from regular.weather import WeatherTool

from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import AzureChatOpenAI
from langchain.tools import DuckDuckGoSearchRun, OpenWeatherMapQueryRun
from langchain.callbacks.streaming_stdout_final_only import FinalStreamingStdOutCallbackHandler
import chainlit as cl

# The search tool has no async implementation, we fall back to sync
@cl.langchain_factory(use_async=False)
def load():
    # 大模型 max_tokens = 4096
    llm = AzureChatOpenAI(
        deployment_name="gpt-35-16k",
        model_name="gpt-35-turbo-16k",
        temperature=0.1,
        streaming=True,
        max_tokens=4096,
        max_retries=1,
        callbacks=[FinalStreamingStdOutCallbackHandler()])

    # Tools
    tools = [
        WeatherTool(), 
        HoroscopeTool(), DuckDuckGoSearchRun()]
    # Return the agent
    return initialize_agent(
        tools, llm, 
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )
