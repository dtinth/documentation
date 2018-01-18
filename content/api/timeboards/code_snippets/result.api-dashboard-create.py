
{
    'dash': {
        'description': 'An informative timeboard.',
        'created': '2015-12-17T21:29:40.890824+00:00',
        'modified': '2015-12-17T21:29:40.890824+00:00',
        'read_only': 'True',
        'graphs': [
            {
                'definition': {'events': [],
                               'requests': [{'q': 'avg:system.mem.free{*}'}],
                               'viz': 'timeseries'},
                'title': 'Average Memory Free'
            }],
        'id': 4952,
        'template_variables': [
            {
                'default': 'host:my-host',
                'name': 'host1',
                'prefix': 'host'
            }],
        'title': 'My Timeboard'},
    'resource': '/api/v1/dash/4952',
    'url': '/dash/dash/4952'
}
