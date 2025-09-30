from . import server
import asyncio

def main():
    """Main entry point for the package."""
    print("Hello, World!")
    asyncio.run(server.main())
    
    
def hello():
    print("Hello, World!")

# Optionally expose other important items at package level
__all__ = ['main', 'server', 'hello']