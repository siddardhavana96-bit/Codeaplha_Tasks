FROM gradle:8.12-jdk21 AS build
WORKDIR /workspace
COPY . .
RUN gradle --no-daemon test jar
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /workspace/build/libs/release-radar-*.jar app.jar
RUN apt-get update && apt-get install --no-install-recommends -y wget && rm -rf /var/lib/apt/lists/* && useradd --system --uid 10001 appuser
USER appuser
EXPOSE 8080
HEALTHCHECK --interval=20s --timeout=3s CMD wget -qO- http://localhost:8080/healthz || exit 1
ENTRYPOINT ["java", "--add-modules=jdk.httpserver", "-jar", "app.jar"]
