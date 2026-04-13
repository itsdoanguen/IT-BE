# Matching Algorithm Contract

## 1. Purpose
Define a stable and explainable scoring method for candidate ranking.

## 2. Input Signals
- Candidate skills
- Candidate location
- Candidate availability slots
- Candidate expected salary
- Job required skills
- Job target location
- Job required availability slots
- Job salary budget (optional)

## 3. Score Weights
Final score range: `0 -> 100`
- Skills: `50%`
- Availability: `30%`
- Location: `20%`

Formula:

`matching_score = skill_score * 0.5 + availability_score * 0.3 + location_score * 0.2`

All component scores are in `0 -> 100`.

## 4. Component Rules

### 4.1 skill_score
- Normalize skill text to lowercase
- Tokenize by comma/semicolon and trim spaces
- `skill_score = (matched_required_skills / total_required_skills) * 100`
- If job has no required skills, default `skill_score = 50`

### 4.2 availability_score
- Use set overlap over JSON slots
- `availability_score = (overlap_slots / required_slots) * 100`
- If job has no required slots, default `availability_score = 50`

### 4.3 location_score
- Exact city/region match: `100`
- Same broader region (if mapping exists): `70`
- Otherwise: `0`

## 5. Salary Adjustment (optional extension)
In this phase salary is used as filter, not a weighted score component.
If salary scoring is enabled later:
- Within budget range: `+5` bonus (capped at 100)
- Above budget max: `-10` penalty (floored at 0)

## 6. Tie-breakers
When two candidates have same `matching_score`:
1. Newer `updated_at`
2. Lower `candidate_id`

## 7. Determinism Rules
- No random factors
- Stable sorting for same inputs
- Rounding: keep one decimal place for returned `matching_score`

## 8. Validation Rules
- Missing or malformed availability JSON from request -> 400
- Unknown sort option -> 400
- Numeric parse failure for salary filters -> 400

## 9. Future Enhancements
- Add geo distance scoring with lat/lng
- Learnable weights by hiring feedback
- Industry-specific skill synonym mapping
