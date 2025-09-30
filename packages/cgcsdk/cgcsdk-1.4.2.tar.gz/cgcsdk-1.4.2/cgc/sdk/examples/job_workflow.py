#!/usr/bin/env python3
"""
Job Workflow Example

This script demonstrates how to:
1. Create and run jobs
2. Monitor job execution
3. Run sequential job pipelines
4. Handle job failures
5. Clean up succeeded jobs

Usage:
    python job_workflow.py
"""

import time
from datetime import datetime
import cgc.sdk.job as job
import cgc.sdk.exceptions as exceptions


def create_simple_job():
    """Create a simple job that prints a message"""
    
    job_name = f"hello-job-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    
    print(f"Creating simple job '{job_name}'...")
    
    try:
        response = job.job_create(
            name=job_name,
            image_name="busybox:latest",
            cpu=1,
            memory=1,
            startup_command="echo 'Hello from CGC Job!'",
            ttl_seconds_after_finished=300  # Clean up after 5 minutes
        )
        
        if response['code'] == 200:
            print(f"✓ Job '{job_name}' created successfully")
            return job_name
        else:
            print(f"✗ Failed to create job: {response.get('message', 'Unknown error')}")
            return None
            
    except exceptions.SDKException as e:
        print(f"✗ SDK Error (code {e.code}): {e}")
        return None


def create_data_processing_job(input_file, output_dir):
    """Create a job that simulates data processing"""
    
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    job_name = f"data-process-{timestamp}"
    
    print(f"Creating data processing job '{job_name}'...")
    
    try:
        response = job.job_create(
            name=job_name,
            image_name="python:3.9-slim",
            cpu=2,
            memory=4,
            environment_data=[
                f"INPUT_FILE={input_file}",
                f"OUTPUT_DIR={output_dir}",
                "PROCESSING_MODE=batch"
            ],
            # Simulate data processing with Python
            startup_command=(
                "python -c \""
                "import os, time; "
                "print(f'Processing {os.environ.get(\\\"INPUT_FILE\\\")}...'); "
                "time.sleep(5); "
                "print(f'Output saved to {os.environ.get(\\\"OUTPUT_DIR\\\")}'); "
                "print('Processing complete!')"
                "\""
            ),
            ttl_seconds_after_finished=600  # Clean up after 10 minutes
        )
        
        if response['code'] == 200:
            print(f"✓ Data processing job '{job_name}' created")
            return job_name
        else:
            print(f"✗ Failed to create job: {response.get('message', 'Unknown error')}")
            return None
            
    except Exception as e:
        print(f"✗ Error creating job: {e}")
        return None


def monitor_job(job_name, check_interval=5, max_wait=60):
    """Monitor a job until it completes or fails"""
    
    print(f"Monitoring job '{job_name}'...")
    
    start_time = time.time()
    last_status = None
    
    while time.time() - start_time < max_wait:
        try:
            response = job.job_list()
            
            if response['code'] != 200:
                print(f"✗ Failed to get job status: {response.get('message', 'Unknown error')}")
                return 'Unknown'
            
            # Find our job in the list
            job_found = False
            for j in response['details'].get('job_list', []):
                if j['name'] == job_name:
                    job_found = True
                    current_status = j.get('status', {}).get('phase', 'Unknown')
                    
                    # Only print if status changed
                    if current_status != last_status:
                        elapsed = int(time.time() - start_time)
                        print(f"  [{elapsed}s] Status: {current_status}")
                        last_status = current_status
                    
                    # Check if job finished
                    if current_status == 'Succeeded':
                        print(f"✓ Job '{job_name}' completed successfully!")
                        return 'Completed'
                    elif current_status == 'Failed':
                        print(f"✗ Job '{job_name}' failed")
                        return 'Failed'
                    
                    break
            
            if not job_found:
                print(f"  Job '{job_name}' not found (may have been cleaned up)")
                return 'NotFound'
            
            time.sleep(check_interval)
            
        except Exception as e:
            print(f"✗ Error monitoring job: {e}")
            return 'Error'
    
    print(f"✗ Job monitoring timeout after {max_wait} seconds")
    return 'Timeout'


def run_job_pipeline(pipeline_name, steps):
    """Run a sequence of jobs as a pipeline"""
    
    print(f"\nStarting pipeline: {pipeline_name}")
    print("=" * 40)
    
    succeeded_jobs = []
    failed_job = None
    
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}/{len(steps)}: {step['description']}")
        
        # Create the job
        job_name = step['create_func'](*step.get('args', []))
        
        if not job_name:
            print(f"✗ Failed to create job for step {i}")
            failed_job = f"Step {i}"
            break
        
        # Monitor the job
        status = monitor_job(job_name)
        
        if status == 'Succeeded':
            succeeded_jobs.append(job_name)
        else:
            print(f"✗ Pipeline failed at step {i}")
            failed_job = job_name
            break
    
    # Pipeline summary
    print("\n" + "=" * 40)
    print(f"Pipeline: {pipeline_name}")
    print(f"Succeeded: {len(succeeded_jobs)}/{len(steps)} steps")
    
    if failed_job:
        print(f"Failed at: {failed_job}")
    else:
        print("✓ All steps succeeded successfully!")
    
    return succeeded_jobs, failed_job


def list_all_jobs():
    """List all jobs with their status"""
    
    print("\nCurrent jobs in the system:")
    print("-" * 40)
    
    try:
        response = job.job_list()
        
        if response['code'] != 200:
            print(f"Failed to list jobs: {response.get('message', 'Unknown error')}")
            return
        
        jobs_list = response['details'].get('job_list', [])
        
        if not jobs_list:
            print("  No jobs found")
            return
        
        # Group jobs by status
        by_status = {}
        for j in jobs_list:
            status = j.get('status', {}).get('phase', 'Unknown')
            if status not in by_status:
                by_status[status] = []
            by_status[status].append(j['name'])
        
        # Display grouped jobs
        for status, names in by_status.items():
            print(f"\n{status}: ({len(names)} jobs)")
            for name in names[:5]:  # Show first 5
                print(f"  - {name}")
            if len(names) > 5:
                print(f"  ... and {len(names) - 5} more")
                
    except Exception as e:
        print(f"Error listing jobs: {e}")


def cleanup_succeeded_jobs():
    """Delete all succeeded jobs"""
    
    print("\nCleaning up succeeded jobs...")
    
    try:
        response = job.job_list()
        
        if response['code'] != 200:
            print(f"Failed to list jobs: {response.get('message', 'Unknown error')}")
            return
        
        deleted_count = 0
        for j in response['details'].get('job_list', []):
            job_phase = j.get('status', {}).get('phase')
            if job_phase == 'Succeeded':
                try:
                    delete_response = job.job_delete(j['name'])
                    if delete_response['code'] == 200:
                        deleted_count += 1
                        print(f"  Deleted: {j['name']}")
                except Exception as e:
                    print(f"  Failed to delete {j['name']}: {e}")
        
        if deleted_count > 0:
            print(f"✓ Cleaned up {deleted_count} succeeded jobs")
        else:
            print("  No succeeded jobs to clean up")
            
    except Exception as e:
        print(f"Error during cleanup: {e}")


def main():
    """Main execution flow"""
    
    print("=" * 50)
    print("CGC SDK - Job Workflow Example")
    print("=" * 50)
    
    # Example 1: Simple job
    print("\n1. Running a simple job")
    print("-" * 30)
    simple_job = create_simple_job()
    if simple_job:
        monitor_job(simple_job)
    else:
        print("✗ Simple job failed. Stopping further tests.")
        return

    # Example 2: Data processing job
    print("\n2. Running a data processing job")
    print("-" * 30)
    data_job = create_data_processing_job(
        input_file="/data/input.csv",
        output_dir="/data/output/"
    )
    if data_job:
        monitor_job(data_job)

    # Example 3: Pipeline of jobs
    print("\n3. Running a job pipeline")
    print("-" * 30)
    
    # Define pipeline steps
    pipeline_steps = [
        {
            'description': 'Extract data',
            'create_func': lambda: create_simple_job()
        },
        {
            'description': 'Process data',
            'create_func': lambda: create_data_processing_job("/tmp/extracted.csv", "/tmp/processed/")
        },
        {
            'description': 'Generate report',
            'create_func': lambda: create_simple_job()
        }
    ]
    
    succeeded, failed = run_job_pipeline("ETL Pipeline", pipeline_steps)
    
    # Show all jobs
    list_all_jobs()
    
    # Cleanup option
    print("\n" + "=" * 50)
    user_input = input("Do you want to clean up succeeded jobs? (y/n): ").lower()
    
    if user_input == 'y':
        cleanup_succeeded_jobs()
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()