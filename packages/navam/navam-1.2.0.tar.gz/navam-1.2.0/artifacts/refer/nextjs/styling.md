# Tailwind CSS Setup for Next.js 15.5

## Installation
```bash
pnpm add -D tailwindcss @tailwindcss/postcss
```

## PostCSS Configuration
```javascript
// postcss.config.mjs
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
```

## Global CSS Setup
```css
/* app/globals.css */
@import 'tailwindcss';
```

## Root Layout Integration
```typescript
// app/layout.tsx
import './globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

## Example Page Styling
```typescript
// app/page.tsx
export default function Page() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
    </main>
  )
}
```

## Best Practices
- Use Tailwind's utility classes for most styling needs
- Import global styles in the root layout
- Use CSS Modules for component-specific styles when Tailwind is insufficient
- Maintain consistent naming conventions
- Avoid auto-sorting import rules that might disrupt CSS ordering