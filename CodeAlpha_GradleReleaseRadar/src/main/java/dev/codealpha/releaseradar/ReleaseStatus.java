package dev.codealpha.releaseradar;

public record ReleaseStatus(String version, String commit) {
    public String healthJson() {
        return "{\"status\":\"healthy\",\"version\":\"%s\",\"commit\":\"%s\"}".formatted(version, commit);
    }
}
