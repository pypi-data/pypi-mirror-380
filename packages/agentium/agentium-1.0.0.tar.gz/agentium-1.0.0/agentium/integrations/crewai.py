"""
CrewAI Integration Module

This module provides seamless integration with CrewAI framework,
allowing Agentium features to be used within CrewAI workflows.
"""

from typing import Dict, Any, List, Optional, Union, Callable
from dataclasses import dataclass
import json

try:
    from crewai import Agent, Task, Crew
    from crewai.tools import BaseTool as CrewAIBaseTool
    CREWAI_AVAILABLE = True
except ImportError:
    CREWAI_AVAILABLE = False
    # Create minimal base classes for type hints
    class Agent:
        pass
    class Task:
        pass
    class Crew:
        pass
    class CrewAIBaseTool:
        pass

from ..core.condenser import Condenser
from ..core.optimizer import Optimizer
from ..core.extractor import Extractor
from ..core.communicator import Communicator
from ..core.translator import Translator
from ..core.insight_generator import InsightGenerator
from ..core.workflow_helper import WorkflowHelper
from ..core.summarize_custom import CustomSummarizer
from ..core.memory_helper import MemoryHelper
from ..utils.logger_utils import LoggerUtils


class AgentiumCrewAITool(CrewAIBaseTool):
    """Base class for Agentium CrewAI tools"""
    
    def __init__(self, agentium_component, name: str, description: str):
        self.agentium_component = agentium_component
        self.name = name
        self.description = description
        self.logger = LoggerUtils.get_logger(__name__)
    
    def _run(self, *args, **kwargs) -> str:
        """Run the tool - to be implemented by subclasses"""
        raise NotImplementedError


class CondenserCrewAITool(AgentiumCrewAITool):
    """CrewAI tool wrapper for Condenser"""
    
    def __init__(self, condenser: Optional[Condenser] = None):
        condenser = condenser or Condenser()
        super().__init__(
            agentium_component=condenser,
            name="text_condenser",
            description="Condense text content intelligently while preserving key information. Useful for reducing lengthy content while maintaining essential details."
        )
    
    def _run(self, content: str, ratio: float = 0.5, **kwargs) -> str:
        """Run the condenser tool"""
        try:
            self.logger.info(f"Condensing text with ratio {ratio}")
            result = self.agentium_component.condense(content, target_ratio=ratio, **kwargs)
            
            condensed_text = result.get('condensed_text', content)
            stats = result.get('stats', {})
            
            # Return formatted result for CrewAI
            return f"Condensed Text ({stats.get('compression_ratio', 'N/A')}% reduction):\n{condensed_text}"
            
        except Exception as e:
            self.logger.error(f"Condenser tool error: {e}")
            return f"Error condensing text: {str(e)}"


class OptimizerCrewAITool(AgentiumCrewAITool):
    """CrewAI tool wrapper for Optimizer"""
    
    def __init__(self, optimizer: Optional[Optimizer] = None):
        optimizer = optimizer or Optimizer()
        super().__init__(
            agentium_component=optimizer,
            name="content_optimizer",
            description="Optimize text, code, or workflow content for better performance and clarity. Supports text refinement, code optimization, and workflow improvements."
        )
    
    def _run(self, content: str, content_type: str = "text", **kwargs) -> str:
        """Run the optimizer tool"""
        try:
            self.logger.info(f"Optimizing {content_type} content")
            result = self.agentium_component.optimize(content, content_type=content_type, **kwargs)
            
            optimized_content = result.get('optimized_content', content)
            improvements = result.get('improvements', [])
            
            # Format result for CrewAI
            improvement_summary = ", ".join(improvements[:3]) if improvements else "General optimization"
            return f"Optimized Content ({improvement_summary}):\n{optimized_content}"
            
        except Exception as e:
            self.logger.error(f"Optimizer tool error: {e}")
            return f"Error optimizing content: {str(e)}"


class ExtractorCrewAITool(AgentiumCrewAITool):
    """CrewAI tool wrapper for Extractor"""
    
    def __init__(self, extractor: Optional[Extractor] = None):
        extractor = extractor or Extractor()
        super().__init__(
            agentium_component=extractor,
            name="data_extractor",
            description="Extract structured information from various data sources including JSON, XML, HTML, CSV, and text patterns. Returns organized data structures."
        )
    
    def _run(self, source: str, extraction_type: str = "auto", **kwargs) -> str:
        """Run the extractor tool"""
        try:
            self.logger.info(f"Extracting data using {extraction_type} method")
            result = self.agentium_component.extract(source, extraction_type=extraction_type, **kwargs)
            
            extracted_data = result.get('extracted_data', {})
            
            # Format extracted data for CrewAI
            if isinstance(extracted_data, dict):
                formatted_data = json.dumps(extracted_data, indent=2, default=str)
            else:
                formatted_data = str(extracted_data)
            
            return f"Extracted Data ({extraction_type}):\n{formatted_data}"
            
        except Exception as e:
            self.logger.error(f"Extractor tool error: {e}")
            return f"Error extracting data: {str(e)}"


class TranslatorCrewAITool(AgentiumCrewAITool):
    """CrewAI tool wrapper for Translator"""
    
    def __init__(self, translator: Optional[Translator] = None):
        translator = translator or Translator()
        super().__init__(
            agentium_component=translator,
            name="text_translator",
            description="Translate text between languages and adapt tone/style. Supports multiple languages and can adjust formality, tone, and cultural context."
        )
    
    def _run(self, text: str, target_language: str = "en", **kwargs) -> str:
        """Run the translator tool"""
        try:
            self.logger.info(f"Translating text to {target_language}")
            result = self.agentium_component.translate(text, target_language=target_language, **kwargs)
            
            translated_text = result.get('translated_text', text)
            detected_language = result.get('detected_language', 'unknown')
            
            return f"Translated from {detected_language} to {target_language}:\n{translated_text}"
            
        except Exception as e:
            self.logger.error(f"Translator tool error: {e}")
            return f"Error translating text: {str(e)}"


class InsightGeneratorCrewAITool(AgentiumCrewAITool):
    """CrewAI tool wrapper for InsightGenerator"""
    
    def __init__(self, insight_generator: Optional[InsightGenerator] = None):
        insight_generator = insight_generator or InsightGenerator()
        super().__init__(
            agentium_component=insight_generator,
            name="insight_generator",
            description="Generate actionable insights from data and text. Provides trend analysis, pattern recognition, and strategic recommendations."
        )
    
    def _run(self, data: str, insight_type: str = "general", **kwargs) -> str:
        """Run the insight generator tool"""
        try:
            self.logger.info(f"Generating {insight_type} insights")
            result = self.agentium_component.generate_insights(data, insight_type=insight_type, **kwargs)
            
            insights = result.get('insights', [])
            confidence_scores = result.get('confidence_scores', [])
            
            # Format insights for CrewAI
            formatted_insights = []
            for i, insight in enumerate(insights[:5]):  # Top 5 insights
                confidence = confidence_scores[i] if i < len(confidence_scores) else 'N/A'
                formatted_insights.append(f"• {insight} (Confidence: {confidence})")
            
            return f"Generated Insights ({insight_type}):\n" + "\n".join(formatted_insights)
            
        except Exception as e:
            self.logger.error(f"Insight generator tool error: {e}")
            return f"Error generating insights: {str(e)}"


class SummarizerCrewAITool(AgentiumCrewAITool):
    """CrewAI tool wrapper for CustomSummarizer"""
    
    def __init__(self, summarizer: Optional[CustomSummarizer] = None):
        summarizer = summarizer or CustomSummarizer()
        super().__init__(
            agentium_component=summarizer,
            name="content_summarizer",
            description="Create custom summaries with various strategies including extractive, bullet points, keyword-based, statistical, and timeline summaries."
        )
    
    def _run(self, content: str, summary_type: str = "extractive", length: str = "medium", **kwargs) -> str:
        """Run the summarizer tool"""
        try:
            self.logger.info(f"Creating {summary_type} summary with {length} length")
            result = self.agentium_component.summarize(content, summary_type=summary_type, length=length, **kwargs)
            
            summary = result.get('summary', '')
            compression_ratio = result.get('compression_ratio', 0)
            
            return f"Summary ({summary_type}, {compression_ratio:.1%} compression):\n{summary}"
            
        except Exception as e:
            self.logger.error(f"Summarizer tool error: {e}")
            return f"Error creating summary: {str(e)}"


class CommunicatorCrewAITool(AgentiumCrewAITool):
    """CrewAI tool wrapper for Communicator"""
    
    def __init__(self, communicator: Optional[Communicator] = None):
        communicator = communicator or Communicator()
        super().__init__(
            agentium_component=communicator,
            name="message_sender",
            description="Send messages and notifications through various channels including email, Slack, Discord, Teams, and webhooks."
        )
    
    def _run(self, message: str, channel: str = "email", recipient: str = "", **kwargs) -> str:
        """Run the communicator tool"""
        try:
            self.logger.info(f"Sending message via {channel}")
            
            # Add recipient to kwargs if provided
            if recipient:
                kwargs['recipient'] = recipient
            
            result = self.agentium_component.send_message(message, channel=channel, **kwargs)
            
            message_id = result.get('message_id', 'N/A')
            status = result.get('status', 'unknown')
            
            return f"Message sent via {channel} (ID: {message_id}, Status: {status})"
            
        except Exception as e:
            self.logger.error(f"Communicator tool error: {e}")
            return f"Error sending message: {str(e)}"


class AgentiumCrewAIAgent:
    """Enhanced CrewAI agent with Agentium capabilities"""
    
    def __init__(
        self,
        role: str,
        goal: str,
        backstory: str,
        tools: Optional[List[AgentiumCrewAITool]] = None,
        memory_context: Optional[str] = None,
        **kwargs
    ):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.logger = LoggerUtils.get_logger(__name__)
        
        # Initialize memory if context provided
        self.memory_helper = None
        self.memory_context = None
        
        if memory_context:
            self.memory_helper = MemoryHelper()
            self.memory_context = self.memory_helper.create_context(memory_context)
        
        # Initialize tools
        self.agentium_tools = tools or []
        
        # Create CrewAI agent if available
        if CREWAI_AVAILABLE:
            crewai_tools = [tool for tool in self.agentium_tools]
            self.agent = Agent(
                role=role,
                goal=goal,
                backstory=backstory,
                tools=crewai_tools,
                **kwargs
            )
        else:
            self.agent = None
            self.logger.warning("CrewAI not available - agent will have limited functionality")
    
    def add_tool(self, tool: AgentiumCrewAITool):
        """Add an Agentium tool to the agent"""
        self.agentium_tools.append(tool)
        
        if self.agent:
            # Update CrewAI agent tools (this depends on CrewAI's API)
            pass
    
    def remember(self, key: str, value: Any):
        """Store information in agent memory"""
        if self.memory_context:
            self.memory_context.store(key, value)
            self.logger.info(f"Stored memory: {key}")
    
    def recall(self, key: str) -> Any:
        """Recall information from agent memory"""
        if self.memory_context:
            return self.memory_context.get(key)
        return None
    
    def get_memories(self) -> Dict[str, Any]:
        """Get all stored memories"""
        if self.memory_context:
            return self.memory_context.get_all()
        return {}
    
    def clear_memory(self):
        """Clear agent memory"""
        if self.memory_context:
            self.memory_context.clear()
            self.logger.info("Cleared agent memory")


class AgentiumCrewAITask:
    """Enhanced CrewAI task with Agentium features"""
    
    def __init__(
        self,
        description: str,
        agent: AgentiumCrewAIAgent,
        expected_output: str = "",
        tools: Optional[List[AgentiumCrewAITool]] = None,
        context: Optional[List['AgentiumCrewAITask']] = None,
        **kwargs
    ):
        self.description = description
        self.agent = agent
        self.expected_output = expected_output
        self.tools = tools or []
        self.context = context or []
        self.logger = LoggerUtils.get_logger(__name__)
        
        # Create CrewAI task if available
        if CREWAI_AVAILABLE and agent.agent:
            crewai_tools = [tool for tool in self.tools]
            crewai_context = [task.task for task in self.context if task.task]
            
            self.task = Task(
                description=description,
                agent=agent.agent,
                expected_output=expected_output,
                tools=crewai_tools,
                context=crewai_context,
                **kwargs
            )
        else:
            self.task = None
            self.logger.warning("CrewAI not available - task will have limited functionality")
    
    def add_tool(self, tool: AgentiumCrewAITool):
        """Add a tool to the task"""
        self.tools.append(tool)
        
        if self.task:
            # Update CrewAI task tools (this depends on CrewAI's API)
            pass
    
    def add_context(self, task: 'AgentiumCrewAITask'):
        """Add context from another task"""
        self.context.append(task)
        
        if self.task and task.task:
            # Update CrewAI task context (this depends on CrewAI's API)
            pass


class AgentiumCrewAICrew:
    """Enhanced CrewAI crew with Agentium capabilities"""
    
    def __init__(
        self,
        agents: List[AgentiumCrewAIAgent],
        tasks: List[AgentiumCrewAITask],
        memory_context: Optional[str] = None,
        **kwargs
    ):
        self.agents = agents
        self.tasks = tasks
        self.logger = LoggerUtils.get_logger(__name__)
        
        # Initialize shared memory
        self.memory_helper = None
        self.memory_context = None
        
        if memory_context:
            self.memory_helper = MemoryHelper()
            self.memory_context = self.memory_helper.create_context(memory_context)
        
        # Create CrewAI crew if available
        if CREWAI_AVAILABLE:
            crewai_agents = [agent.agent for agent in agents if agent.agent]
            crewai_tasks = [task.task for task in tasks if task.task]
            
            if crewai_agents and crewai_tasks:
                self.crew = Crew(
                    agents=crewai_agents,
                    tasks=crewai_tasks,
                    **kwargs
                )
            else:
                self.crew = None
                self.logger.warning("Cannot create CrewAI crew - missing agents or tasks")
        else:
            self.crew = None
            self.logger.warning("CrewAI not available - crew will have limited functionality")
    
    def add_agent(self, agent: AgentiumCrewAIAgent):
        """Add an agent to the crew"""
        self.agents.append(agent)
        self.logger.info(f"Added agent: {agent.role}")
    
    def add_task(self, task: AgentiumCrewAITask):
        """Add a task to the crew"""
        self.tasks.append(task)
        self.logger.info(f"Added task: {task.description[:50]}...")
    
    def execute(self, **kwargs):
        """Execute the crew"""
        if self.crew:
            try:
                result = self.crew.kickoff(**kwargs)
                
                # Store execution results in shared memory
                if self.memory_context:
                    self.memory_context.store("last_execution_result", result)
                    self.memory_context.store("execution_timestamp", LoggerUtils.get_timestamp())
                
                return result
            except Exception as e:
                self.logger.error(f"Error executing crew: {e}")
                return f"Execution failed: {str(e)}"
        else:
            self.logger.warning("Cannot execute crew - CrewAI not available")
            return "Execution not available - CrewAI not installed"
    
    def get_execution_history(self) -> List[Dict[str, Any]]:
        """Get execution history from memory"""
        if self.memory_context:
            return self.memory_context.get("execution_history", [])
        return []


class AgentiumCrewAIIntegration:
    """Main integration class for CrewAI"""
    
    def __init__(self):
        self.logger = LoggerUtils.get_logger(__name__)
        self.tools = {}
        self._initialize_tools()
    
    def _initialize_tools(self):
        """Initialize all Agentium tools"""
        try:
            self.tools = {
                'condenser': CondenserCrewAITool(),
                'optimizer': OptimizerCrewAITool(),
                'extractor': ExtractorCrewAITool(),
                'translator': TranslatorCrewAITool(),
                'insight_generator': InsightGeneratorCrewAITool(),
                'summarizer': SummarizerCrewAITool(),
                'communicator': CommunicatorCrewAITool(),
            }
            
            self.logger.info(f"Initialized {len(self.tools)} CrewAI tools")
        
        except Exception as e:
            self.logger.error(f"Error initializing tools: {e}")
    
    def get_tool(self, tool_name: str) -> Optional[AgentiumCrewAITool]:
        """Get a specific tool"""
        return self.tools.get(tool_name)
    
    def get_all_tools(self) -> List[AgentiumCrewAITool]:
        """Get all available tools"""
        return list(self.tools.values())
    
    def create_agent(
        self,
        role: str,
        goal: str,
        backstory: str,
        tools: Optional[List[str]] = None,
        memory_context: Optional[str] = None,
        **kwargs
    ) -> AgentiumCrewAIAgent:
        """Create an Agentium-enhanced CrewAI agent"""
        
        # Get requested tools
        agent_tools = []
        if tools:
            for tool_name in tools:
                tool = self.get_tool(tool_name)
                if tool:
                    agent_tools.append(tool)
                else:
                    self.logger.warning(f"Tool not found: {tool_name}")
        
        return AgentiumCrewAIAgent(
            role=role,
            goal=goal,
            backstory=backstory,
            tools=agent_tools,
            memory_context=memory_context,
            **kwargs
        )
    
    def create_task(
        self,
        description: str,
        agent: AgentiumCrewAIAgent,
        expected_output: str = "",
        tools: Optional[List[str]] = None,
        **kwargs
    ) -> AgentiumCrewAITask:
        """Create an Agentium-enhanced CrewAI task"""
        
        # Get requested tools
        task_tools = []
        if tools:
            for tool_name in tools:
                tool = self.get_tool(tool_name)
                if tool:
                    task_tools.append(tool)
                else:
                    self.logger.warning(f"Tool not found: {tool_name}")
        
        return AgentiumCrewAITask(
            description=description,
            agent=agent,
            expected_output=expected_output,
            tools=task_tools,
            **kwargs
        )
    
    def create_crew(
        self,
        agents: List[AgentiumCrewAIAgent],
        tasks: List[AgentiumCrewAITask],
        memory_context: Optional[str] = None,
        **kwargs
    ) -> AgentiumCrewAICrew:
        """Create an Agentium-enhanced CrewAI crew"""
        
        return AgentiumCrewAICrew(
            agents=agents,
            tasks=tasks,
            memory_context=memory_context,
            **kwargs
        )
    
    def is_available(self) -> bool:
        """Check if CrewAI integration is available"""
        return CREWAI_AVAILABLE


# Convenience function for easy integration
def get_agentium_crewai_integration() -> AgentiumCrewAIIntegration:
    """Get the main CrewAI integration object"""
    return AgentiumCrewAIIntegration()


# Example usage functions
def create_content_processing_crew():
    """Example function showing how to create a content processing crew"""
    if not CREWAI_AVAILABLE:
        raise ImportError("CrewAI is required for this functionality")
    
    integration = get_agentium_crewai_integration()
    
    # Create agents
    analyzer = integration.create_agent(
        role="Content Analyzer",
        goal="Analyze and extract insights from content",
        backstory="Expert at understanding and analyzing textual content",
        tools=["extractor", "insight_generator"],
        memory_context="content_analysis"
    )
    
    optimizer = integration.create_agent(
        role="Content Optimizer",
        goal="Improve and refine content quality",
        backstory="Specialist in content optimization and summarization",
        tools=["optimizer", "condenser", "summarizer"],
        memory_context="content_optimization"
    )
    
    # Create tasks
    analysis_task = integration.create_task(
        description="Analyze the provided content and extract key insights",
        agent=analyzer,
        expected_output="Detailed analysis with extracted insights and data patterns"
    )
    
    optimization_task = integration.create_task(
        description="Optimize and condense the content based on the analysis",
        agent=optimizer,
        expected_output="Optimized and condensed content with summary"
    )
    
    # Create crew
    crew = integration.create_crew(
        agents=[analyzer, optimizer],
        tasks=[analysis_task, optimization_task],
        memory_context="content_processing_crew"
    )
    
    return crew