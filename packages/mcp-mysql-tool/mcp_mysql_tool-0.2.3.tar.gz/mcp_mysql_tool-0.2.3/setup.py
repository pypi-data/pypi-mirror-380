from setuptools import setup, find_packages

setup(
    name="mcp-mysql-tool",
    version="0.2.3",
    description="MySQL MCP Server for AI database operations",
    author="Mrbeandev",
    author_email="mrbeandev@gmail.com",
    packages=find_packages(),
    install_requires=[
        "mcp>=1.15.0",
        "mysql-connector-python>=9.0.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "mcp-mysql-tool=mcp_mysql_server.server:cli_main",
        ],
    },
)