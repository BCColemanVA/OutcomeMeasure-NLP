from medspacy.section_detection import Sectionizer
from medspacy.section_detection import SectionRule

section_rules = [
    SectionRule(literal="qqqqqqqqqqqqqqqqqqqqqqqqq", category="section_break",pattern=[{"LOWER":{"IN":["qqqqqqqqqqqqqqqqqqqqqqqqq"]}}]
               ), # this rule is applied for breaking apart concatenated notes from the input data
    SectionRule(literal="HPI", category="history",pattern=[{"LOWER":{"IN":["hpi"]}}]
               ),
    SectionRule(literal="pmh", category="past_medical",pattern=[{"LOWER":{"IN":["pmh","pmhx"]}}]
               ),
    SectionRule(literal="Objective", category="objective",pattern=[{"LOWER":{"IN":["objective"]}}]
               ),
    SectionRule(literal="Physical Exam", category="physical_exam",
                pattern=[
                   {"LOWER": {"FUZZY1":{"IN":["physical","phys","phy"]}}},{"LOWER": {"REGEX": "\s*"},"OP":"?"},
                   {"LOWER": {"FUZZY1":{"IN": ["examination","exam","ex"]}}},
                  ]),
    SectionRule(literal="Active Problems", category="problem_list",
               pattern=r"Active Problem(s)?"
               ),
    SectionRule(literal="Active Outpatient Medications", category="med_list",
                pattern=r"Active (Outpatient )?Medications"
               ),
    SectionRule(literal="Abbreviations",category="abbrev_List",
               pattern=r"(A|a)bbreviation(|s)"),
    SectionRule(literal="Review of Systems", category="R_O_S",
                pattern=[
                   {"LOWER": "review"},{"LOWER": {"REGEX": "\s*"},"OP":"?"},
                   {"LOWER": "of"},{"LOWER": {"REGEX": "\s*"},"OP":"?"},
                   {"LOWER": {"IN": ["systems","symptoms","system","symptom"]}},
                   
               ]),
    SectionRule(literal="Imaging", category="Imaging",
                pattern=[
                   {"LOWER": {"IN":["previous","prev","prior"]},"OP":"?"},{"LOWER": {"REGEX": "\s*"},"OP":"?"},
                   {"LOWER": {"IN": ["imaging","images"]}}, 
               ]),
    SectionRule(literal="Social History", category="social_hx",
                pattern=[
                   {"LOWER": {"FUZZY1":{"IN":["social","soc"]}}},{"LOWER": {"REGEX": "\s*"},"OP":"?"},
                   {"LOWER": {"FUZZY1":{"IN": ["history","hx"]}}},
                  ]), 
        SectionRule(literal="Family History", category="family_hx",
                pattern=[
                   {"LOWER": {"FUZZY1":{"IN":["family","fam","familial"]}}},{"LOWER": {"REGEX": "\s*"},"OP":"?"},
                   {"LOWER": {"FUZZY1":{"IN": ["history","hx"]}}},
                  ]),
        SectionRule(literal="Assessment", category="assessment",
                pattern=[
                   {"LOWER": {"FUZZY1":{"IN":["assessment"]}}}
                  ]),
        SectionRule(literal="Assessment/plan", category="assessment_plan",
                pattern=[
                   {"LOWER": {"FUZZY1":{"IN":["assessment"]}}},
                    {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                    {"LOWER": {"FUZZY1":{"IN":["plan"]}}},
                  ]),
        SectionRule(literal="plan", category="plan",),
        SectionRule(literal="goals",category="goals",
                   pattern=[{"LOWER":{"IN":["goal","goals"]}}]),
        SectionRule(literal="Follow up", category="follow_up", # Reasoning: F/U is usually the last part of the doc.  we might capture those end abbrev lists this way
                pattern=[
                   {"LOWER": {"IN":["follow","f"]}},
                    {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                    {"LOWER": {"IN":["up","u"]}},
                    {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                    {"LOWER": {"IN":["plan"]},"OP":"?"},
                  ]),
        # Added after initial review
        SectionRule(literal="outcome measures",category="outcomes",
                   pattern=[{"LOWER": {"REGEX":"outcome(s)?"}},
                    {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                    {"LOWER": {"REGEX":"measure(s)?"},"OP":"?"}]),
        SectionRule(literal="home recommendations",category="home_recs",
                   pattern=[{"LOWER": {"REGEX":"home"}},
                    {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                    {"LOWER": {"REGEX":"recommendation(s)?"}}]),
        SectionRule(literal="post treatment",category="post_treatment",
                   pattern=[{"LOWER": {"REGEX":"post(treatment)?"}},
                    {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                    {"LOWER": {"REGEX":"treatment"}}]),
        SectionRule(literal="chief complaint",category="history",
                   pattern=[{"LOWER": {"REGEX":"chief"}},
                    {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                    {"LOWER": {"REGEX":"complaint(s)?"}}]),
        SectionRule(literal="chief concern",category="history",
                   pattern=[{"LOWER": {"REGEX":"chief"}},
                    {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                    {"LOWER": {"REGEX":"concern(s)?"}}]),
        SectionRule(literal="subjective",category="history",
                   pattern=[{"LOWER": {"FUZZY1":{"IN":["subjective"]}}},
                    ]),
        SectionRule(literal="precautions",category="precautions_contra",
                   pattern=[{"LOWER": {"REGEX":"precaution(s)?"}}
                    ]),
        SectionRule(literal="contraindications",category="precautions_contra",
                   pattern=[{"LOWER": {"REGEX":"contraindication(s)?"}}
                    ]),
]