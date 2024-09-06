# Overview
This is a repository of code developed and reported in the manuscript "Natural Language Processing Approaches to Identify Patient Reported Outcome Measure Documentation in Veterans Health Administration Chiropractic Clinic Notes".  

Reference: (To be updated upon publication in a peer-reviewed journal.)

# Requirements
This code uses <a href="https://github.com/medspacy/medspacy/tree/master" target="_blank">MedSpaCy</a> and <a href="https://spacy.io/" target="_blank">SpaCy</a>. 


# Rule-Based Model
Here is an example showing basic initialization and usage.  An additional example is shown under "Rule-Based-Model" as an iPython notebook.
## Initialization
```python
# Initialize environment
import spacy, medspacy
from medspacy.ner import TargetRule, TargetMatcher
from medspacy.visualization import visualize_ent
from spacy.tokens import Span

# Set up MedSpaCy Pipe and Rules
# Initialize a medspacy pipe
nlp = medspacy.load()
print('Initial Pipe: ', nlp.pipe_names)
if 'medspacy_context' in nlp.pipe_names:
  nlp.remove_pipe('medspacy_context') # Removes the MedSpaCy context component which will not be used in this application
print("Updated Pipe: ", nlp.pipe_names)

# Register a new custom attribute to store measureType
Span.set_extension("measureType", default="dflt", force=True)

# Add the TargetMatcher component
from PROM_TargetRules import target_rules

target_matcher = nlp.get_pipe("medspacy_target_matcher")
target_matcher.add(target_rules)

# Add the Sectionizer component
from medspacy.section_detection import Sectionizer
from medspacy.section_detection import SectionRule
from PROM_SectionRules import section_rules

sectionizer = nlp.add_pipe("medspacy_sectionizer")
sectionizer.add(section_rules)

# Add the Postprocessor component
from medspacy.postprocess import Postprocessor, PostprocessingRule, PostprocessingPattern
from medspacy.postprocess import postprocessing_functions
from PROM_PostProcessorRules import postprocess_rules

postprocessor = nlp.add_pipe("medspacy_postprocessor", config={"debug": False})
postprocessor.add(postprocess_rules)
```

## Basic Usage
```python
sampleNote = """
This is an example text note for demonstration purposes.
We are searching for patient reported outcome measures documented in this text, such as the PEG-3 or the Neck Disability Index.
The pipeline will exclude mentions in certain sections like Goals of Care or Abbreviations.
That way, if the PEG-3 showed up in these sections they would be ignored until another section.
If a section heading like Subjective was then present, the model would find and include mentions of the PEG-3 again.
"""

visualize_ent(nlp_medsp(note))
```
`Output:`

--- Will insert a picture of output here ---


# Statistical and Machine Learning Models
Additional architecture configuration files are included under "ML Configurations" for initializing the following models in SpaCy:
- Bag of Words Model
- Convoluted Neural Network Model
- Ensemble Model (Linear Bag-of-Words + Tok2Vec)


# Acknowledgements
The contents of this manuscript represent the view of the authors and do not necessarily reflect the position or policy of the U.S. Department of Veterans Affairs, the National Institutes of Health, nor the United States Government. This material is based upon work supported by the National Center for Complementary & Integrative Health of the National Institutes of Health under Award Number K08AT011570. Successful completion of this study also builds on support of previous work by the Department of Veterans Affairs, Veterans Health Administration, Office of Research and Development, and Health Services Research and Development IIR-12-118 and CIN-13-407, and the NCMIC Foundation.

