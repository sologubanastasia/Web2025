import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Lab3Application {

	public static void main(String[] args) {
		System.out.println(System.getProperty("java.home"));
		SpringApplication.run(Lab3Application.class, args);
	}

}
