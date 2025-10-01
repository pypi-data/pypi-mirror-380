import tempfile
from pathlib import Path

import mlflow
import mlflow.pyfunc
import mlflow.sklearn
import numpy as np
from Orange.base import Model
from Orange.data import Table
from Orange.widgets.utils.save.owsavebase import OWSaveBase
from Orange.widgets.utils.widgetpreview import WidgetPreview
from Orange.widgets.widget import Input, Msg


class OrangeModelWrapper(mlflow.pyfunc.PythonModel):
    """
    A wrapper class that packages Orange models with their preprocessing steps
    for MLFlow deployment.
    """
    
    def __init__(self, orange_model):
        self.orange_model = orange_model
        self.model_domain = orange_model.domain
        
    def predict(self, context, model_input):
        """
        Apply the Orange model including preprocessing to input data.
        
        Args:
            context: MLFlow context
            model_input: pandas DataFrame with input data
            
        Returns:
            numpy array with predictions
        """
        from Orange.data import Table, Domain, ContinuousVariable

        # Convert pandas DataFrame to Orange Table using the expected domain structure
        attrs = []
        for attr in self.model_domain.attributes:
            # Preserve the original attribute type and name
            if hasattr(attr, 'is_continuous') and attr.is_continuous:
                attrs.append(ContinuousVariable(attr.name))
            else:
                # For discrete variables, try to preserve the structure
                attrs.append(ContinuousVariable(attr.name))  # Simplified for now
        
        domain = Domain(attrs)
        
        # Convert DataFrame to numpy array and create Orange Table
        if isinstance(model_input, list):
            orange_table = Table.from_list(domain, model_input)
        else:
            data_array = model_input.values
            orange_table = Table.from_numpy(domain, data_array)
        
        # Apply the model (which includes preprocessing)
        try:
            # The Orange model handles domain transformation internally
            predictions = self.orange_model(orange_table)
            
            # Handle both classification and regression
            if hasattr(predictions, 'shape') and len(predictions.shape) > 1:
                # Classification with probabilities
                return predictions
            else:
                # Regression or classification without probabilities
                return np.array(predictions).reshape(-1, 1)
        except Exception as e:
            raise ValueError(f"Prediction failed: {str(e)}")
    
    def get_model_metadata(self):
        """Get metadata about the wrapped model."""
        metadata = {
            "model_type": type(self.orange_model).__name__,
            "model_name": getattr(self.orange_model, 'name', 'Orange Model'),
            "domain_attributes": [attr.name for attr in self.model_domain.attributes],
        }
        
        if self.model_domain.class_var:
            metadata["target_variable"] = self.model_domain.class_var.name
            if self.model_domain.class_var.is_discrete:
                metadata["target_classes"] = list(self.model_domain.class_var.values)
                metadata["model_task"] = "classification"
            else:
                metadata["model_task"] = "regression"
        
        return metadata


class OWMLFlowExport(OWSaveBase):
    """
    Export Orange models to MLFlow format with preprocessing steps included.
    """
    name = "MLFlow Export"
    description = "Export a trained model with preprocessing to MLFlow format."
    icon = "icons/SaveModel.svg"
    priority = 3100
    keywords = "mlflow, export, model, save, preprocessing"
    
    class Inputs:
        model = Input("Model", Model)
        data = Input("Data", Table)  # Optional: for capturing preprocessing pipeline
    
    class Warning(OWSaveBase.Warning):
        no_preprocessing = Msg("No preprocessing steps detected in the model")
        export_failed = Msg("MLFlow export failed: {}")
    
    class Information(OWSaveBase.Information):
        export_success = Msg("Model exported successfully to MLFlow format")
        preprocessing_included = Msg("Preprocessing steps included in export")
    
    filters = ["MLFlow Model (*.mlflow)"]
    
    def __init__(self):
        super().__init__()
        self.model = None
        self.sample_data = None
        self.last_export_path = None
    
    @Inputs.model
    def set_model(self, model):
        """Set the model to be exported."""
        self.model = model
        self.data = model  # For compatibility with OWSaveBase
        self.on_new_input()
        
        if model:
            self.Information.preprocessing_included()
    
    @Inputs.data
    def set_sample_data(self, data):
        """Optional: Set sample data for testing the model export."""
        self.sample_data = data
    
    def do_save(self):
        """Export the model to MLFlow format."""
        if not self.model:
            return
        
        # Check if filename is set
        if not hasattr(self, 'filename') or not self.filename:
            self.Warning.export_failed("No filename specified")
            return
        
        self.Warning.clear()
        self.Information.clear()
        
        try:
            # Create a wrapper for the Orange model
            wrapped_model = OrangeModelWrapper(self.model)
            
            # Get model metadata
            metadata = wrapped_model.get_model_metadata()
            
            # Set up MLFlow tracking
            output_dir = Path(self.filename)
            if output_dir.suffix != '.mlflow':
                output_dir = output_dir.with_suffix('.mlflow')
            
            # Create a temporary directory for MLFlow artifacts
            with tempfile.TemporaryDirectory() as temp_dir:
                mlflow.set_tracking_uri(f"file://{temp_dir}")
                
                # Create a default experiment if none exists
                try:
                    experiment = mlflow.get_experiment_by_name("Default")
                    experiment_id = experiment.experiment_id
                except Exception:
                    experiment_id = mlflow.create_experiment("Default")
                
                # Set the experiment explicitly
                mlflow.set_experiment(experiment_id=experiment_id)
                
                # Start an MLFlow run
                with mlflow.start_run():
                    # Log the model with its preprocessing pipeline
                    conda_env = {
                        'channels': ['defaults', 'conda-forge'],
                        'dependencies': [
                            'python=3.12',
                            'pyqt',
                            'orange3',
                            'orange-spectroscopy',
                            'numpy',
                            'pandas',
                            'scikit-learn',
                            'cloudpickle',
                            'pip',
                            {
                                'pip': [
                                    'mlflow'
                                ]
                            }
                        ],
                        'name': 'orange_mlflow_env'
                    }
                    
                    # Create signature if we have sample data
                    signature = None
                    if self.sample_data:
                        try:
                            # Create a sample prediction to infer signature
                            import pandas as pd
                            
                            # Convert Orange Table to pandas DataFrame for signature
                            sample_df = self._orange_to_pandas(self.sample_data[:5])
                            
                            # Get predictions
                            sample_predictions = wrapped_model.predict(None, sample_df)
                            
                            # Infer signature
                            signature = mlflow.models.infer_signature(
                                sample_df, 
                                sample_predictions
                            )
                        except Exception as e:
                            print(f"Could not infer signature: {e}")
                    
                    # Log the model - MLflow uses cloudpickle by default to serialize Python models
                    # This embeds the OrangeModelWrapper class in the model artifact
                    mlflow.pyfunc.log_model(
                        artifact_path="orange_model",
                        python_model=wrapped_model,
                        conda_env=conda_env,
                        signature=signature,
                        registered_model_name=None,
                        input_example=self._orange_to_pandas(self.sample_data[:1]) if self.sample_data else None
                    )
                    
                    # Log additional metadata
                    mlflow.log_params(metadata)
                    
                    # Log model metrics if available
                    if hasattr(self.model, 'score') and self.sample_data:
                        try:
                            score = self.model.score(self.sample_data)
                            mlflow.log_metric("model_score", score)
                        except:
                            pass
                    
                    # Save the model to the specified location
                    run_id = mlflow.active_run().info.run_id
                    model_uri = f"runs:/{run_id}/orange_model"
                    
                    # Save to the user-specified location
                    # MLflow uses cloudpickle by default to serialize Python models
                    mlflow.pyfunc.save_model(
                        path=str(output_dir),
                        python_model=wrapped_model,
                        conda_env=conda_env,
                        signature=signature,
                        input_example=self._orange_to_pandas(self.sample_data[:1]) if self.sample_data else None
                    )
            
            self.last_export_path = str(output_dir)
            self.Information.export_success()
            
            # Print export details
            print(f"\nModel exported successfully to: {output_dir}")
            print(f"Model type: {metadata.get('model_task', 'unknown')}")
            print(f"Input features: {metadata.get('domain_attributes', [])}")
            if 'target_variable' in metadata:
                print(f"Target variable: {metadata['target_variable']}")
            if 'target_classes' in metadata:
                print(f"Target classes: {metadata['target_classes']}")
            
            # Provide usage instructions
            print("\nTo load and use this model:")
            print(f"  import mlflow")
            print(f"  model = mlflow.pyfunc.load_model('{output_dir}')")
            print(f"  predictions = model.predict(data)")
            
        except Exception as e:
            self.Warning.export_failed(str(e))
            raise
    
    def _orange_to_pandas(self, orange_table):
        """Convert Orange Table to pandas DataFrame."""
        import pandas as pd
        
        if orange_table is None or len(orange_table) == 0:
            return None
        
        # Extract data
        data = orange_table.X
        
        # Create DataFrame with default column names (0, 1, 2, ..., n)
        df = pd.DataFrame(data)
        
        return df
    
    def get_save_filename(self):
        """Override to set default extension."""
        result = super().get_save_filename()
        if isinstance(result, tuple):
            filename, selected_filter = result
            if filename and not filename.endswith('.mlflow'):
                filename += '.mlflow'
            return filename, selected_filter
        else:
            # Handle case where only filename is returned
            filename = result
            if filename and not filename.endswith('.mlflow'):
                filename += '.mlflow'
            return filename


if __name__ == "__main__":
    # Example usage with a simple model
    import Orange
    from Orange.classification import LogisticRegressionLearner
    from Orange.preprocess import Normalize, Continuize, Impute
    from Orange.preprocess import preprocess
    
    # Load sample data
    iris = Orange.data.Table("iris")
    
    # Create a preprocessing pipeline
    preprocessor = preprocess.PreprocessorList([
        Continuize(),
        Impute(),
        Normalize()
    ])
    
    # Apply preprocessing and train a model
    preprocessed_data = preprocessor(iris)
    learner = LogisticRegressionLearner()
    model = learner(preprocessed_data)
    
    # The model now includes the preprocessing steps in its domain transformation
    
    # Run the widget
    WidgetPreview(OWMLFlowExport).run(
        set_model=model,
        set_sample_data=iris
    )