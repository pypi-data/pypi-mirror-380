#!/usr/bin/env python3
"""
Port Management Example

This script demonstrates how to:
1. Create resources with multiple services
2. Add, update, and delete ports
3. Configure ingress for external access
4. List and manage port configurations

Usage:
    python port_management.py
"""

import time
import cgc.sdk.resource as resource
import cgc.sdk.exceptions as exceptions


def create_multi_service_app(app_name="multi-port-app"):
    """Create an application that needs multiple ports"""
    
    print(f"Creating multi-service application '{app_name}'...")
    
    try:
        # Create a resource that could serve multiple services
        # Using a Python image that can run multiple services
        response = resource.resource_create(
            name=app_name,
            image_name="python:3.9",
            cpu=2,
            memory=4,
            startup_command=(
                "python -c \""
                "import http.server, socketserver, threading; "
                "handlers = []; "
                "ports = [8080, 8081, 8082]; "
                "for port in ports: "
                "  handler = http.server.SimpleHTTPRequestHandler; "
                "  httpd = socketserver.TCPServer(('', port), handler); "
                "  thread = threading.Thread(target=httpd.serve_forever); "
                "  thread.daemon = True; "
                "  thread.start(); "
                "  print(f'Server started on port {port}'); "
                "import time; "
                "while True: time.sleep(1)"
                "\""
            ),
            environment_data=[
                "SERVICE_NAME=multi-port-demo",
                "ENV=development"
            ]
        )
        
        if response['code'] == 200:
            print(f"✓ Application '{app_name}' created successfully")
            return app_name
        else:
            print(f"✗ Failed to create application: {response.get('message', 'Unknown error')}")
            return None
            
    except exceptions.SDKException as e:
        print(f"✗ SDK Error (code {e.code}): {e}")
        return None


def wait_for_app(app_name):
    """Wait for application to be ready"""
    
    print(f"Waiting for '{app_name}' to be ready...")
    
    max_wait = 60
    waited = 0
    
    while waited < max_wait:
        if resource.resource_ready(app_name):
            print(f"✓ Application '{app_name}' is ready!")
            return True
        
        time.sleep(5)
        waited += 5
        print(f"  Still starting... ({waited}s elapsed)")
    
    print(f"✗ Application failed to become ready within {max_wait} seconds")
    return False


def add_application_ports(app_name):
    """Add multiple ports to the application"""
    
    print(f"\nAdding ports to '{app_name}'...")
    
    # Define ports to add
    ports_config = [
        {
            'name': 'web',
            'port': 8080,
            'ingress': True,
            'description': 'Main web interface'
        },
        {
            'name': 'api',
            'port': 8081,
            'ingress': True,
            'description': 'REST API endpoint'
        },
        {
            'name': 'admin',
            'port': 8082,
            'ingress': False,  # Internal only
            'description': 'Admin panel (internal)'
        }
    ]
    
    success_count = 0
    
    for config in ports_config:
        try:
            response = resource.resource_add_port(
                name=app_name,
                port_name=config['name'],
                new_port=config['port'],
                ingress=config['ingress']
            )
            
            if response['code'] == 200:
                ingress_status = "external" if config['ingress'] else "internal"
                print(f"  ✓ Added {config['name']} port ({config['port']}) - {ingress_status}")
                print(f"    Description: {config['description']}")
                success_count += 1
            else:
                print(f"  ✗ Failed to add {config['name']} port: {response.get('message', 'Unknown error')}")
                
        except Exception as e:
            print(f"  ✗ Error adding {config['name']} port: {e}")
    
    print(f"\nSuccessfully added {success_count}/{len(ports_config)} ports")
    return success_count > 0


def list_ports(app_name):
    """List all ports for an application"""
    
    print(f"\nCurrent ports for '{app_name}':")
    print("-" * 50)
    
    try:
        response = resource.resource_list_ports(app_name)
        
        if response['code'] == 200:
            ports = response.get('details', {}).get('ports', {}).get('ports')
            ingresses = response.get('details', {}).get('ingress')
            i_names = [i.get("port_name") for i in ingresses]
            if not ports:
                print("  No ports configured")
                return []
            print(f"  {'Port Name':<15} {'Port':<10} {'Ingress':<10}")
            print("  " + "-" * 35)
            
            for port in ports:
                name = port.get('name', 'unknown')
                number = port.get('port', 'unknown')
                ingress = "External" if port.get('name') in i_names else "Internal"
                
                print(f"  {name:<15} {number:<10} {ingress:<10}")
            
            return ports
        else:
            print(f"  Failed to list ports: {response.get('message', 'Unknown error')}")
            return []
            
    except Exception as e:
        print(f"  Error listing ports: {e}")
        return []


def update_port_configuration(app_name):
    """Update existing port configurations"""
    
    print(f"\nUpdating port configurations for '{app_name}'...")
    
    # Example: Change the API port from 8081 to 8090
    try:
        print("  Updating 'api' port from 8081 to 8090...")
        
        response = resource.resource_update_port(
            name=app_name,
            port_name='api',
            new_port=8090,
            ingress=True
        )
        
        if response['code'] == 200:
            print("  ✓ Successfully updated API port to 8090")
        else:
            print(f"  ✗ Failed to update port: {response.get('message', 'Unknown error')}")
            
    except Exception as e:
        print(f"  ✗ Error updating port: {e}")
    
    # Example: Change admin port to allow external access
    try:
        print("  Enabling external access for 'admin' port...")
        
        response = resource.resource_update_port(
            name=app_name,
            port_name='admin',
            new_port=8082,  # Keep same port
            ingress=True    # Change to external
        )
        
        if response['code'] == 200:
            print("  ✓ Admin port now accessible externally")
        else:
            print(f"  ✗ Failed to update port: {response.get('message', 'Unknown error')}")
            
    except Exception as e:
        print(f"  ✗ Error updating port: {e}")


def delete_port(app_name, port_name):
    """Delete a specific port"""
    
    print(f"\nDeleting port '{port_name}' from '{app_name}'...")
    
    try:
        response = resource.resource_delete_port(
            name=app_name,
            port_name=port_name
        )
        
        if response['code'] == 200:
            print(f"  ✓ Successfully deleted port '{port_name}'")
            return True
        else:
            print(f"  ✗ Failed to delete port: {response.get('message', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"  ✗ Error deleting port: {e}")
        return False


def demonstrate_port_scenarios(app_name):
    """Demonstrate various port management scenarios"""
    
    print("\n" + "=" * 50)
    print("Port Management Scenarios")
    print("=" * 50)
    
    # Scenario 1: Add a monitoring port
    print("\nScenario 1: Adding monitoring port")
    try:
        response = resource.resource_add_port(
            name=app_name,
            port_name='metrics',
            new_port=9090,
            ingress=False  # Internal monitoring
        )
        
        if response['code'] == 200:
            print("  ✓ Added internal monitoring port (9090)")
        else:
            print(f"  ✗ Failed: {response.get('message', 'Unknown error')}")
            
    except Exception as e:
        print(f"  ✗ Error: {e}")
    
    # Scenario 2: Add a WebSocket port
    print("\nScenario 2: Adding WebSocket port")
    try:
        response = resource.resource_add_port(
            name=app_name,
            port_name='websocket',
            new_port=8899,
            ingress=True  # External WebSocket connections
        )
        
        if response['code'] == 200:
            print("  ✓ Added WebSocket port (8899) with external access")
        else:
            print(f"  ✗ Failed: {response.get('message', 'Unknown error')}")
            
    except Exception as e:
        print(f"  ✗ Error: {e}")
    
    # Scenario 3: Try to add duplicate port (should fail)
    print("\nScenario 3: Testing duplicate port prevention")
    try:
        response = resource.resource_add_port(
            name=app_name,
            port_name='duplicate-web',
            new_port=8080,  # Already used by 'web'
            ingress=True
        )
        
        # This might succeed or fail depending on implementation
        if response['code'] == 200:
            print("  ⚠ Warning: System allowed duplicate port number")
        else:
            print("  ✓ System correctly prevented duplicate port")
            
    except Exception as e:
        print(f"  ✓ System prevented duplicate: {e}")


def cleanup_application(app_name):
    """Delete the application"""
    
    print(f"\nCleaning up application '{app_name}'...")
    
    try:
        response = resource.resource_delete(app_name)
        
        if response['code'] == 200:
            print(f"✓ Application '{app_name}' deleted successfully")
            return True
        else:
            print(f"✗ Failed to delete application: {response.get('message', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"✗ Error during cleanup: {e}")
        return False


def main():
    """Main execution flow"""
    
    print("=" * 60)
    print("CGC SDK - Port Management Example")
    print("=" * 60)
    
    # Step 1: Create application
    app_name = create_multi_service_app()
    
    if not app_name:
        print("\nFailed to create application. Exiting.")
        return
    
    # Step 2: Wait for application to be ready
    if not wait_for_app(app_name):
        print("\nApplication failed to start. Cleaning up...")
        cleanup_application(app_name)
        return
    
    # Step 3: Add initial ports
    if not add_application_ports(app_name):
        print("\nFailed to add ports. Cleaning up...")
        cleanup_application(app_name)
        return
    
    # Step 4: List current ports
    list_ports(app_name)
    
    # Step 5: Update port configurations
    update_port_configuration(app_name)
    
    # Step 6: List ports after updates
    print("\nPorts after updates:")
    list_ports(app_name)
    
    # Step 7: Demonstrate various scenarios
    demonstrate_port_scenarios(app_name)
    
    # Step 8: Final port listing
    print("\nFinal port configuration:")
    final_ports = list_ports(app_name)
    
    print(f"\nTotal ports configured: {len(final_ports)}")
    
    # Step 9: Demonstrate port deletion
    print("\n" + "=" * 60)
    user_input = input("Do you want to see port deletion? (y/n): ").lower()
    
    if user_input == 'y':
        delete_port(app_name, 'metrics')
        print("\nPorts after deletion:")
        list_ports(app_name)
    
    # Step 10: Cleanup
    print("\n" + "=" * 60)
    user_input = input(f"Do you want to delete the application '{app_name}'? (y/n): ").lower()
    
    if user_input == 'y':
        cleanup_application(app_name)
    else:
        print(f"✓ Keeping application '{app_name}' running")
        print("  You can access the configured ports externally")
        print("  Remember to delete it when you're done!")
    
    print("\n" + "=" * 60)
    print("Example completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()