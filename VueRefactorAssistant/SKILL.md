I have a large Vue component files (`.vue`) using the Vue 3 Composition API, and it has become hard to understand and maintain.
I want to modularize it step by step without changing the existing behavior.

Important:
- Please do not refactor everything at once.
- Please do not make design, UI, or behavior changes unless I explicitly ask for them.
- Please keep the existing logic as unchanged as possible.
- If something is unclear, make a conservative assumption and clearly mention it.
- If the existing code uses TypeScript, please use TypeScript as well.
- If this is a Nuxt project, please follow Nuxt conventions such as `pages`, `components`, `composables`, `useRoute`, `useRouter`, `useFetch`/`$fetch`, etc.
- The goal is better maintainability, not a complete rewrite.
- Please answer in English and provide complete code blocks, not partial snippets.

Please proceed step by step:

## Step 1: Analyze the component

Analyze the component and briefly explain:

1. Which responsibilities are currently mixed together in this file, for example:
   - Template/UI
   - API calls
   - Form state
   - Validation
   - Routing
   - Dialogs/modals
   - Tables/lists
   - Actions such as save, delete, publish, submit, cancel, duplicate, export, etc.
   - Data transformation or formatting
   - Permissions or feature flags
   - Side effects such as watchers, lifecycle hooks, or subscriptions

2. Which UI sections should reasonably be extracted into their own child components.

3. Which logic should reasonably be extracted into one or more composables.

4. Which helper logic should be moved into utility files, if applicable.

5. Which types or interfaces should be moved into dedicated type files, if applicable.

6. Which parts should intentionally stay in the original `.vue` file for now to keep the refactoring small and low-risk.

## Step 2: Suggest a target structure

Suggest a reasonable target structure based on the actual component.

For example:

```txt
components/
  ExampleHeader.vue
  ExampleForm.vue
  ExampleActions.vue
  ExampleDialog.vue

composables/
  useExampleData.ts
  useExampleForm.ts
  useExampleActions.ts

types/
  example.ts

utils/
  exampleMappers.ts
  exampleFormatters.ts
```

Please briefly explain what each suggested file would be responsible for.

Important:
- Do not force this exact structure.
- Suggest only files that are actually useful for this component.
- Prefer a small number of well-named files over many tiny abstractions.

## Step 3: Implement the first concrete refactoring step

For the first step, create ONLY the most important new composable.

This composable should contain the central business logic, state management, and API calls.

Please follow these rules:

- Output the complete code for the new composable file.
- Use the Vue 3 Composition API.
- Use TypeScript if the existing code uses TypeScript.
- Preserve the existing API calls as much as possible.
- Preserve existing state names where it makes sense.
- Avoid unnecessary abstractions.
- Do not extract UI components in this step.
- Do not rewrite the template in this step.
- Do not introduce a new state management library unless it is already used.
- Do not change naming conventions unless there is a clear reason.
- If a minimal usage example is helpful, show it separately after the composable code.

The composable should include, where applicable:

- Props-derived or route-derived ID handling, if currently done in the component
- Loading state
- Error state
- Fetch/load function
- Save/create/update function, if present
- Delete/action functions, if present
- Submit handlers that contain business logic
- Relevant computed values with business meaning
- Watchers or lifecycle hooks related to data loading or business state
- Mapping between API data and local state, if present
- Permission/availability checks, if present

The composable should NOT include:

- Template code
- CSS
- Purely visual state such as whether a dropdown, tooltip, tab, accordion, or modal is open, unless it is connected to business logic
- Purely presentation-related formatting
- Component-specific DOM logic
- Styling decisions
- Markup structure
- UI-only event handling

## Step 4: Explain the return values and integration

After the code, briefly explain:

1. What exactly was extracted.
2. Which values and functions the composable returns.
3. How the original `.vue` component should later import and use this composable.
4. Which old code blocks in the original `.vue` file can then be removed or replaced.
5. Which risks or areas I should test carefully.

## Step 5: Stop

Please stop after this first composable step.

Do not create any UI child components yet.

Wait for my approval before we continue extracting the UI components step by step.
