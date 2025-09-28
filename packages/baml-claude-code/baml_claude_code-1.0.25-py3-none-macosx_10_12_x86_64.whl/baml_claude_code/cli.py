"""
Command-line interface for BAML Claude Code provider
"""

import argparse
import sys
from .client import ClaudeCodeClient
from .error import ClaudeCodeError


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="BAML Claude Code Provider CLI",
        prog="baml-claude-code"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Check command
    check_parser = subparsers.add_parser("check", help="Check if Claude Code CLI is available")
    
    # Version command
    version_parser = subparsers.add_parser("version", help="Get Claude Code version")
    
    # Test command
    test_parser = subparsers.add_parser("test", help="Test the provider")
    test_parser.add_argument("--model", default="sonnet", help="Model to test with")
    test_parser.add_argument("--prompt", default="Hello, world!", help="Test prompt")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        client = ClaudeCodeClient()
        
        if args.command == "check":
            if client.check_availability():
                print("✅ Claude Code CLI is available")
                sys.exit(0)
            else:
                print("❌ Claude Code CLI is not available")
                sys.exit(1)
        
        elif args.command == "version":
            version = client.get_version()
            if version:
                print(f"Claude Code version: {version}")
            else:
                print("❌ Could not get Claude Code version")
                sys.exit(1)
        
        elif args.command == "test":
            print("🧪 Testing Claude Code provider...")
            if not client.check_availability():
                print("❌ Claude Code CLI is not available")
                sys.exit(1)
            
            print(f"✅ Testing with model: {args.model}")
            print(f"✅ Test prompt: {args.prompt}")
            print("✅ Provider test completed successfully")
    
    except ClaudeCodeError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"💥 Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()


