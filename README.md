# Django Pluggable Dashboard

`django-pluggable-dashboard` is a reusable Django app that provides a dynamic and configurable admin dashboard.

## Quick Start

1.  Install the app:
    ```bash
    pip install django-pluggable-dashboard
    ```
    *(This will be true once the package is built and uploaded to PyPI)*

    Alternatively, install directly from source:
    ```bash
    pip install -e /path/to/your/django-pluggable-dashboard/ # or git+https://your-repo-url
    ```


2.  Add `'pluggable_dashboard'` to your `INSTALLED_APPS` setting in your Django project's `settings.py`:
    ```python
    INSTALLED_APPS = [
        ...,
        'pluggable_dashboard',
    ]
    ```

3.  Include the dashboard URLs in your project's `urls.py`:
    ```python
    from django.urls import path, include

    urlpatterns = [
        ...,
        path('dashboard/', include('pluggable_dashboard.urls')),
    ]
    ```
    *(Assuming `pluggable_dashboard.urls` will be created in the next step)*

4.  Run migrations (if any, not expected for this version):
    ```bash
    python manage.py migrate
    ```

## Features

*   Dynamic table component.
*   Configurable widgets (coming soon).
*   Component-based template system.

## Usage

See the example view in `pluggable_dashboard/views.py` and the `pluggable_dashboard/templates/pluggable_dashboard/example_dashboard.html` template for how to configure and render dashboard components.
