from medspacy.postprocess import Postprocessor, PostprocessingRule, PostprocessingPattern
from medspacy.postprocess import postprocessing_functions

postprocess_rules = [
    PostprocessingRule(
        # Pass in a list of patterns
        patterns=[
            # The pattern will check if the entitie's section is in list of bad sections
            PostprocessingPattern(condition=lambda ent: ent._.section_category, success_value="follow_up"),
        ],
        # If all patterns are True, this entity will be removed.
        action=postprocessing_functions.remove_ent,
        description="Remove any entities from the Follow Up section. This is often the final section of the note which may help us identify end of note abbreviations that are not labeled."
    ),
    # Instantiate our rule
    PostprocessingRule(
        # Pass in a list of patterns
        patterns=[
            # The pattern will check if the entitie's section is in list of bad sections
            PostprocessingPattern(condition=lambda ent: ent._.section_category, success_value="med_list"),
        ],
        # If all patterns are True, this entity will be removed.
        action=postprocessing_functions.remove_ent,
        description="Remove any entities from the Active Meds section."
    ),
#     PostprocessingRule(
#         # Pass in a list of patterns
#         patterns=[
#             # The pattern will check if the entitie's section is in list of bad sections
#             PostprocessingPattern(condition=lambda ent: ent._.section_category, success_value="problem_list"),
#         ],
#         # If all patterns are True, this entity will be removed.
#         action=postprocessing_functions.remove_ent,
#         description="Remove any entities from the Problem List section."
#     ),
    PostprocessingRule(
        # Pass in a list of patterns
        patterns=[
            # The pattern will check if the entitie's section is in list of bad sections
            (PostprocessingPattern(condition=lambda ent: ent._.section_category, success_value="abbrev_List"))
        ],
        # If all patterns are True, this entity will be removed.
        action=postprocessing_functions.remove_ent,
        description="Remove any entities from the Abbreviation List section."
    ),
    PostprocessingRule(
        # Pass in a list of patterns
        patterns=[
            # The pattern will check if the entitie's section is in list of bad sections
            PostprocessingPattern(condition=lambda ent: ent._.section_category, success_value="plan"),
        ],
        # If all patterns are True, this entity will be removed.
        action=postprocessing_functions.remove_ent,
        description="Remove any entities from the Plan section."
    ),
        
    PostprocessingRule(
        # Pass in a list of patterns
        patterns=[
            # The pattern will check if the entitie's section is in list of bad sections
            (PostprocessingPattern(condition=lambda ent: ent._.section_category, success_value="goals"))
        ],
        # If all patterns are True, this entity will be removed.
        action=postprocessing_functions.remove_ent,
        description="Remove any entities from the Goals section."
    )

]
