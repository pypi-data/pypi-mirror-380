"""
Dashboard views for Django CFG Tasks app.

Provides template-based dashboard views for task monitoring.
"""

import logging
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

logger = logging.getLogger(__name__)


@staff_member_required
def dashboard_view(request):
    """
    Main dashboard view for task monitoring.
    
    Provides a comprehensive overview of:
    - Queue status and statistics
    - Worker information
    - Task execution metrics
    - Recent task history
    """
    try:
        # Use simulator to get data
        from ..utils.simulator import TaskSimulator
        simulator = TaskSimulator()
        
        # Prepare context data
        context = {
            'queue_status': simulator.get_current_queue_status(),
            'task_stats': simulator.get_current_task_statistics(),
        }
        
        return render(request, 'tasks/pages/dashboard.html', context)
        
    except Exception as e:
        logger.error(f"Dashboard view error: {e}")
        
        # Provide fallback context for error cases
        context = {
            'queue_status': {
                'error': str(e),
                'queues': {},
                'workers': 0,
                'redis_connected': False,
                'timestamp': None
            },
            'task_stats': {
                'error': str(e),
                'statistics': {'total': 0},
                'recent_tasks': [],
                'timestamp': None
            }
        }
        
        return render(request, 'tasks/pages/dashboard.html', context)
