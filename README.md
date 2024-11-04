# Project README

 **Structure examples**:

   - Run the script from the command line as follows:

     ```bash
     python jet_brain.py <path_to_code_folder> dataset.json> <num_examples> <examples_per_file>
     ```
     I did with num_examples=40 and examples_per_file=40 and the files text_analyzer.py and image_processor.py from the example_code folder

Output: This will generate dataset.json with structured examples in three parts: prefix, middle, and suffix.

**Use run_tiny_starcoder.py to load the dataset and run the model for each code completion example.**;
   - Run the script from the command line as follows:

     ```bash
     python run_tiny_starcoder.py dataset.json dataset_with_completions.json
     ```
Output: This will generate dataset_with_completions.json with structured examples in three parts: before, to_complete, and after.

**Evaluating Model Performance**;
- Run the script from the command line as follows:

     ```bash
     python metrics.py
     ```
Output: The script will print scores for each metric to help evaluate the model’s accuracy.


Several paths have to be changed in order to execut the project localy.
