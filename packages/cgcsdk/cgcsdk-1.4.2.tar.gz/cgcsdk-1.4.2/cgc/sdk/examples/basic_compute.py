#!/usr/bin/env python3
"""
Basic Compute Resource Example

This script demonstrates how to:
1. Create a compute resource
2. Check if it's ready
3. Add ports for external access
4. Clean up resources

Usage:
    python basic_compute.py
"""

import time
import cgc.sdk.resource as resource
import cgc.sdk.exceptions as exceptions


def create_web_server():
    """Deploy a basic web server"""
    
    app_name = "example-web-server"
    
    print(f"Creating web server '{app_name}'...")
    
    try:
        # Create the resource
        response = resource.resource_create(
            name=app_name,
            image_name="nginx:latest",
            cpu=1,               # 1 CPU core
            memory=2,            # 2GB RAM
            environment_data=[
                "NGINX_HOST=example.com",
                "NGINX_PORT=80"
            ]
        )
        
        if response['code'] == 200:
            print(f"✓ Web server '{app_name}' created successfully")
        else:
            print(f"✗ Failed to create web server: {response.get('message', 'Unknown error')}")
            return None
            
    except exceptions.SDKException as e:
        print(f"✗ SDK Error (code {e.code}): {e}")
        return None
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None
    
    return app_name


def wait_for_resource(app_name, max_wait=60):
    """Wait for resource to be ready"""
    
    print(f"Waiting for '{app_name}' to be ready...")
    
    waited = 0
    while waited < max_wait:
        if resource.resource_ready(app_name):
            print(f"✓ '{app_name}' is ready!")
            return True
        
        print(f"  Still starting... ({waited}s elapsed)")
        time.sleep(5)
        waited += 5
    
    print(f"✗ '{app_name}' failed to become ready within {max_wait} seconds")
    return False


def configure_ports(app_name):
    """Add ports for external access"""
    
    print(f"Configuring ports for '{app_name}'...")
    
    try:
        # Add HTTP port
        response = resource.resource_add_port(
            name=app_name,
            port_name="http",
            new_port=80,
            ingress=True  # Enable external access
        )
        
        if response['code'] == 200:
            print("✓ HTTP port (80) configured")
        else:
            print(f"✗ Failed to add port: {response.get('message', 'Unknown error')}")
            
        # List all ports
        ports = resource.resource_list_ports(app_name)
        if ports['code'] == 200 and ports.get('details'):
            print(f"Current ports for '{app_name}':")
            for port in ports.get('details')['ports']['ports']:
                print(f"  - {port.get('name', 'unknown')}: {port.get('port', 'unknown')}")
            if ports.get('details', {}).get('ingress'):
                for port in ports.get('details')['ingress']:
                    print(f"    - URL: {port.get('url')}")
                
    except Exception as e:
        print(f"✗ Error configuring ports: {e}")


def list_resources():
    """List all compute resources"""
    
    print("\nListing all compute resources:")
    
    try:
        resources = resource.compute_list()
        
        if resources['code'] == 200:
            pods = resources['details']['pods_list']
            
            if not pods:
                print("  No resources found")
                return
            
            for pod in pods:
                if 'app-name' in pod.get('labels', {}):
                    name = pod['labels']['app-name']
                    status = pod.get('status', 'Unknown')
                    restarts = pod.get('restart_count', 0)
                    
                    status_symbol = "✓" if status == "Running" else "○"
                    print(f"  {status_symbol} {name}: {status} (Restarts: {restarts})")
        else:
            print(f"  Failed to list resources: {resources.get('message', 'Unknown error')}")
            
    except Exception as e:
        print(f"  Error listing resources: {e}")


def cleanup_resource(app_name):
    """Delete a resource"""
    
    print(f"\nCleaning up '{app_name}'...")
    
    try:
        response = resource.resource_delete(app_name)
        
        if response['code'] == 200:
            print(f"✓ '{app_name}' deleted successfully")
            return True
        else:
            print(f"✗ Failed to delete: {response.get('message', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"✗ Error during cleanup: {e}")
        return False


def main():
    """Main execution flow"""
    
    print("=" * 50)
    print("CGC SDK - Basic Compute Resource Example")
    print("=" * 50)
    
    # Step 1: Create web server
    app_name = create_web_server()
    
    if not app_name:
        print("\nFailed to create web server. Exiting.")
        return
    
    # Step 2: Wait for it to be ready
    if not wait_for_resource(app_name):
        print("\nResource failed to start. Cleaning up...")
        cleanup_resource(app_name)
        return
    
    # Step 3: Configure ports
    configure_ports(app_name)
    
    # Step 4: List all resources
    list_resources()
    
    # Step 5: Ask user if they want to keep or delete the resource
    print("\n" + "=" * 50)
    user_input = input("Do you want to delete the web server? (y/n): ").lower()
    
    if user_input == 'y':
        cleanup_resource(app_name)
    else:
        print(f"✓ Keeping '{app_name}' running")
        print("  Remember to delete it when you're done to avoid charges")
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()