# Learning metrics and beyond

This repository holds all the materials created for the Metrics examples
 that aims to introduce and exercise the metrics collection, code
  instrumentation and ploting.
  
Please, follow the next steps for building the docs and read it.

* Build the docs in html for instance:
  * ``docker-compose run docs make html``
* Run the docs web server to access it throw your browser:
  * ``docker-compose up docs``
  
* Go to http://localhost:8000/build/html/

Build stack to see some metrics and logs.

* Steps
 * ``docker-compose up -d``
 * Go to http://localhost:3000/ and login with credentials (admin, pydev).
 * Go to Configuration
 * Add Loki as data source.
 * Go to explore, select Loki as data source and add some query ({job="containerlogs", container_name="the name of container"})
 * Update in Run query options the time line.
