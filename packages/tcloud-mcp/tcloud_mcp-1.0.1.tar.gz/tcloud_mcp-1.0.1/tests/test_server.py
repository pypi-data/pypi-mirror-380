#!/usr/bin/env python3
"""
Simple test script for Tencent Cloud SDK MCP Server

This script tests the MCP server by sending JSON-RPC requests via stdin/stdout.
"""

import json
import subprocess
import sys
import os


def test_mcp_server():
    """Test basic MCP server functionality."""

    # Path to the main.py script
    script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "main.py")

    # Test requests
    test_requests = [
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "test-client", "version": "1.0.0"}
            }
        },
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": {}
        }
    ]

    try:
        # Start the MCP server
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print("Testing Tencent Cloud SDK MCP Server...")
        print("=" * 50)

        for i, request in enumerate(test_requests, 1):
            print(f"\nTest {i}: {request['method']}")
            print(f"Request: {json.dumps(request, indent=2)}")

            # Send request
            request_line = json.dumps(request) + "\n"
            process.stdin.write(request_line)
            process.stdin.flush()

            # Read response
            response_line = process.stdout.readline()
            if response_line:
                try:
                    response = json.loads(response_line.strip())
                    print(f"Response: {json.dumps(response, indent=2)}")

                    if "error" in response:
                        print(f"❌ Error: {response['error']}")
                    else:
                        print("✅ Success")

                except json.JSONDecodeError as e:
                    print(f"❌ Invalid JSON response: {response_line}")
                    print(f"Error: {e}")
            else:
                print("❌ No response received")

        # Terminate the process
        process.terminate()
        process.wait(timeout=5)

        print("\n" + "=" * 50)
        print("Test completed!")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        if 'process' in locals():
            process.kill()
        return False

    return True


def test_sdk_availability():
    """Test if Tencent Cloud SDK is available in the system."""
    print("Checking Tencent Cloud SDK availability...")

    try:
        import tencentcloud.common
        print("✅ Tencent Cloud SDK is available")

        # Check SDK version
        try:
            import tencentcloud
            sdk_version = getattr(tencentcloud, '__version__', 'unknown')
            print(f"   SDK Version: {sdk_version}")
        except:
            print("   SDK Version: unknown")

        return True

    except ImportError:
        print("❌ Tencent Cloud SDK not found. Please install it first:")
        print("   pip install tencentcloud-sdk-python")
        return False
    except Exception as e:
        print(f"❌ Error checking SDK: {e}")
        return False


def test_dependencies():
    """Test if all required dependencies are available."""
    print("Checking dependencies...")

    dependencies = [
        ('jmespath', 'jmespath'),
        ('six', 'six')
    ]

    all_available = True

    for name, module in dependencies:
        try:
            __import__(module)
            print(f"✅ {name} is available")
        except ImportError:
            print(f"❌ {name} not found")
            all_available = False
        except Exception as e:
            print(f"❌ Error importing {name}: {e}")
            all_available = False

    return all_available


if __name__ == "__main__":
    print("Tencent Cloud SDK MCP Server Test Suite")
    print("=" * 40)

    # Check dependencies first
    print("Step 1: Checking dependencies...")
    deps_ok = test_dependencies()
    print()

    # Check SDK availability
    print("Step 2: Checking SDK...")
    sdk_ok = test_sdk_availability()
    print()

    # Run MCP server tests if everything is available
    if deps_ok and sdk_ok:
        print("Step 3: Testing MCP server...")
        test_mcp_server()
    else:
        print("Skipping MCP server tests due to missing dependencies.")
        print("\nTo install missing dependencies:")
        print("   pip install -r requirements.txt")
        sys.exit(1)