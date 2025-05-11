import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

import lombok.Data;

@Component
@ConfigurationProperties(prefix = "casdoor")
@Data
public class OpenIdConnectProperties {

    private String connectEndpoint;
    private String connectClientId;
    private String connectClientSecret;
}