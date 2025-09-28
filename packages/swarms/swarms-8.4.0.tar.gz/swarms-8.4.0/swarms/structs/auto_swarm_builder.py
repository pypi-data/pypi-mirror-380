import json
import traceback
from typing import List, Optional

from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseModel, Field

from swarms.structs.agent import Agent
from swarms.structs.conversation import Conversation
from swarms.structs.ma_utils import set_random_models_for_agents
from swarms.structs.swarm_router import SwarmRouter, SwarmType
from swarms.utils.litellm_wrapper import LiteLLM

load_dotenv()

BOSS_SYSTEM_PROMPT = """
You are an expert multi-agent architecture designer and team coordinator. Your role is to create and orchestrate sophisticated teams of specialized AI agents, each with distinct personalities, roles, and capabilities. Your primary goal is to ensure the multi-agent system operates efficiently while maintaining clear communication, well-defined responsibilities, and optimal task distribution.

### Core Design Principles:

1. **Comprehensive Task Analysis**:
   - Thoroughly deconstruct the task into its fundamental components and sub-tasks
   - Identify the specific skills, knowledge domains, and personality traits required for each component
   - Analyze potential challenges, dependencies, and coordination requirements between agents
   - Map out optimal workflows, information flow patterns, and decision-making hierarchies
   - Consider scalability, maintainability, and adaptability requirements

2. **Agent Design Excellence**:
   - Each agent must have a crystal-clear, specific purpose and domain of expertise
   - Design agents with distinct, complementary personalities that enhance team dynamics
   - Ensure agents are self-aware of their limitations and know when to seek assistance
   - Create agents that can effectively communicate progress, challenges, and insights
   - Design for resilience, adaptability, and continuous learning capabilities

3. **Comprehensive Agent Framework**:
   For each agent, meticulously define:
   - **Role & Purpose**: Precise description of responsibilities, authority, and contribution to team objectives
   - **Personality Profile**: Distinct characteristics that influence thinking patterns, communication style, and decision-making approach
   - **Expertise Matrix**: Specific knowledge domains, skill sets, tools, and capabilities
   - **Communication Protocol**: How the agent presents information, interacts with others, and reports progress
   - **Decision-Making Framework**: Systematic approach to problem-solving, risk assessment, and choice evaluation
   - **Limitations & Boundaries**: Clear constraints, ethical guidelines, and operational boundaries
   - **Collaboration Strategy**: How the agent works with others, shares knowledge, and contributes to team success

4. **Advanced System Prompt Engineering**:
   Create comprehensive system prompts that include:
   - Detailed role and purpose explanation with context and scope
   - Rich personality description with behavioral guidelines and interaction patterns
   - Comprehensive capabilities, tools, and resource specifications
   - Detailed communication protocols, reporting requirements, and feedback mechanisms
   - Systematic problem-solving approach with decision-making frameworks
   - Collaboration guidelines, team interaction rules, and conflict resolution procedures
   - Quality standards, success criteria, and performance metrics
   - Error handling, recovery procedures, and escalation protocols

5. **Multi-Agent Coordination Architecture**:
   - Design robust communication channels and protocols between agents
   - Establish clear task handoff procedures and information sharing mechanisms
   - Create feedback loops for continuous improvement and adaptation
   - Implement comprehensive error handling and recovery procedures
   - Define escalation paths for complex issues and decision-making hierarchies
   - Design monitoring, logging, and performance tracking systems

6. **Quality Assurance & Governance**:
   - Set measurable success criteria for each agent and the overall system
   - Implement verification steps, validation procedures, and quality checks
   - Create mechanisms for self-assessment, peer review, and continuous improvement
   - Establish protocols for handling edge cases, unexpected situations, and failures
   - Design governance structures for oversight, accountability, and performance management

### Multi-Agent Architecture Types:

Choose the most appropriate architecture based on task requirements:

- **AgentRearrange**: Dynamic task reallocation based on agent performance and workload
- **MixtureOfAgents**: Parallel processing with specialized agents working independently
- **SpreadSheetSwarm**: Structured data processing with coordinated workflows
- **SequentialWorkflow**: Linear task progression with handoffs between agents
- **ConcurrentWorkflow**: Parallel execution with coordination and synchronization
- **GroupChat**: Collaborative discussion and consensus-building approach
- **MultiAgentRouter**: Intelligent routing and load balancing across agents
- **AutoSwarmBuilder**: Self-organizing and self-optimizing agent teams
- **HiearchicalSwarm**: Layered decision-making with management and execution tiers
- **MajorityVoting**: Democratic decision-making with voting mechanisms
- **MALT**: Multi-agent learning and training with knowledge sharing
- **CouncilAsAJudge**: Deliberative decision-making with expert panels
- **InteractiveGroupChat**: Dynamic group interactions with real-time collaboration
- **HeavySwarm**: High-capacity processing with multiple specialized agents

### Output Requirements:

When creating a multi-agent system, provide:

1. **Agent Specifications**:
   - Comprehensive role and purpose statements
   - Detailed personality profiles and behavioral characteristics
   - Complete capabilities, limitations, and boundary definitions
   - Communication style and interaction protocols
   - Collaboration strategies and team integration plans

2. **System Prompts**:
   - Complete, detailed prompts that embody each agent's identity and capabilities
   - Clear behavioral instructions and decision-making frameworks
   - Specific interaction guidelines and reporting requirements
   - Quality standards and performance expectations

3. **Architecture Design**:
   - Team structure, hierarchy, and reporting relationships
   - Communication flow patterns and information routing
   - Task distribution strategies and workload balancing
   - Quality control measures and performance monitoring
   - Error handling and recovery procedures

### Best Practices:

- Prioritize clarity, specificity, and precision in agent design
- Ensure each agent has a unique, well-defined role with clear boundaries
- Create comprehensive, detailed system prompts that leave no ambiguity
- Maintain thorough documentation of agent capabilities, limitations, and interactions
- Design for scalability, adaptability, and long-term maintainability
- Focus on creating agents that work together synergistically and efficiently
- Consider edge cases, failure modes, and contingency planning
- Implement robust error handling, monitoring, and recovery procedures
- Design for continuous learning, improvement, and optimization
- Ensure ethical considerations, safety measures, and responsible AI practices
"""


execution_types = [
    "return-agents",
    "execute-swarm-router",
    "return-swarm-router-config",
    "return-agent-configurations",
]


class AgentConfig(BaseModel):
    """Configuration for an individual agent in a swarm"""

    name: str = Field(
        description="The name of the agent. This should be a unique identifier that distinguishes this agent from others within the swarm. The name should reflect the agent's primary function, role, or area of expertise, and should be easily recognizable by both humans and other agents in the system. A well-chosen name helps clarify the agent's responsibilities and facilitates effective communication and collaboration within the swarm.",
    )
    description: str = Field(
        description=(
            "A comprehensive description of the agent's purpose, core responsibilities, and capabilities within the swarm. One sentence is enough."
        ),
    )
    system_prompt: str = Field(
        description=(
            "The system prompt that defines the agent's behavior. This prompt should be extremely long, comprehensive, and extensive, encapsulating the agent's identity, operational guidelines, and decision-making framework in great detail. It provides the foundational instructions that guide the agent's actions, communication style, and interaction protocols with both users and other agents. The system prompt should be highly detailed, unambiguous, and exhaustive, ensuring the agent consistently acts in accordance with its intended role and adheres to the swarm's standards and best practices. The prompt should leave no ambiguity and cover all relevant aspects of the agent's responsibilities, behaviors, and expected outcomes."
        ),
    )
    goal: str = Field(
        description="The goal of the agent. This should clearly state the primary objective or desired outcome the agent is tasked with achieving. The goal should be specific, measurable, and aligned with the overall mission of the swarm. It serves as the guiding principle for the agent's actions and decision-making processes, helping to maintain focus and drive effective collaboration within the multi-agent system.",
    )
    model_name: str = Field(
        description="The model to use for the agent. This is the model that will be used to generate the agent's responses. For example, 'gpt-4o-mini' or 'claude-sonnet-3.7-sonnet-20240620'."
    )
    temperature: float = Field(
        description="The temperature to use for the agent. This controls the randomness of the agent's responses. For example, 0.5 or 1.0."
    )
    max_loops: int = Field(
        description="The maximum number of loops for the agent to run. This is the maximum number of times the agent will run its loop. For example, 1, 2, or 3. Keep this set to 1 unless the agent requires more than one loop to complete its task.",
    )

    # max_loops: int = Field(
    #     description="The maximum number of loops for the agent to run",
    # )

    class Config:
        arbitrary_types_allowed = True


class AgentsConfig(BaseModel):
    """Configuration for a list of agents in a swarm"""

    agents: List[AgentConfig] = Field(
        description="A list of agent configurations",
    )


class SwarmRouterConfig(BaseModel):
    """Configuration model for SwarmRouter."""

    name: str = Field(description="The name of the team of agents")
    description: str = Field(
        description="Description of the team of agents"
    )
    agents: List[AgentConfig] = Field(
        description="A list of agent configurations",
    )
    swarm_type: SwarmType = Field(
        description="Type of multi-agent structure to use",
    )
    rearrange_flow: Optional[str] = Field(
        description="Flow configuration string. Only to be used if you you use the AgentRearrange multi-agent structure"
    )
    rules: Optional[str] = Field(
        description="Rules to inject into every agent. This is a string of rules that will be injected into every agent's system prompt. This is a good place to put things like 'You are a helpful assistant' or 'You are a helpful assistant that can answer questions and help with tasks'."
    )

    task: str = Field(
        description="The task to be executed by the swarm",
    )

    class Config:
        arbitrary_types_allowed = True


class AutoSwarmBuilder:
    """A class that automatically builds and manages swarms of AI agents.

    This class handles the creation, coordination and execution of multiple AI agents working
    together as a swarm to accomplish complex tasks. It uses a boss agent to delegate work
    and create new specialized agents as needed.

    Args:
        name (str): The name of the swarm
        description (str): A description of the swarm's purpose
        verbose (bool, optional): Whether to output detailed logs. Defaults to True.
        max_loops (int, optional): Maximum number of execution loops. Defaults to 1.
        random_models (bool, optional): Whether to use random models for agents. Defaults to True.
    """

    def __init__(
        self,
        name: str = "auto-swarm-builder",
        description: str = "Auto Swarm Builder",
        verbose: bool = True,
        max_loops: int = 1,
        model_name: str = "gpt-4.1",
        generate_router_config: bool = False,
        interactive: bool = False,
        max_tokens: int = 8000,
        execution_type: execution_types = "return-agents",
    ):
        """Initialize the AutoSwarmBuilder.

        Args:
            name (str): The name of the swarm
            description (str): A description of the swarm's purpose
            verbose (bool): Whether to output detailed logs
            max_loops (int): Maximum number of execution loops
            random_models (bool): Whether to use random models for agents
        """
        self.name = name
        self.description = description
        self.verbose = verbose
        self.max_loops = max_loops
        self.model_name = model_name
        self.generate_router_config = generate_router_config
        self.interactive = interactive
        self.max_tokens = max_tokens
        self.execution_type = execution_type
        self.conversation = Conversation()

        self.reliability_check()

    def reliability_check(self):

        if self.max_loops == 0:
            raise ValueError(
                f"AutoSwarmBuilder: {self.name} max_loops cannot be 0"
            )

        logger.info(
            f"Initializing AutoSwarmBuilder: {self.name} Description: {self.description}"
        )

    def _execute_task(self, task: str):
        logger.info(f"Executing task: {task}")

        agents = self.create_agents(task)

        if self.execution_type == "return-agents":
            logger.info("Setting random models for agents")
            agents = set_random_models_for_agents(agents=agents)

        return self.initialize_swarm_router(agents=agents, task=task)

    def run(self, task: str, *args, **kwargs):
        """Run the swarm on a given task.

        Args:
            task (str): The task to execute
            *args: Additional positional arguments
            **kwargs: Additional keyword arguments

        Returns:
            Any: The result of the swarm execution

        Raises:
            Exception: If there's an error during execution
        """
        try:

            if self.execution_type == "return-swarm-router-config":
                return self.create_router_config(task)
            elif self.execution_type == "return-agent-configurations":
                return self.create_agents(task)
            else:
                return self._execute_task(task)

        except Exception as e:
            logger.error(
                f"AutoSwarmBuilder: Error in swarm execution: {str(e)} Traceback: {traceback.format_exc()}",
                exc_info=True,
            )
            raise

    def dict_to_agent(self, output: dict):
        agents = []
        if isinstance(output, dict):
            for agent_config in output["agents"]:
                logger.info(f"Building agent: {agent_config['name']}")
                agent = self.build_agent(
                    agent_name=agent_config["name"],
                    agent_description=agent_config["description"],
                    agent_system_prompt=agent_config["system_prompt"],
                )
                agents.append(agent)
                logger.info(
                    f"Successfully built agent: {agent_config['name']}"
                )

        return agents

    def create_router_config(self, task: str):
        try:
            logger.info(
                f"Creating swarm router config for task: {task}"
            )

            model = self.build_llm_agent(config=SwarmRouterConfig)

            output = model.run(
                f"Create the multi-agent team for the following task: {task}"
            )

            output = json.loads(output)

            return output

        except Exception as e:
            logger.error(
                f"Error creating swarm router config: {str(e)} Traceback: {traceback.format_exc()}",
                exc_info=True,
            )
            raise e

    def build_llm_agent(self, config: BaseModel):
        # return OpenAIFunctionCaller(
        #     system_prompt=BOSS_SYSTEM_PROMPT,
        #     api_key=os.getenv("OPENAI_API_KEY"),
        #     temperature=0.5,
        #     base_model=config,
        #     model_name=self.model_name,
        #     max_tokens=self.max_tokens,
        # )
        return LiteLLM(
            model_name=self.model_name,
            system_prompt=BOSS_SYSTEM_PROMPT,
            temperature=0.5,
            response_format=config,
            max_tokens=self.max_tokens,
        )

    def create_agents(self, task: str):
        """Create agents for a given task.

        Args:
            task (str): The task to create agents for

        Returns:
            List[Agent]: List of created agents

        Raises:
            Exception: If there's an error during agent creation
        """
        try:
            model = self.build_llm_agent(config=AgentsConfig)

            output = model.run(
                f"Create the agents for the following task: {task}"
            )

            output = json.loads(output)

            return output

        except Exception as e:
            logger.error(
                f"Error creating agents: {str(e)} Traceback: {traceback.format_exc()}",
                exc_info=True,
            )
            raise e

    def build_agent(
        self,
        agent_name: str,
        agent_description: str,
        agent_system_prompt: str,
    ) -> Agent:
        """Build a single agent with enhanced error handling.

        Args:
            agent_name (str): Name of the agent
            agent_description (str): Description of the agent
            agent_system_prompt (str): System prompt for the agent

        Returns:
            Agent: The constructed agent

        Raises:
            Exception: If there's an error during agent construction
        """
        logger.info(f"Building agent: {agent_name}")
        try:
            agent = Agent(
                agent_name=agent_name,
                agent_description=agent_description,
                system_prompt=agent_system_prompt,
                verbose=self.verbose,
                dynamic_temperature_enabled=False,
            )
            logger.info(f"Successfully built agent: {agent_name}")
            return agent
        except Exception as e:
            logger.error(
                f"Error building agent {agent_name}: {str(e)}",
                exc_info=True,
            )
            raise

    def initialize_swarm_router(self, agents: List[Agent], task: str):
        """Initialize and run the swarm router.

        Args:
            agents (List[Agent]): List of agents to use
            task (str): The task to execute

        Returns:
            Any: The result of the swarm router execution

        Raises:
            Exception: If there's an error during router initialization or execution
        """
        try:
            logger.info("Initializing swarm router")
            model = self.build_llm_agent(config=SwarmRouterConfig)

            swarm_spec = model.run(
                f"Create the swarm spec for the following task: {task}"
            )

            print(swarm_spec)

            print(type(swarm_spec))

            swarm_router = SwarmRouter(
                name=swarm_spec["name"],
                description=swarm_spec["description"],
                max_loops=1,
                swarm_type=swarm_spec["swarm_type"],
                rearrange_flow=swarm_spec["rearrange_flow"],
                rules=swarm_spec["rules"],
                multi_agent_collab_prompt=swarm_spec[
                    "multi_agent_collab_prompt"
                ],
                agents=agents,
                output_type="dict",
            )

            logger.info("Starting swarm router execution")
            return swarm_router.run(task)
        except Exception as e:
            logger.error(
                f"Error in swarm router initialization/execution: {str(e)}",
                exc_info=True,
            )
            raise

    def batch_run(self, tasks: List[str]):
        """Run the swarm on a list of tasks.

        Args:
            tasks (List[str]): List of tasks to execute

        Returns:
            List[Any]: List of results from each task execution

        Raises:
            Exception: If there's an error during batch execution
        """

        return [self.run(task) for task in tasks]

    def list_types(self):
        return execution_types
