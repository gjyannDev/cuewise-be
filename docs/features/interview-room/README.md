# Interview Room (backend side)

The spec for this feature lives in the web app repo, and it is the single source of truth for both repos:

- **Spec:** `../cuewise-fe/docs/features/interview-room/spec.md`
  - **API Contract** section: the speech routes, error codes, limits and the 404 rules that this repo implements.
  - **Phase 0** (Aura spike) and **Phase 1** (backend) requirements.

Files in this folder:

- `plan.md`: the backend implementation plan (written by `/create-plan`), starting with the no-behaviour-change move of transcription into the generic speech layer, then TTS.
- `task.md`: backend progress tracking.

Change the contract in the spec first, then in both repos.
