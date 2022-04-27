Taking Metrics
===============

What metrics are?
-----------------

Before starting messing up with metrics, we should first get in touch with
the concept of metric. A metric can be defined as::

    A metric is a phenomena observation in a given time

This is a wide definition but is good for us since it define two important
things:

* We do take metrics on a concrete phenomena. A phenomena can be almost
  anything and the unique constrain for metric a phenomena comes on the next
  point.
* We need an observation. Typically it will be a measure over a
  phenomena. This measure will give us a magnitude and a unity (meters, times,
  ocurrences, etc).
* The observation over the time (Time series) will be our lovely metric :)

Ok, so lets talk about `prometheus`
-----------------------------------

In the `official web <https://prometheus.io/>`_, they define it as::

    Prometheus is an open-source systems monitoring and alerting toolkit
    originally built at SoundCloud.

and here is its architecture

.. image:: images/prometheus_architecture.png

As usual, I encourage you to read the
`f**king docs <https://prometheus.io/docs/introduction/overview/>`_ where
everything is preciously explain. In the meanwhile, here you have a brief
description of some key concepts that will allow us to go further within the
workshop

Data model
^^^^^^^^^^

Next, we will talk about the data model that `prometheus` expose to us and
which will be the base materials that we will use to build our dashboards.

Labels
""""""

Labels enable Prometheus's dimensional data model: any given combination of
labels for the same metric name identifies a particular dimensional
instantiation of that metric (for example: all HTTP requests that used the
method POST to the /api/tracks handler)

Samples
"""""""

Samples form the actual time series data. Each sample consists of:

* a float64 value
* a millisecond-precision timestamp

Metrics types
^^^^^^^^^^^^^

Here is a short explanation taken and simplified from the official
documentation, I encourage to take a look at the
`docs <https://prometheus.io/docs/concepts/metric_types/>`_

Counter
"""""""

A counter is a cumulative metric that represents a single monotonically
increasing counter whose value can only increase or be reset to zero on
restart. For example, you can use a counter to represent the number of
requests served, tasks completed, or errors.

Gauge
"""""

A gauge is a metric that represents a single numerical value that can
arbitrarily go up and down.
Gauges are typically used for measured values like temperatures or current
memory usage, but also "counts" that can go up and down, like the number
of concurrent requests.

Histogram
"""""""""

A histogram samples observations (usually things like request durations or
response sizes) and counts them in configurable buckets. It also provides
a sum of all observed values.

A histogram with a base metric name of <basename> exposes multiple time
series during a scrape:

    * cumulative counters for the observation buckets
    * the total sum of all observed values
    * the count of events that have been observed

Summary
"""""""

Similar to a histogram, a summary samples observations (usually things like
request durations and response sizes). While it also provides a total count of
observations and a sum of all observed values, it calculates configurable
quantiles over a sliding time window.

A summary with a base metric name of <basename> exposes multiple time series
during a scrape:

    * streaming φ-quantiles (0 ≤ φ ≤ 1) of observed events
    * the total sum of all observed values
    * the count of events that have been observed

Instances and jobs
^^^^^^^^^^^^^^^^^^

When Prometheus scrapes a target, it attaches some labels automatically to the
scraped time series which serve to identify the scraped target:

    * job: The configured job name that the target belongs to.
    * instance: The <host>:<port> part of the target's URL that was scraped.
