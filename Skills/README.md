# Skills
The skills in this repository use a custom format. They are primarily inspired by the architectures of Claude and OpenAI, and are designed to dynamically load specific content to improve the efficiency of executing particular tasks.


## Workflow
```
[user] Question
   ↓
[Agent]
  Collect all skills' names + descriptions
   ↓
[LLM]
  Decide whether to use a skill
   ↓
[Agent]
  If yes → Load SKILL.md + scripts/*
   ↓
[LLM]
  Read the skill content + generate the answer
```


## SKILL.md
This mainly follows the approach of [SKILL.md](https://github.com/anthropics/skills/blob/main/template/SKILL.md), where the file begins with two fields: `name` and `description`.


## scripts
`scripts/*.py` are example references provided for the model.
