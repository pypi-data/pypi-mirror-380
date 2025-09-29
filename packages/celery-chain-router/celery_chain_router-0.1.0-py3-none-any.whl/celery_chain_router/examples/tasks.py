"""
Task definitions for the chain router example.
"""
from celery import Celery
import os
import time

# Create the Celery app with explicit name matching the module
app = Celery('celery_chain_router.examples.tasks')
app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    task_track_started=True,
)

# Define tasks with explicit names
@app.task(bind=True, name='celery_chain_router.examples.tasks.process_data')
def process_data(self, data_id, complexity=1):
    """Process a data item with variable complexity."""
    worker_name = self.request.hostname or os.environ.get('HOSTNAME', 'unknown')
    
    # Simulate work proportional to complexity
    time.sleep(0.1 * complexity)
    
    return {
        'data_id': data_id,
        'worker': worker_name,
        'complexity': complexity,
        'status': 'processed'
    }

@app.task(bind=True, name='celery_chain_router.examples.tasks.analyze_result')
def analyze_result(self, result):
    """Analyze a result from process_data task."""
    worker_name = self.request.hostname or os.environ.get('HOSTNAME', 'unknown')
    
    # Simulate analysis work
    time.sleep(0.05)
    
    return {
        'data_id': result['data_id'],
        'analysis_worker': worker_name,
        'processing_worker': result['worker'],
        'complexity': result['complexity'],
        'status': 'analyzed'
    } 