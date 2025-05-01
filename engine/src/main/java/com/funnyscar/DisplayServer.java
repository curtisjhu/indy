package com.funnyscar;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class DisplayServer {
    public static void main(String[] args) throws IOException {
        // Create an HttpServer instance listening on port 8000
        HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);

        // Set up a context and assign a handler
        server.createContext("/", new ServerHandler());

        // Start the server
        server.setExecutor(null); // creates a default executor
        server.start();

        System.out.println("Server is running on http://localhost:8000/");
    }

    static class ServerHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String response = "Hello, this is a simple HTTP server response!";
            exchange.sendResponseHeaders(200, response.length());
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}
