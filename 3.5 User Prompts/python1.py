```python
# Used to process tabular sample data
import pandas as pd


def generate_user_prompt(row: pd.Series):
    # 1. Respondent persona description
    persona = f"""
The current year is 2022. You are a respondent selected for the China Social Work Longitudinal Survey. Your profile is as follows:

You are a {row.get('Age')}-year-old Chinese {row.get('Sex')} currently living in {row.get('City')}. Your household registration type is {row.get('Household registration')}, 
and your ethnicity is {row.get('Ethnicity')}. Your highest level of education is {row.get('Highest education')}; your current job position is {row.get('Job position')}; 
you have worked in social work for {row.get('Working years')} years; and your service field is {row.get('Service field')}. 
During the past year, you received the following professional training from your organization: {row.get('Professional training')}. 
The highest-level social worker professional qualification certificate you currently hold is {row.get('Qualification certificate')}.
""".strip()

    # 2. Questionnaire item blocks
    # Only the first three items of each scale are shown here.
    # All 26 items should be included in the actual implementation.
    # Items from different dimensions are stored as separate variables and
    # inserted into the User Prompt through {ca_block}, {se_block}, and
    # {j3_block}, respectively, to keep the prompt structure clear and manageable.

    # Knowledge-dimension item block: child abuse awareness scale
    ca_block = """
CA_B: Constantly monitoring and suspecting children, making them feel mistrusted
CA_D: Frequently using insulting language to scold children
CA_E: Constantly telling children that their father (mother) does not want them
...
""".strip()

    # Attitude-dimension item block: service-efficacy scale
    se_block = """
SE_A: I help service users change their circumstances and improve their quality of life.
SE_B: I help service users address problems at the individual, family, and societal levels.
SE_C: I help service users address one or two key problems that can improve their lives.
...
""".strip()

    # Behavior-dimension item block: professional-ethics fit scale
    j3_block = """
J3_A: I use my professional authority responsibly.
J3_B: I am able to distinguish between professional relationships and personal relationships.
J3_C: I am able to identify ethical dilemmas in my work.
...
""".strip()

    # 3. Integrate the persona description and questionnaire item blocks
    # into a complete User Prompt
    user_prompt = f"""
{persona}

Please answer all of the following questions by selecting the option that best reflects your own position.

[Part I: Knowledge Items]
Question: The following items assess your knowledge. Do you consider each of the following parental behaviors to constitute child abuse (inappropriate treatment)?

Response codes:
1 = Definitely not
2 = Probably not
3 = Uncertain
4 = Probably yes
5 = Definitely yes

Please respond:
{ca_block}

[Part II: Attitude Items]
Question: To what extent do you agree with the following statements?

Response codes:
1 = Strongly disagree
2 = Disagree
3 = Neutral
4 = Agree
5 = Strongly agree

Please respond:
{se_block}

[Part III: Behavior Items]
Question: To what extent do you agree with the following statements?

Response codes:
1 = Strongly disagree
2 = Disagree
3 = Neutral
4 = Agree
5 = Strongly agree

Please respond:
{j3_block}
""".strip()

    return user_prompt
```
