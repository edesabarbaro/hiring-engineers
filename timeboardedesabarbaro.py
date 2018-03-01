#!/usr/bin/env python

from datadog import initialize, api

import urllib3
urllib3.disable_warnings()

options = {
    'api_key': 'd5adb408b3f603dc7158196e11017cb5',
    'app_key': 'c89254ee7d8e3114461e15386272271f0935037c'
}

initialize(**options)

title = "Visualizing Data for edesabarbaro"
description = "Timeboard using Datadog's API."
graphs = [

{
    "definition": {
        "events": [],
        "requests": [
            {"q": "my_metric{host:precise64}"}
        ],
        "viz": "timeseries"
    },
    "title": "My metric scoped over my host"
},

{
    "definition": {
        "events": [],
        "requests": [
            {"q": "anomalies:(avg:mysql.performance.cpu_time{host:precise64}, 'robust', 2)"}
        ],
        "viz": "timeseries"
    },
    "title": "Anomalies on MySQL for CPU time"
},

{
    "definition": {
        "events": [],
        "requests": [
            {"q": "avg:my_metric{host:precise64}.rollup(sum, 3600)"}
        ],
        "viz": "timeseries"
    },
    "title": "Rollup for My metric over the past hour"

}]

template_variables = [{
    "name": "host1",
    "prefix": "host",
    "default": "host:my-host"
}]

read_only = True
api.Timeboard.update(
                     602631,
                     title=title,
                     description=description,
                     graphs=graphs,
                     read_only=read_only)

print "hello, world"
