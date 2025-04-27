+++
date = 2025-04-27T13:40:35+02:00
title = "Business contracts are transport agnostic"
description = "Business contract testing is much simpler done by method calls instead of using something like PACT."
tags = ["Simplicity", "Testing", "Java"]
slug = "simple-contract-testing"
+++

I have never been a big fan of how some people equate "contract testing" with using something like [PACT][pact]. There are other ways of doing contract testing, but a lot of engineers don't seem to know this. Today, I thought I would write something about this.

[pact]: https://docs.pact.io

## Contract testing?

_Contract testing_ is about making sure that two pieces of software (usually two services) can communicate correctly with each other, and that they agree on how they should talk.

The "contract" is an agreement that "When you send me this kind of request, I'll send you this kind of response."

Contract testing checks that:

 * The consumer (the thing sending the request) is using the right format.
 * The provider (the thing answering the request) is sending back the right format.

## Testing with PACT

PACT is a testing tool that allows developers to replay recorded HTTP traffic to ensure API contracts are still met:

{{< figure src="pact.svg" alt="Figure showing PACT." caption="PACT testing is done in two phases. The first phase is recording API requests and responses. The second phase is to replay those requests against a server to ensure it returns the same responses." >}}

PACT does this by recording and replaying API traffic. You record the API traffic and store the request and response in a recording file (called a "pact"). Once you have a recording file, you can rerun it against a server (and its future versions) and assert that it returns the same response as in the recording.

PACT is mostly a tool to ensure your API is forward/backward compatible and you don't break any previous/future API contracts.

## Business contract testing

The biggest problem with how PACT is being used is its to a transport protocol (in this case HTTP[^1]). In most cases, it is _not_ the transport protocol, nor the JSON parser[^2], the test foremost intends to test. Most contract tests test things that relate to "business contracts", such as

 * old business actions (such as "creating a user", or "uploading a file") work with the new API (where fields are usually missing).
 * new business actions (adding a new field) work with older APIs/server versions.

[^1]: PACT supports transport protocols other than HTTP, for example, various message passing protocols such as ActiveMQ, RabbitMQ, SNS, SQS, Kafka, and Kinesis. However, that's mostly irrelevant to this article.

[^2]: ...if it's a JSON API.

Of course, you want to make sure that your JSON parser can parse a JSON request and map it to a variable. And of course, you want to make sure that your web server can receive a request. But those are _two_ basic tests. All other business contract tests do not need to test this.

## Testing without PACT

The modern way of doing API development involves defining an API schema in a high-level <abbr title="Domain-Specific Language">DSL</abbr>, such as [gRPC][grpc] or [OpenAPI][openapi], and using those to generate a client and server. If you do this, your generator will have implemented a server interface that you must implement your server in. By doing so, *your RPC library implicitly takes care of mapping your transport protocol and parsing*, and then makes **basic method calls** to your implemented methods.

[grpc]: https://grpc.io
[openapi]: https://www.openapis.org

### An example

Let's say we have an OpenAPI schema for a "Hello World" server:
```yaml
openapi: 3.0.3
info:
  title: Hello World API
  description: A simple API that returns "Hello, {name}!"
  version: 1.0.0
servers:
  - url: https://api.example.com/v1
paths:
  /hello:
    get:
      summary: Returns a personalized Hello World message
      parameters:
        - name: name
          in: query
          description: The name of the person to greet
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Hello, John!
```
The generated (Java) server `interface` would look something like this:

```java
package com.example.api;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.BeanParam;

@Path("/hello")
public interface HelloWorldApi {

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
    public MessageResponse hello(@BeanParam HelloWorldRequest params);
}
```
where your `HelloWorldRequest` would be
```java
package com.example.model;

import javax.ws.rs.QueryParam;

public class HelloWorldRequest {

    @QueryParam("name")
    private String name;

    public HelloWorldRequest() {}

    public HelloWorldRequest(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```
Since our server now is implemented using a basic Java class, writing our API contract test is _really simple_:
```java
package com.example.api;

import com.example.model.HelloWorldRequest;
import com.example.model.MessageResponse;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class HelloWorldApiImplTest {

    @Test
    void testHelloWithName() {
        HelloWorldApiImpl api = new HelloWorldApiImpl();
        HelloWorldRequest request = new HelloWorldRequest("John");

        MessageResponse response = api.hello(request);

        assertEquals("Hello, John!", response.getMessage());
    }
}
```
Notice, I am not recording any traffic, not starting up a web server, not making any HTTP calls, nor am I serialising any JSON.

If we later would like our `HelloWorldApiImpl` server to support first name and last name, we could easily extend our `HelloWorldRequest` to support that and write unit tests that assert the old behaviour still works, too. Our HelloWorldRequest would turn into this:
```java
package com.example.model;

import javax.ws.rs.QueryParam;

public class HelloWorldRequest {

    /**
     * @deprecated Use firstname and lastname instead.
     */
    @Deprecated
    @QueryParam("name")
    private String name;

    @QueryParam("firstname")
    private String firstname;

    @QueryParam("lastname")
    private String lastname;

    public HelloWorldRequest() {}

    public HelloWorldRequest(String name) {
        this.name = name;
    }

    public HelloWorldRequest(String firstname, String lastname) {
        this.firstname = firstname;
        this.lastname = lastname;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
}
```
and our updated unit test file would look like this:
```java
package com.example.api;

import com.example.model.HelloWorldRequest;
import com.example.model.MessageResponse;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class HelloWorldApiImplTest {

    @Test
    void testDeprecatedHelloWithName() {
        HelloWorldApiImpl api = new HelloWorldApiImpl();
        HelloWorldRequest request = new HelloWorldRequest("John");

        MessageResponse response = api.hello(request);

        assertEquals("Hello, John!", response.getMessage());
    }

    @Test
    void testHelloWithFirstnameAndLastname() {
        HelloWorldApiImpl api = new HelloWorldApiImpl();
        HelloWorldRequest request = new HelloWorldRequest();
        request.setFirstname("Jane");
        request.setLastname("Doe");

        MessageResponse response = api.hello(request);

        assertEquals("Hello, Jane Doe!", response.getMessage());
    }
}
```
In other words, testing business APIs _can_ be done without having to make any HTTP calls. This makes the tests simpler & faster to run - easier to understand, easier to execute, easier to debug, without having to start up any web server for every test suite run.

## Controllers and services

Strictly speaking, an RPC library is not needed for method-based API contract testing. In layered software design, _controllers_ take care of transport protocol (HTTP) work, and delegate actual business work to a _service_ through basic method calls. Here is an example:
```java
package com.example.controller;

import com.example.model.HelloWorldRequest;
import com.example.service.HelloWorldService;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/hello")
public class HelloWorldController extends HttpServlet {

    private final HelloWorldService helloWorldService;

    // Constructor injection: Now the controller simply takes a HelloWorldService as a parameter
    public HelloWorldController(HelloWorldService helloWorldService) {
        this.helloWorldService = helloWorldService;
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // Parse query parameters manually
        String name = req.getParameter("name");
        String firstname = req.getParameter("firstname");
        String lastname = req.getParameter("lastname");

        // Build HelloWorldRequest object
        HelloWorldRequest helloWorldRequest = new HelloWorldRequest();
        helloWorldRequest.setName(name);
        helloWorldRequest.setFirstname(firstname);
        helloWorldRequest.setLastname(lastname);

        // Delegate to HelloWorldService for business logic
        String message = helloWorldService.hello(helloWorldRequest);

        // Prepare HTTP response
        resp.setContentType("application/json");
        resp.setCharacterEncoding("UTF-8");

        // Write JSON response manually
        PrintWriter writer = resp.getWriter();
        writer.write("{\"message\":\"" + escapeJson(message) + "\"}");
        writer.flush();
    }

    // Simple JSON escaping
    private String escapeJson(String str) {
        return str.replace("\"", "\\\"");
    }
}
```
If you have a controller like this, you can write plenty of simple unit tests to make sure that `HelloWorldService.hello(...)` does what it's supposed to do. Testing of `HelloWorldController` must be done using HTTP calls (that's its responsibility) and can be done by injecting a [test double][test-doubles] with preprogrammed canned answers.

[test-doubles]: https://martinfowler.com/bliki/TestDouble.html

## When PACT is useful

PACT can be useful in two cases:

 * Blackbox testing of services where you can't control the source code implementation;
 * Testing of a legacy service where refactoring is a major risk undertaking, and some automated testing must be in place first.

## Closing thoughts

Unfortunately, "contract testing" has become synonymous with "testing using the transport protocol". It doesn't have to be that way. Most API testing can be done without transport protocol or serialisation considerations (such as HTTP or JSON). I hope this article has proven this.
