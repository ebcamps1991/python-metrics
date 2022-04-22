Querying `prometheus`
=====================

For query `prometheus` we will be using the `PromQL <https://prometheus
.io/docs/prometheus/latest/querying/basics/#querying-prometheus>`_ (Prometheus
Query Language).

Again, I encourage you to take a look at the official documentation (in
fact, what you will find here is a summarized version of what you can found
there)

Furthermore, you are aimed to take a look a some examples `here
<https://prometheus.io/docs/prometheus/latest/querying/examples/>`_.

Data types
----------

In the `PromQL`, we will be able to manage the data in one of the next types:

* Instant vector - a set of time series containing a single sample for each
  time series, all sharing the same timestamp
* Range vector - a set of time series containing a range of data points over
  time for each time series
* Scalar - a simple numeric floating point value
* String - a simple string value; currently unused

Depending on the use-case (e.g. when graphing vs. displaying the output of an
expression), only some of these types are legal as the result from a
user-specified expression. For example, an expression that returns an instant
vector is the only type that can be directly graphed.

Time series selectors
---------------------

Instant vector selector
^^^^^^^^^^^^^^^^^^^^^^^

Instant vector selectors allow the selection of a set of time series and a
single sample value for each at a given timestamp (instant): in the simplest
form, only a metric name is specified. This results in an instant vector
containing elements for all time series that have this metric name.

Range Vector Selectors
^^^^^^^^^^^^^^^^^^^^^^

Range vector literals work like instant vector literals, except that they
select a range of samples back from the current instant. Syntactically,
a range duration is appended in square brackets ([]) at the end of a vector
selector to specify how far back in time values should be fetched for each
resulting range vector element.

Offset modifier
^^^^^^^^^^^^^^^

The offset modifier allows changing the time offset for individual instant and
range vectors in a query.

Operators
---------


