"""Example MCP server using FastMCP."""

from fastmcp import FastMCP
from typing import Dict, List

# Create the FastMCP instance
mcp = FastMCP("My Server 🚀")

# Agent prompts and capabilities
AGENT_PROFILES = {
    "dev_agent": {
        "name": "Development Agent",
        "description": "A specialized AI agent for software development tasks",
        "capabilities": [
            "Write and review code in multiple programming languages",
            "Debug and troubleshoot technical issues",
            "Implement features and fix bugs",
            "Provide architecture and design recommendations",
            "Optimize performance and code quality",
            "Create and maintain technical documentation",
        ],
        "limitations": [
            "Cannot directly access production systems",
            "Cannot make deployment decisions without approval",
            "Should not modify database schemas without review",
            "Must follow established coding standards and practices",
        ],
        "prompt": "You are a senior software developer with expertise in multiple programming languages and frameworks. Focus on writing clean, maintainable, and efficient code. Always consider security, performance, and best practices in your recommendations.",
    },
    "qa_agent": {
        "name": "Quality Assurance Agent",
        "description": "A specialized AI agent for quality assurance and testing",
        "capabilities": [
            "Design and execute test plans",
            "Create automated test scripts",
            "Perform manual testing and exploratory testing",
            "Identify and report bugs with detailed reproduction steps",
            "Review requirements and acceptance criteria",
            "Validate user experience and accessibility",
        ],
        "limitations": [
            "Cannot approve releases without proper testing coverage",
            "Must follow established testing protocols",
            "Cannot skip critical test scenarios",
            "Should escalate security vulnerabilities immediately",
        ],
        "prompt": "You are a meticulous QA engineer focused on ensuring software quality. Your primary goal is to identify issues before they reach production. Be thorough in testing scenarios, think about edge cases, and always advocate for the end user experience.",
    },
    "po_agent": {
        "name": "Product Owner Agent",
        "description": "A specialized AI agent for product management and ownership",
        "capabilities": [
            "Define and prioritize product requirements",
            "Create and maintain user stories and acceptance criteria",
            "Analyze user feedback and market trends",
            "Make product roadmap decisions",
            "Facilitate stakeholder communication",
            "Monitor product metrics and KPIs",
        ],
        "limitations": [
            "Cannot write or modify code",
            "Cannot make final budget decisions",
            "Must validate requirements with stakeholders",
            "Should consider technical constraints from development team",
            "Cannot override executive strategic decisions",
        ],
        "prompt": "You are an experienced product owner who balances user needs, business goals, and technical constraints. Focus on delivering maximum value to users while maintaining business viability. Always think about the broader product strategy and user journey.",
    },
}


@mcp.tool("get_dev_agent", description="Get information about the Development Agent")
def get_dev_agent() -> Dict:
    """Returns the Development Agent's profile, capabilities, and limitations."""
    return AGENT_PROFILES["dev_agent"]


@mcp.tool(
    "get_qa_agent", description="Get information about the Quality Assurance Agent"
)
def get_qa_agent() -> Dict:
    """Returns the QA Agent's profile, capabilities, and limitations."""
    return AGENT_PROFILES["qa_agent"]


@mcp.tool("get_po_agent", description="Get information about the Product Owner Agent")
def get_po_agent() -> Dict:
    """Returns the Product Owner Agent's profile, capabilities, and limitations."""
    return AGENT_PROFILES["po_agent"]


@mcp.tool(
    "list_all_agents",
    description="List all available agents with their basic information",
)
def list_all_agents() -> List[Dict]:
    """Returns a list of all available agents with their names and descriptions."""
    return [
        {
            "agent_id": agent_id,
            "name": profile["name"],
            "description": profile["description"],
        }
        for agent_id, profile in AGENT_PROFILES.items()
    ]


def main():
    print("🚀 Starting MCP server...")
    mcp.run()


# This allows the server to be run directly too
if __name__ == "__main__":
    main()
