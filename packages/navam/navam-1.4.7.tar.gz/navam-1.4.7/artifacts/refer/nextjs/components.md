# Server vs Client Components in Next.js

## Key Differences

### Server Components
- **Use When**:
  - Fetching data from databases or APIs
  - Using API keys or secrets
  - Reducing JavaScript sent to browser
  - Improving initial page load performance

### Client Components
- **Use When**:
  - Needing state and event handlers
  - Using lifecycle effects
  - Accessing browser-only APIs
  - Implementing custom hooks

## Implementation

### Adding Client Components
Use the `"use client"` directive at the top of a file:

```typescript
'use client'

import { useState } from 'react'

export default function InteractiveComponent() {
  const [count, setCount] = useState(0)
  return (
    <div>
      <p>{count} likes</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  )
}
```

## Best Practices

- Minimize client-side JavaScript by using Server Components
- Add `"use client"` only to components that require interactivity
- Pass data from Server Components to Client Components via props
- Use context providers carefully in client-side code

## Example Pattern

```typescript
// Server Component (page.tsx)
export default async function Page() {
  const post = await getPost(id)
  return <LikeButton likes={post.likes} />
}

// Client Component (like-button.tsx)
'use client'
export default function LikeButton({ likes }) {
  // Interactive logic here
}
```

This approach leverages server-side rendering for performance while maintaining client-side interactivity where needed.