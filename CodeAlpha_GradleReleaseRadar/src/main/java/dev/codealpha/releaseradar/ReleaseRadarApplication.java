package dev.codealpha.releaseradar;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;

public class ReleaseRadarApplication {
    static void send(HttpExchange exchange, int status, String contentType, String body) throws IOException {
        exchange.getResponseHeaders().set("Content-Type", contentType);
        byte[] payload = body.getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(status, payload.length);
        exchange.getResponseBody().write(payload);
        exchange.close();
    }
    public static void main(String[] args) throws IOException {
        ReleaseStatus release = new ReleaseStatus(System.getProperty("app.version", "local"), System.getenv().getOrDefault("GIT_SHA", "untracked"));
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        server.createContext("/healthz", e -> send(e, 200, "application/json", release.healthJson()));
        server.createContext("/", e -> send(e, 200, "text/html", "<h1>ReleaseRadar</h1><p>Build intelligence is online.</p><pre>" + release.healthJson() + "</pre>"));
        server.start();
        System.out.println("ReleaseRadar listening on :8080");
    }
}
