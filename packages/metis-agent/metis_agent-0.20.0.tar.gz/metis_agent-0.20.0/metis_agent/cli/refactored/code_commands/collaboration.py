"""
Multi-agent collaboration functionality.

This module handles parsing @mentions, coordinating between multiple agents,
and displaying collaborative responses.
"""

import re
from typing import List, Tuple, Dict, Optional, Any

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


class CollaborationManager:
    """Manages multi-agent collaboration features."""

    def __init__(self):
        self.console = Console() if RICH_AVAILABLE else None

    def parse_mentions(self, text: str) -> Tuple[str, List[str]]:
        """Parse @mentions from text and return cleaned text and list of mentioned agents."""
        # Find all @mentions in the text
        mentions = re.findall(r'@([a-zA-Z0-9_-]+)', text)

        # Handle @everyone special case
        if 'everyone' in mentions:
            # Get all available agents
            try:
                from ...cli.agent_commands import get_agent_manager
                agent_manager = get_agent_manager()
                if agent_manager:
                    all_agents = agent_manager.list_agents()
                    agent_names = [agent.get('name') for agent in all_agents if agent.get('name')]
                    mentions = list(set(mentions + agent_names))
                    mentions = [m for m in mentions if m != 'everyone']
            except ImportError:
                pass

        # Remove @mentions from text
        cleaned_text = re.sub(r'@[a-zA-Z0-9_-]+\s*', '', text).strip()

        return cleaned_text, mentions

    def process_collaboration(self, mentioned_agents: List[str], query: str,
                            session_id: Optional[str] = None) -> List[Tuple[str, str]]:
        """Process collaborative query with mentioned agents."""
        try:
            from ...cli.agent_commands import get_agent_manager
            agent_manager = get_agent_manager()
            if not agent_manager:
                raise ImportError("Agent manager not available")

            # Determine collaboration type
            if len(mentioned_agents) == 1:
                return self._process_single_agent_response(
                    mentioned_agents[0], query, agent_manager, session_id
                )
            else:
                return self._process_multi_agent_query(
                    mentioned_agents, query, agent_manager, session_id
                )

        except ImportError:
            # Fallback if agent manager not available
            return [("system", "Multi-agent collaboration not available in this configuration")]

    def _process_multi_agent_query(self, mentioned_agents: List[str], query: str,
                                 agent_manager: Any, session_id: str) -> List[Tuple[str, str]]:
        """Process query with multiple agents."""
        responses = []

        for agent_id in mentioned_agents:
            try:
                agent = agent_manager.get_agent(agent_id)
                if agent:
                    response = agent.process_query(query, session_id=session_id)
                    responses.append((agent_id, response))
                else:
                    responses.append((agent_id, f"Agent '{agent_id}' not found"))
            except Exception as e:
                responses.append((agent_id, f"Error processing query: {str(e)}"))

        return responses

    def _process_single_agent_response(self, agent_id: str, query: str,
                                     agent_manager: Any, session_id: str) -> List[Tuple[str, str]]:
        """Process query with a single mentioned agent."""
        try:
            agent = agent_manager.get_agent(agent_id)
            if agent:
                response = agent.process_query(query, session_id=session_id)
                return [(agent_id, response)]
            else:
                return [(agent_id, f"Agent '{agent_id}' not found")]
        except Exception as e:
            return [(agent_id, f"Error processing query: {str(e)}")]

    def _process_collaborative_discussion(self, mentioned_agents: List[str], query: str,
                                        agent_manager: Any, session_id: str) -> List[Tuple[str, str]]:
        """Process collaborative discussion between agents."""
        responses = []
        conversation_context = {}

        for i, agent_id in enumerate(mentioned_agents):
            try:
                agent = agent_manager.get_agent(agent_id)
                if not agent:
                    responses.append((agent_id, f"Agent '{agent_id}' not found"))
                    continue

                # Build collaborative context
                collaborative_context = self._build_collaborative_context(agent_id, conversation_context)

                # Process query with context
                enhanced_query = f"{query}\n\nCollaborative context:\n{collaborative_context}"
                response = agent.process_query(enhanced_query, session_id=session_id)

                responses.append((agent_id, response))
                conversation_context[agent_id] = response

            except Exception as e:
                responses.append((agent_id, f"Error in collaborative processing: {str(e)}"))

        return responses

    def _build_collaborative_context(self, current_agent_id: str, conversation_context: Dict[str, str]) -> str:
        """Build collaborative context from previous agent responses."""
        if not conversation_context:
            return "This is the start of a collaborative discussion."

        context_parts = ["Previous contributions to this discussion:"]
        for agent_id, response in conversation_context.items():
            if agent_id != current_agent_id:
                # Summarize previous responses
                summary = response[:200] + "..." if len(response) > 200 else response
                context_parts.append(f"- {agent_id}: {summary}")

        context_parts.append(f"\nAs {current_agent_id}, please contribute your perspective while considering the above inputs.")
        return "\n".join(context_parts)

    def display_responses(self, responses: List[Tuple[str, str]]):
        """Display agent responses with appropriate formatting."""
        if not responses:
            return

        try:
            from ...cli.agent_commands import get_agent_manager
            agent_manager = get_agent_manager()
        except ImportError:
            agent_manager = None

        if RICH_AVAILABLE and self.console:
            if len(responses) > 1:
                self._display_collaborative_discussion_rich(responses, agent_manager, self.console)
            else:
                self._display_standard_responses_rich(responses, agent_manager, self.console)
        else:
            if len(responses) > 1:
                self._display_collaborative_discussion_plain(responses, agent_manager)
            else:
                self._display_standard_responses_plain(responses, agent_manager)

    def _display_collaborative_discussion_rich(self, responses: List[Tuple[str, str]],
                                             agent_manager: Any, console: Console):
        """Display collaborative discussion with Rich formatting."""
        console.print("\n" + "="*60)
        console.print("🤝 Collaborative Discussion", style="bold blue")
        console.print("="*60 + "\n")

        for i, (agent_id, response) in enumerate(responses, 1):
            # Get agent info
            agent_info = self._get_agent_display_info(agent_id, agent_manager)

            # Create panel for each agent's response
            panel_title = f"🤖 {agent_info['display_name']} ({i}/{len(responses)})"

            panel = Panel(
                response,
                title=panel_title,
                title_align="left",
                border_style=agent_info['color'],
                padding=(1, 2)
            )

            console.print(panel)
            console.print()

        # Summary
        console.print("💡 Discussion Summary", style="bold yellow")
        console.print(f"Participants: {', '.join([r[0] for r in responses])}")
        console.print(f"Total responses: {len(responses)}")

    def _display_standard_responses_rich(self, responses: List[Tuple[str, str]],
                                       agent_manager: Any, console: Console):
        """Display standard responses with Rich formatting."""
        for agent_id, response in responses:
            agent_info = self._get_agent_display_info(agent_id, agent_manager)

            panel = Panel(
                response,
                title=f"🤖 {agent_info['display_name']}",
                title_align="left",
                border_style=agent_info['color'],
                padding=(1, 2)
            )

            console.print(panel)
            console.print()

    def _display_collaborative_discussion_plain(self, responses: List[Tuple[str, str]],
                                              agent_manager: Any):
        """Display collaborative discussion with plain text formatting."""
        print("\n" + "="*60)
        print("🤝 Collaborative Discussion")
        print("="*60 + "\n")

        for i, (agent_id, response) in enumerate(responses, 1):
            agent_info = self._get_agent_display_info(agent_id, agent_manager)

            print(f"🤖 {agent_info['display_name']} ({i}/{len(responses)}):")
            print("-" * 40)
            print(response)
            print("\n" + "="*40 + "\n")

        print("💡 Discussion Summary:")
        print(f"Participants: {', '.join([r[0] for r in responses])}")
        print(f"Total responses: {len(responses)}")

    def _display_standard_responses_plain(self, responses: List[Tuple[str, str]],
                                        agent_manager: Any):
        """Display standard responses with plain text formatting."""
        for agent_id, response in responses:
            agent_info = self._get_agent_display_info(agent_id, agent_manager)

            print(f"\n🤖 {agent_info['display_name']}:")
            print("-" * 40)
            print(response)
            print("-" * 40)

    def _get_agent_display_info(self, agent_id: str, agent_manager: Any) -> Dict[str, str]:
        """Get display information for an agent."""
        default_info = {
            'display_name': agent_id,
            'color': 'blue',
            'description': 'AI Agent'
        }

        if not agent_manager:
            return default_info

        try:
            agent = agent_manager.get_agent(agent_id)
            if agent and hasattr(agent, 'config'):
                return {
                    'display_name': getattr(agent.config, 'display_name', agent_id),
                    'color': getattr(agent.config, 'theme_color', 'blue'),
                    'description': getattr(agent.config, 'description', 'AI Agent')
                }
        except Exception:
            pass

        return default_info