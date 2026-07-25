# Nuxt boundaries for SFC decomposition

Apply existing project conventions before introducing a new structure. Nuxt
runtime behavior can make a seemingly local extraction affect data loading,
server rendering, routing, or imports.

## Data access

Distinguish `useFetch` from `$fetch` by the project's established server and
client data-flow pattern. Preserve caching, keying, error, pending, and
serialization behavior when moving remote I/O. Do not move a request merely to
reduce component size.

## Runtime context

Identify whether code runs on server, client, or both. Guard browser-only APIs
without changing hydration output. Preserve server-to-client data transfer and
avoid introducing work that differs during hydration.

## Auto-imports and locations

Confirm local conventions for auto-imported composables and utilities. Keep page
and layout responsibilities separate from reusable components. Place a
composable, component, or module where its ownership and reuse scope are clear,
not where it avoids an import.

## Routes and middleware

Keep route parameters, navigation side effects, middleware behavior, and URL
state observable across an extraction. Test navigation and failure handling when
the component uses route state.

## Verification question

What server, client, route, or data-loading behavior could differ after moving
this concern, and which targeted check would expose that difference?
