package dev.codealpha.releaseradar;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
class ReleaseStatusTest {
    @Test void reports_a_traceable_healthy_release() {
        assertEquals("{\"status\":\"healthy\",\"version\":\"1.0.0\",\"commit\":\"abc123\"}", new ReleaseStatus("1.0.0", "abc123").healthJson());
    }
}
