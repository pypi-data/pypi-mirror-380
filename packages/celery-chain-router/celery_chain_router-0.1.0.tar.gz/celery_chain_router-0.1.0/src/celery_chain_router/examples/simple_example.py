"""
Simple example demonstrating the chain router.

This example shows how to set up the ChainRouter with a Celery application
and run tasks that will be distributed using the chain-based algorithm.
"""

import socket
import redis
from celery_chain_router import ChainRouter
from celery_chain_router.examples.tasks import app, process_data, analyze_result

# Create and configure the chain router with reset to clean state
router = ChainRouter(universe_size=1000, reset_persistent=True)

# Register workers - use simple names matching the queues
router.register_worker("worker1")
router.register_worker("worker2")
router.register_worker("worker3")

# Set task routes
app.conf.task_routes = router

if __name__ == "__main__":
    """
    Submit example tasks to demonstrate the chain router.
    
    To run this example:
    1. Start Redis: docker run -d -p 6379:6379 redis
    2. Start workers (in separate terminals):
       - celery -A celery_chain_router.examples.tasks worker -n worker1@%h -Q worker1
       - celery -A celery_chain_router.examples.tasks worker -n worker2@%h -Q worker2
       - celery -A celery_chain_router.examples.tasks worker -n worker3@%h -Q worker3
    3. Run this script: python -m celery_chain_router.examples.simple_example
    """
    # Check if Redis is running
    try:
        s = socket.socket()
        s.connect(('localhost', 6379))
        s.close()
    except:
        print("Error: Redis doesn't appear to be running.")
        print("Start Redis with: docker run -d -p 6379:6379 redis")
        exit(1)
    
    # Clear Redis to start clean
    print("Clearing Redis...")
    r = redis.Redis(host='localhost', port=6379)
    r.flushall()
    
    print(f"Router configured with workers: {router.worker_positions}")
    print("Submitting tasks...")
    results = []
    
    # Submit tasks with different parameters
    for i in range(100):
        # Vary complexity based on data_id
        complexity = 1 + (i % 5)
        
        # Submit data processing task
        result = process_data.delay(i, complexity)
        results.append(result)
        if i % 10 == 0:
            print(f"Submitted {i} tasks...")
    
    # Wait for all tasks to complete
    print("Waiting for tasks to complete...")
    completed_results = []
    for i, result in enumerate(results):
        try:
            data = result.get(timeout=30)
            completed_results.append(data)
            if i % 10 == 0:
                print(f"Completed {i}/{len(results)} tasks")
        except Exception as e:
            print(f"Error with task {i}: {e}")
    
    # Print distribution summary
    print("\nTask distribution summary:")
    worker_tasks = {}
    for result in completed_results:
        worker = result['worker']
        simple_worker = worker.split('@')[0] if '@' in worker else worker
        worker_tasks[simple_worker] = worker_tasks.get(simple_worker, 0) + 1
    
    for worker, count in worker_tasks.items():
        print(f"Worker {worker}: {count} tasks")
    
    # Run analysis tasks on the results
    print("\nSubmitting analysis tasks...")
    analysis_results = []
    for data in completed_results:
        result = analyze_result.delay(data)
        analysis_results.append(result)
    
    # Wait for analysis tasks
    print("\nWaiting for analysis tasks...")
    for i, result in enumerate(analysis_results):
        try:
            data = result.get(timeout=10)
            if i % 10 == 0:
                print(f"Completed {i}/{len(analysis_results)} analyses")
        except Exception as e:
            print(f"Error with analysis {i}: {e}")
    
    # Calculate locality benefit
    print("\nData locality analysis:")
    same_worker_count = 0
    for ar in analysis_results:
        try:
            data = ar.get(timeout=1)
            proc_worker = data['processing_worker']
            analysis_worker = data['analysis_worker']
            proc_simple = proc_worker.split('@')[0] if '@' in proc_worker else proc_worker
            analysis_simple = analysis_worker.split('@')[0] if '@' in analysis_worker else analysis_worker
            
            if proc_simple == analysis_simple:
                same_worker_count += 1
        except:
            pass
    
    if analysis_results:
        locality_percentage = same_worker_count / len(analysis_results) * 100
        print(f"Tasks that maintained data locality: {same_worker_count}/{len(analysis_results)} "
              f"({locality_percentage:.1f}%)")
    
    print("\nExample completed successfully!")
