# API Contract - Candidates V1

## 1. Common Rules
- Base path: `/api/v1`
- Auth: JWT required
- Role: employer only (`vai_tro=cong_ty`)
- Content type: `application/json`
- Pagination fields in response:
  - `page`
  - `limit`
  - `total`
  - `results`

## 2. GET /api/v1/candidates
Candidate list for discovery screen.

### Query Params
- `page` (optional, int, default `1`, min `1`)
- `limit` (optional, int, default `20`, min `1`, max `100`)
- `sort` (optional, enum)
  - `matching_desc`
  - `updated_desc`
- `q` (optional, string) - search by candidate name or skills
- `location` (optional, string)
- `salary_min` (optional, number)
- `salary_max` (optional, number)
- `availability_slots` (optional, JSON array string)
  - example: `["Mon-AM","Tue-PM"]`

### Success Response 200
```json
{
  "page": 1,
  "limit": 20,
  "total": 2,
  "results": [
    {
      "candidate_id": 101,
      "full_name": "Nguyen Van A",
      "avatar_url": "https://cdn.example.com/candidates/101.jpg",
      "primary_skills": ["python", "django", "rest"],
      "location": "HCM",
      "expected_salary": 22000,
      "matching_score": 82.5,
      "updated_at": "2026-04-13T09:30:00Z"
    }
  ]
}
```

### Empty Result 200
```json
{
  "page": 1,
  "limit": 20,
  "total": 0,
  "results": []
}
```

### Validation Error 400
```json
{
  "error": "bad_request",
  "details": {
    "salary_min": "Must be a valid number"
  }
}
```

## 3. GET /api/v1/jobs/{job_id}/matched-candidates
Candidate list matched against one job.

### Path Params
- `job_id` (required, int)

### Query Params
Same as `GET /api/v1/candidates`.

### Extra Behavior
- `matching_score` is computed against target job requirements
- If `job_id` not found: 404

### Success Response 200
```json
{
  "page": 1,
  "limit": 20,
  "total": 1,
  "results": [
    {
      "candidate_id": 101,
      "full_name": "Nguyen Van A",
      "avatar_url": "https://cdn.example.com/candidates/101.jpg",
      "primary_skills": ["python", "django", "rest"],
      "location": "HCM",
      "expected_salary": 22000,
      "matching_score": 91.0,
      "updated_at": "2026-04-13T09:30:00Z"
    }
  ]
}
```

### Not Found 404
```json
{
  "error": "not_found",
  "message": "Job not found"
}
```

## 4. GET /api/v1/candidates/{candidate_id}
Candidate detail for summary/profile view.

### Path Params
- `candidate_id` (required, int)

### Success Response 200
```json
{
  "candidate_id": 101,
  "full_name": "Nguyen Van A",
  "avatar_url": "https://cdn.example.com/candidates/101.jpg",
  "location": "HCM",
  "expected_salary": 22000,
  "skills": ["python", "django", "rest"],
  "availability_slots": ["Mon-AM", "Tue-PM"],
  "experience": [
    {
      "title": "Backend Developer",
      "company": "ABC Tech",
      "start_date": "2023-01-01",
      "end_date": "2025-12-31",
      "description": "Built APIs and optimized SQL queries"
    }
  ],
  "review_summary": {
    "avg_rating": 4.5,
    "total_reviews": 8
  },
  "reviews": [
    {
      "rating": 5,
      "comment": "Reliable and fast learner",
      "created_at": "2026-01-20T10:00:00Z"
    }
  ],
  "certifications": []
}
```

### Not Found 404
```json
{
  "error": "not_found",
  "message": "Candidate not found"
}
```

## 5. Auth/Error Contract

### 401 Unauthenticated
```json
{
  "error": "unauthorized",
  "message": "Authentication credentials were not provided"
}
```

### 403 Wrong Role
```json
{
  "error": "forbidden",
  "message": "Employer role required"
}
```

## 6. Notes for FE-BE Integration
- FE should always send `page`, `limit`, and `sort` explicitly
- FE should encode `availability_slots` as JSON array string
- FE should not expect extra fields outside this contract
- `matching_score` is always included in list responses
