# Overview
This is a repository of code developed and reported in the manuscript "Natural Language Processing Approaches to Identify Patient Reported Outcome Measure Documentation in Veterans Health Administration Chiropractic Clinic Notes".  

Reference: (To be updated upon publication in a peer-reviewed journal.)

# Requirements
This code uses <a href="https://github.com/medspacy/medspacy/tree/master" target="_blank">MedSpaCy</a> and <a href="https://spacy.io/" target="_blank">SpaCy</a>. 


# Rule-Based Model
This example shows basic initialization and usage, with source files located under "Rule-Based-Model".
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
(This is an example text note for demonstration purposes)
Subjective:
The patient presents today with low back pain.
Objective:
Physical exam is normal.
Outcome Measures:
PEG-3: 4/10 (Subscales: 3, 4, 5)
ODI: 30%
Assessment and Plan:
Initiate a trial of chiropractic care for 3-4 visits over 3-4 weeks to assess for improvement in low back pain.
Goals of Care:
Reduce PEG-3 by 1, Improve ODI by 10%
"""

visualize_ent(nlp_medsp(note))
```
`Output:`

<img src="https://github.com/BCColemanVA/OutcomeMeasure-NLP/blob/6820a688139e785c968557258b347aa229a5a39d/Images/SampleVisual.PNG">


# Statistical and Machine Learning Models
Additional architecture configuration files are included under "ML-Configurations" for initializing the following models in SpaCy:
- Bag of Words Model
- Convoluted Neural Network Model
- Ensemble Model (Linear Bag-of-Words + Tok2Vec)


# Acknowledgements
The contents of this manuscript represent the view of the authors and do not necessarily reflect the position or policy of the U.S. Department of Veterans Affairs, the National Institutes of Health, nor the United States Government. This material is based upon work supported by the National Center for Complementary & Integrative Health of the National Institutes of Health under Award Number K08AT011570. Successful completion of this study also builds on support of previous work by the Department of Veterans Affairs, Veterans Health Administration, Office of Research and Development, and Health Services Research and Development IIR-12-118 and CIN-13-407, and the NCMIC Foundation.

