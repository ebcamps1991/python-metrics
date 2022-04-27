Getting started
===============

This workshop aims to give you the basic knowledge and support the first
practices on the amazing art of collecting and plotting metrics :)

What do we have here?
---------------------

The materials of the example is in our `github <https://github.com/ebcamps1991/python-metrics>`_ and is all based on docker
and docker-compose, so your first step will be to get sure that you already
have installed and running both `docker` and `docker-compose`

The basic infrastructure for this example is:

* An application with some basic instrumentation that is already publishing
  some very basic metrics.
* A `prometheus` server configured for collecting the metrics from our app.
* A `grafana` that is configure for consuming the prometheus as data source

Architecture overview
---------------------

Here is a simple schema for the architecture.

All components are already set and configure in the `docker-compose.yml`
file and I do aim you to take a look into it just for fun :)

Let's start things up
---------------------

Running our system is as easy as running the next command

``docker-compose up``

It should start giving you logs of all components. Once everything up, you
should be able to browse `http://localhost:3000 <http://localhost:3000>`_
and get into the grafana by using: `user: admin, password: pydevs`