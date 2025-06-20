from django.shortcuts import render

def dashboard_home_view(request):
    table_config = {
        'title': 'Sample Projects Table',
        'columns': [
            {'key': 'project_name', 'header': 'Project'},
            {'key': 'client_name', 'header': 'Client'},
            {'key': 'users', 'header': 'Users'},
            {'key': 'status', 'header': 'Status'},
            # {'key': 'actions', 'header': 'Actions'} # Actions might need more complex HTML, skip for now
        ],
        'data': [
            {
                'project_name': 'Angular Project',
                'client_name': 'Albert Cook',
                'users': 'User A, User B', # Placeholder for now, could be more complex
                'status': 'Active',
            },
            {
                'project_name': 'React Project',
                'client_name': 'Barry Hunter',
                'users': 'User C',
                'status': 'Completed',
            },
            {
                'project_name': 'VueJs Project',
                'client_name': 'Trevor Baker',
                'users': 'User D, User E, User F',
                'status': 'Scheduled',
            },
            {
                'project_name': 'Bootstrap Project',
                'client_name': 'Jerry Milton',
                'users': 'User G',
                'status': 'Pending',
            },
        ]
    }
    context = {
        'table_data': table_config # Pass it as 'table_data' to avoid conflict if table_config is used elsewhere
    }
    return render(request, 'pluggable_dashboard/example_dashboard.html', context)
