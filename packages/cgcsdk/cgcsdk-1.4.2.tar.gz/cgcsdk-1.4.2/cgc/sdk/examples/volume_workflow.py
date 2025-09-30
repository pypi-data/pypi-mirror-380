#!/usr/bin/env python3
"""
Volume Workflow Example

This script demonstrates a complete volume lifecycle:
1. Create a persistent volume
2. Wait for volume to be ready
3. Create a compute resource
4. Wait for compute resource to be ready
5. Mount the volume to the compute resource
6. Demonstrate data persistence concepts
7. Unmount the volume from the compute resource
8. Delete the compute resource
9. Delete the volume

Usage:
    python volume_workflow.py
"""

import time
import cgc.sdk.volume as volume
import cgc.sdk.resource as resource
import cgc.sdk.exceptions as exceptions


def create_volume(name, size, storage_class=None):
    """Create a new volume"""

    print(f"Creating volume '{name}' with {size}GB...")

    try:
        # Get available storage classes
        available_classes = volume.get_available_storage_classes()
        print(f"Available storage classes: {available_classes}")

        # Use default if not specified
        if storage_class is None:
            storage_class = volume.get_default_storage_class()
            print(f"Using default storage class: {storage_class}")

        # Create the volume
        response = volume.volume_create(name, size, storage_class)

        if response['code'] == 200:
            print(f"✓ Volume '{name}' created successfully")
            return True
        else:
            print(f"✗ Failed to create volume: {response.get('message', 'Unknown error')}")
            return False

    except exceptions.SDKException as e:
        if e.code == -1:
            print("✗ Volume name is required")
        elif e.code == -2:
            print("✗ Invalid volume size")
        elif e.code == -3:
            print("✗ Invalid storage class")
        else:
            print(f"✗ SDK Error (code {e.code}): {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False


def wait_for_volume(name, max_wait=120):
    """Wait for volume to be ready"""

    print(f"Waiting for volume '{name}' to be ready...")

    waited = 0
    while waited < max_wait:
        if volume.volume_ready(name):
            print(f"✓ Volume '{name}' is ready!")
            return True

        print(f"  Still provisioning... ({waited}s elapsed)")
        time.sleep(5)
        waited += 5

    print(f"✗ Volume '{name}' failed to become ready within {max_wait} seconds")
    return False


def create_compute_resource(name):
    """Create a compute resource for demonstration"""

    print(f"Creating compute resource '{name}'...")

    try:
        response = resource.resource_create(
            name=name,
            image_name="ubuntu:20.04",
            cpu=1,
            memory=2,
            startup_command="sleep infinity",  # Keep container running
            environment_data=[
                "DEMO_ENV=volume_workflow",
                "DATA_PATH=/persistent_data"
            ]
        )

        if response['code'] == 200:
            print(f"✓ Compute resource '{name}' created successfully")
            return True
        else:
            print(f"✗ Failed to create compute resource: {response.get('message', 'Unknown error')}")
            return False

    except Exception as e:
        print(f"✗ Error creating compute resource: {e}")
        return False


def wait_for_compute_resource(name, max_wait=120):
    """Wait for compute resource to be ready"""

    print(f"Waiting for compute resource '{name}' to be ready...")

    waited = 0
    while waited < max_wait:
        if resource.resource_ready(name):
            print(f"✓ Compute resource '{name}' is ready!")
            return True

        print(f"  Still starting... ({waited}s elapsed)")
        time.sleep(5)
        waited += 5

    print(f"✗ Compute resource '{name}' failed to become ready within {max_wait} seconds")
    return False


def wait_for_volume_mount(volume_name, compute_name, timeout=60):
    """Wait for volume to show as mounted to the compute resource"""

    print(f"⏳ Waiting for volume '{volume_name}' to be mounted to '{compute_name}'...")
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            response = volume.volume_list()
            if response['code'] == 200:
                volumes = response['details'].get('volume_list', [])
                for vol in volumes:
                    if vol['name'] == volume_name:
                        mounted_to = vol.get('mounted_to', [])
                        # Check if compute name is in mounted_to list (might be pod name format)
                        for mount in mounted_to:
                            if compute_name in mount:
                                print(f"✓ Volume mount confirmed! Mounted as: {mount}")
                                return True
                        break
        except Exception:
            pass

        elapsed = int(time.time() - start_time)
        print(f"  Still mounting... ({elapsed}s elapsed)")
        time.sleep(3)

    print(f"⚠ Volume mount verification timed out after {timeout}s")
    print("  Note: Volume may still be mounting in the background")
    return False


def wait_for_volume_unmount(volume_name, timeout=30):
    """Wait for volume to show as unmounted"""

    print(f"⏳ Waiting for volume '{volume_name}' to be unmounted...")
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            response = volume.volume_list()
            if response['code'] == 200:
                volumes = response['details'].get('volume_list', [])
                for vol in volumes:
                    if vol['name'] == volume_name:
                        mounted_to = vol.get('mounted_to', [])
                        if not mounted_to:
                            print("✓ Volume unmount confirmed!")
                            return True
                        break
        except Exception:
            pass

        elapsed = int(time.time() - start_time)
        print(f"  Still unmounting... ({elapsed}s elapsed)")
        time.sleep(2)

    print(f"⚠ Volume unmount verification timed out after {timeout}s")
    return False


def mount_volume_to_compute(volume_name, compute_name, mount_path="/persistent_data"):
    """Mount volume to compute resource"""

    print(f"Mounting volume '{volume_name}' to compute '{compute_name}' at '{mount_path}'...")

    try:
        response = volume.volume_mount(
            name=volume_name,
            target=compute_name,
            start_mount_path=mount_path
        )

        if response['code'] == 200:
            print(f"✓ Volume mount initiated successfully")
            print(f"  Data will persist at '{mount_path}' in the container")
            print("⏳ Compute resource is reloading to apply the mount...")

            # Wait for mount to complete
            if wait_for_volume_mount(volume_name, compute_name):
                print(f"✓ Volume '{volume_name}' is now fully mounted!")
                return True
            else:
                print(f"⚠ Mount may still be in progress")
                return True  # Continue anyway as mount was initiated
        else:
            print(f"✗ Failed to mount volume: {response.get('message', 'Unknown error')}")
            return False

    except exceptions.SDKException as e:
        if e.code == -1:
            print("✗ Volume name is required")
        elif e.code == -2:
            print("✗ Target template name is required")
        else:
            print(f"✗ SDK Error (code {e.code}): {e}")
        return False
    except Exception as e:
        print(f"✗ Error mounting volume: {e}")
        return False


def list_volumes():
    """List all volumes and their status"""

    print("\nListing all volumes:")

    try:
        response = volume.volume_list()

        if response['code'] == 200:
            volumes = response['details'].get('volume_list', [])

            if not volumes:
                print("  No volumes found")
                return

            for vol in volumes:
                name = vol.get('name', 'Unknown')
                size = vol.get('size', 'Unknown').replace('Gi', '')  # Remove 'Gi' suffix
                status = vol.get('status', 'Unknown')
                storage_type = vol.get('disks_type', 'Unknown')
                mounted_to = vol.get('mounted_to', [])

                status_symbol = "✓" if status.lower() == "bound" else "○"
                mount_info = f", Mounted: {len(mounted_to)}" if mounted_to else ", Not mounted"
                print(f"  {status_symbol} {name}: {status} ({size}GB, {storage_type}{mount_info})")
        else:
            print(f"  Failed to list volumes: {response.get('message', 'Unknown error')}")

    except Exception as e:
        print(f"  Error listing volumes: {e}")


def list_compute_resources():
    """List all compute resources"""

    print("\nListing all compute resources:")

    try:
        resources = resource.compute_list()

        if resources['code'] == 200:
            pods = resources['details']['pods_list']

            if not pods:
                print("  No compute resources found")
                return

            for pod in pods:
                if 'app-name' in pod.get('labels', {}):
                    name = pod['labels']['app-name']
                    status = pod.get('status', 'Unknown')
                    restarts = pod.get('restart_count', 0)

                    status_symbol = "✓" if status == "Running" else "○"
                    print(f"  {status_symbol} {name}: {status} (Restarts: {restarts})")
        else:
            print(f"  Failed to list compute resources: {resources.get('message', 'Unknown error')}")

    except Exception as e:
        print(f"  Error listing compute resources: {e}")


def demonstrate_persistence(volume_name, compute_name):
    """Demonstrate volume persistence"""

    print(f"\n" + "=" * 50)
    print("VOLUME PERSISTENCE DEMONSTRATION")
    print("=" * 50)

    print(f"The volume '{volume_name}' is now mounted to '{compute_name}'.")
    print("This means:")
    print("  • Data written to /persistent_data will survive container restarts")
    print("  • The volume can be unmounted and remounted to other resources")
    print("  • Multiple resources can share the same volume")
    print("  • Data persists even after the compute resource is deleted")

    print("\nTo test persistence:")
    print(f"  1. Connect to the compute resource '{compute_name}'")
    print("  2. Write data to /persistent_data/")
    print("  3. Restart or recreate the compute resource")
    print("  4. Verify data still exists in /persistent_data/")


def cleanup_volume(name, force=False):
    """Unmount and delete a volume"""

    print(f"\nCleaning up volume '{name}'...")

    try:
        # First unmount from all resources
        print(f"Unmounting volume '{name}'...")
        umount_response = volume.volume_umount(name)

        if umount_response['code'] == 200:
            print("✓ Volume unmount initiated successfully")
            # Wait for unmount to complete (unless forced)
            if not force:
                wait_for_volume_unmount(name)
        else:
            print(f"⚠ Warning: Unmount response: {umount_response.get('message', 'Unknown')}")

        # Then delete the volume
        print(f"Deleting volume '{name}'...")
        delete_response = volume.volume_delete(name, force=force)

        if delete_response['code'] == 200:
            print(f"✓ Volume '{name}' deleted successfully")
            return True
        else:
            print(f"✗ Failed to delete volume: {delete_response.get('message', 'Unknown error')}")
            return False

    except Exception as e:
        print(f"✗ Error during volume cleanup: {e}")
        return False


def cleanup_compute_resource(name):
    """Delete a compute resource"""

    print(f"Deleting compute resource '{name}'...")

    try:
        response = resource.resource_delete(name)

        if response['code'] == 200:
            print(f"✓ Compute resource '{name}' deleted successfully")
            return True
        else:
            print(f"✗ Failed to delete compute resource: {response.get('message', 'Unknown error')}")
            return False

    except Exception as e:
        print(f"✗ Error during compute resource cleanup: {e}")
        return False


def unmount_volume_from_compute(volume_name, compute_name):
    """Unmount volume from compute resource"""

    print(f"\nUnmounting volume '{volume_name}' from compute '{compute_name}'...")

    try:
        response = volume.volume_umount(
            name=volume_name,
            target_template_names=[compute_name],
        )

        if response['code'] == 200:
            print(f"✓ Volume unmount initiated successfully")
            print(f"  Compute resource is reloading to apply the unmount...")

            # Wait for unmount to complete
            if wait_for_volume_unmount(volume_name):
                print(f"✓ Volume '{volume_name}' is now fully unmounted!")
                return True
            else:
                print(f"⚠ Unmount may still be in progress")
                return True  # Continue anyway as unmount was initiated
        else:
            print(f"✗ Failed to unmount volume: {response.get('message', 'Unknown error')}")
            return False

    except exceptions.SDKException as e:
        if e.code == -1:
            print("✗ Volume name is required")
        else:
            print(f"✗ SDK Error (code {e.code}): {e}")
        return False
    except Exception as e:
        print(f"✗ Error unmounting volume: {e}")
        return False


def complete_workflow_demonstration():
    """Demonstrate complete volume lifecycle with all steps"""

    print("\n" + "=" * 60)
    print("COMPLETE VOLUME LIFECYCLE DEMONSTRATION")
    print("=" * 60)

    volume_name = "demo-lifecycle-volume"
    compute_name = "demo-lifecycle-compute"
    volume_size = 5  # GB

    print("This demonstration will show the complete volume lifecycle:")
    print("  CREATE → MOUNT → UNMOUNT → DELETE")
    print()

    # Step 1: Create volume
    print("🔄 STEP 1: Creating volume...")
    if not create_volume(volume_name, volume_size):
        print("❌ Failed at volume creation")
        return False

    # Step 2: Wait for volume to be ready
    print("\n🔄 STEP 2: Waiting for volume to be ready...")
    if not wait_for_volume(volume_name):
        print("❌ Failed waiting for volume")
        cleanup_volume(volume_name)
        return False

    # Step 3: Create compute resource
    print("\n🔄 STEP 3: Creating compute resource...")
    if not create_compute_resource(compute_name):
        print("❌ Failed at compute creation")
        cleanup_volume(volume_name)
        return False

    # Step 4: Wait for compute resource to be ready
    print("\n🔄 STEP 4: Waiting for compute resource to be ready...")
    if not wait_for_compute_resource(compute_name):
        print("❌ Failed waiting for compute resource")
        cleanup_compute_resource(compute_name)
        cleanup_volume(volume_name)
        return False

    # Step 5: Mount volume to compute resource
    print("\n🔄 STEP 5: Mounting volume to compute resource...")
    if not mount_volume_to_compute(volume_name, compute_name):
        print("❌ Failed at volume mounting")
        cleanup_compute_resource(compute_name)
        cleanup_volume(volume_name)
        return False

    # Step 6: Show mounted state
    print("\n📊 STEP 6: Showing mounted state...")
    list_volumes()
    list_compute_resources()

    # Step 7: Unmount volume from compute resource
    print("\n🔄 STEP 7: Unmounting volume from compute resource...")
    if not unmount_volume_from_compute(volume_name, compute_name):
        print("❌ Failed at volume unmounting")
        cleanup_compute_resource(compute_name)
        cleanup_volume(volume_name)
        return False

    # Step 8: Delete compute resource
    print("\n🔄 STEP 8: Deleting compute resource...")
    if not cleanup_compute_resource(compute_name):
        print("❌ Failed at compute deletion")
        cleanup_volume(volume_name)
        return False

    # Step 9: Delete volume
    print("\n🔄 STEP 9: Deleting volume...")
    if not cleanup_volume(volume_name):
        print("❌ Failed at volume deletion")
        return False

    print("\n✅ COMPLETE LIFECYCLE DEMONSTRATION SUCCESSFUL!")
    print("All steps completed: CREATE → MOUNT → UNMOUNT → DELETE")
    return True


def main():
    """Main execution flow"""

    print("=" * 60)
    print("CGC SDK - Volume Workflow Example")
    print("=" * 60)

    print("This example demonstrates volume management workflows.")
    print("\nChoose a demonstration:")
    print("  1. Interactive workflow (create, mount, ask for cleanup)")
    print("  2. Complete lifecycle automation (create → mount → unmount → delete)")

    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()

        if choice == "1":
            interactive_workflow()
            break
        elif choice == "2":
            complete_workflow_demonstration()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("\n" + "=" * 60)
    print("Volume workflow example completed!")
    print("=" * 60)


def interactive_workflow():
    """Interactive workflow with user choices"""

    volume_name = "demo-persistent-storage"
    compute_name = "demo-data-processor"
    volume_size = 10  # GB

    print("\n🚀 Starting interactive workflow...")

    # Step 1: Create volume
    print("\n🔄 STEP 1: Creating volume...")
    if not create_volume(volume_name, volume_size):
        print("\nFailed to create volume. Exiting.")
        return

    # Step 2: Wait for volume to be ready
    print("\n🔄 STEP 2: Waiting for volume to be ready...")
    if not wait_for_volume(volume_name):
        print("\nVolume failed to become ready. Cleaning up...")
        cleanup_volume(volume_name)
        return

    # Step 3: Create compute resource
    print("\n🔄 STEP 3: Creating compute resource...")
    if not create_compute_resource(compute_name):
        print("\nFailed to create compute resource. Cleaning up...")
        cleanup_volume(volume_name)
        return

    # Step 4: Wait for compute resource to be ready
    print("\n🔄 STEP 4: Waiting for compute resource to be ready...")
    if not wait_for_compute_resource(compute_name):
        print("\nCompute resource failed to start. Cleaning up...")
        cleanup_compute_resource(compute_name)
        cleanup_volume(volume_name)
        return

    # Step 5: Mount volume to compute resource
    print("\n🔄 STEP 5: Mounting volume to compute resource...")
    if not mount_volume_to_compute(volume_name, compute_name):
        print("\nFailed to mount volume. Cleaning up...")
        cleanup_compute_resource(compute_name)
        cleanup_volume(volume_name)
        return

    # Step 6: List resources to show current state
    print("\n📊 STEP 6: Current state of resources...")
    list_volumes()
    list_compute_resources()

    # Step 7: Demonstrate persistence concepts
    demonstrate_persistence(volume_name, compute_name)

    # Step 8: Ask user what to do next
    print("\n" + "=" * 50)
    print("Interactive workflow completed successfully!")
    print("=" * 50)

    while True:
        print("\nWhat would you like to do next?")
        print("  1. Keep resources running (remember to clean up later)")
        print("  2. Unmount volume and delete compute only (keep volume)")
        print("  3. Complete cleanup: unmount → delete compute → delete volume")
        print("  4. Show current resource status")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("\n✓ Keeping resources running")
            print(f"  Volume: {volume_name} (mounted to {compute_name})")
            print(f"  Compute: {compute_name}")
            print("  Remember to clean up when you're done!")
            break

        elif choice == "2":
            print("\n🔄 Unmounting volume and deleting compute...")
            unmount_volume_from_compute(volume_name, compute_name)
            cleanup_compute_resource(compute_name)
            print(f"✓ Volume '{volume_name}' is preserved and can be mounted to other resources")
            break

        elif choice == "3":
            print("\n🔄 Complete cleanup sequence...")
            print("  1. Unmounting volume...")
            unmount_volume_from_compute(volume_name, compute_name)
            print("  2. Deleting compute resource...")
            cleanup_compute_resource(compute_name)
            print("  3. Deleting volume...")
            cleanup_volume(volume_name)
            print("✓ All resources cleaned up")
            break

        elif choice == "4":
            list_volumes()
            list_compute_resources()
            continue

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nWorkflow interrupted by user.")
        print("Don't forget to clean up any created resources!")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        print("Don't forget to clean up any created resources!")