# django-alpine-formset
Django and Alpine JS go great together. This package provides a set of template tags 
to easily work with Django formsets in frontend code using Alpine JS.

The simplest way you'll ever find to work with formsets in frontend code. 

## Installation
```python
pip install django-alpine-formset
```
Add to `INSTALLED_APPS` in `settings.py`
```python
INSTALLED_APPS = [
    ...
    'alpineformset',
    ...
]
```

Finally include Alpine JS somewhere on your page. This package does not include Alpine JS, 
however there is a convienence template tag `alpine_js` to load the latest 3.x-version from CDN.

## Usage
All functionality is provided through two template tags, `formset_x_data` and `emptyform`. 
New forms are added by incrementing the `TOTAL_FORMS` variable set in the `x-data` attribute.

Example:
```html
{% load formset_tags %}

{% alpine_js %}  {# Convenience tag to include Alpine JS #}

<div x-data="{% formset_x_data formset %}">
    {{ formset.management_form }}
    {% for form in formset %}
        {{ form }}
    {% endfor %}
    {# Important: include this directly after the list of existing forms #}
    {% emptyform %}
        {{ formset.empty_form }}
    {% endemptyform %}
    <button type="button" x-on:click="TOTAL_FORMS++">Add Form</button>
</div>
```
