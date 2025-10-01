# Next.js Project Structure Guide

## Top-Level Folders

```
my-app/
├── app/           # App Router
├── pages/         # Pages Router
├── public/        # Static assets
└── src/           # Optional source folder
```

## Top-Level Files

```
my-app/
├── next.config.js     # Next.js configuration
├── package.json       # Project dependencies
├── middleware.ts      # Request middleware
├── .env              # Environment variables
├── tsconfig.json      # TypeScript configuration
└── .gitignore        # Git ignore file
```

## App Router Routing Files

Key routing files in each route segment:

```
app/
├── layout.js          # Shared layout
├── page.js            # Page content
├── loading.js         # Loading state UI
├── error.js           # Error handling UI
├── not-found.js       # 404 page
└── route.js           # API endpoint
```

## Dynamic Routes

```
app/
├── blog/
│   └── [slug]/
│       └── page.js   # Dynamic route segment
└── posts/
    └── [...slug]/    # Catch-all route
        └── page.js
```

## Route Organization Strategies

### Private Folders
- Prefix with underscore: `_folderName`
- Excludes folder from routing

### Route Groups
- Use parentheses: `(marketing)`
- Organize routes without affecting URL path

## Metadata Files

```
app/
├── favicon.ico        # Favicon
├── icon.png           # App icon
├── opengraph-image.jpg # Open Graph image
└── robots.txt         # SEO robots file
```

## Recommended Project Organization

1. Store shared components/utilities outside `app`
2. Colocate route-specific components within route segments
3. Use route groups to organize complex routing structures

## Best Practices

- Keep routing logic separate from implementation details
- Use private folders for internal components
- Leverage route groups for logical organization
- Utilize Next.js file-based routing conventions