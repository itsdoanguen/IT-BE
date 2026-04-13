# Team Coding Contract - Candidate Viewing Feature

## 1. Branching and Task Split
- Use one feature branch per workstream:
  - `feature/candidates-api`
  - `feature/candidates-matching`
  - `feature/candidates-tests`
- No direct push to main branch
- Merge via pull request only

## 2. Ownership
- BE-1: model + migrations + serializers
- BE-2: views + permissions + query validation + pagination
- BE-3: matching service + optimization
- BE-4: tests + integration support with FE

## 3. API-first Workflow
1. Freeze API contract docs in `docs/contract`
2. FE and BE approve sample payloads
3. BE implements endpoint responses exactly as contract
4. Any contract change requires docs update in same PR

## 4. Code Structure Rules
- Keep domain logic in module layer (profiles/jobs/services)
- Keep heavy scoring logic in dedicated service/helper function, not inside serializer
- Keep view methods thin: validate input, call service, return serialized data

## 5. Validation and Error Rules
- Invalid params must return 400 with structured details
- Not found resources return 404
- Empty list search returns 200 with empty array
- Auth failures return 401/403 with clear messages

## 6. Database and Migration Rules
- Any model change must include migration in same PR
- Migration names should describe intent clearly
- Never rewrite old applied migrations in shared branch

## 7. Testing Contract
Minimum test coverage required for merge:
- Auth and role access tests
- Query validation tests (bad sort, bad salary, bad availability JSON)
- Filter combination tests
- Sorting tests
- Pagination tests
- Empty result behavior tests

## 8. Performance Contract
- Use `select_related`/`prefetch_related` in list/detail APIs
- Avoid N+1 query patterns
- Add query count check in tests when possible

## 9. Pull Request Contract
Each PR must contain:
- Scope summary
- Changed files list
- API contract changes (if any)
- Migration note
- Test evidence (command + result)
- Risk and rollback note

## 10. Definition of Done
A task is done only when:
1. Code implemented and reviewed
2. Tests pass
3. API contract docs updated
4. No breaking changes to agreed payload shape
5. Ready for FE integration without extra hidden fields
