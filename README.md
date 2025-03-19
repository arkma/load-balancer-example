# Example Dashboard Application
This example shows how basic load balancer works, based on nginx.
In backend we define some unique id via `uuid` that is returned in `/api/hello` endpoint.

Then in the nginx config we define `upstream` (multiple destinations), so we can balance the load.
## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/arkma/ngxing-loadbalancer.git
    cd ngxing-loadbalancer
    ```

3. **Build the containers:**
    ```sh
    docker-compose build
    ```
4. **Start the app:**
    ```sh
    docker-compose up
    ```

3. **Open the app in your browser:**
    ```
    http://127.0.0.1:80/api/hello
    ```

3. Update the page multiple times, and see how the id changes.
    Each backend has its unique id, so you can see you are reaching different backends.

## Application Diagram

Below is a diagram illustrating the architecture of the application:

![Application Diagram](app_diagram.svg)
