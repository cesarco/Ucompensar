package application;

import org.opencv.core.Core;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class FourierTransform extends Application {
	// the main stage
		private Stage primaryStage;
		
		@Override
		public void start(Stage primaryStage)
		{
			try
			{
				// load the FXML resource
				FXMLLoader loader = new FXMLLoader(getClass().getResource("Fourier.fxml"));
				BorderPane root = (BorderPane) loader.load();
				// set a whitesmoke background
				root.setStyle("-fx-background-color: whitesmoke;");
				Scene scene = new Scene(root, 800, 600);
				scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
				// create the stage with the given title and the previously created
				// scene
				this.primaryStage = primaryStage;
				this.primaryStage.setTitle("Fourier");
				this.primaryStage.setScene(scene);
				this.primaryStage.show();
				
				// init the controller
				FT_Controller controller = loader.getController();
				controller.setStage(this.primaryStage);
				controller.init();
			}
			catch (Exception e)
			{
				e.printStackTrace();
			}
		}
		
		public static void main(String[] args)
		{
			// load the native OpenCV library
			System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
			
			launch(args);
		}
	}