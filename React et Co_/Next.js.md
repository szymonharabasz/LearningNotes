Components have the type `NextPage`.
API endpoints in the subdirectory `pages/api` are async functions of the signature
```ts
export default async function handler( 
	req: NextApiRequest, res: NextApiResponse 
): Promise<NextApiResponse<responseItemType[]> | void> { ... }
```
where `responseItemType` is a custom entity type.
Dynamic URLs are defined with files like:
```
api/weather/[zipcode].ts
```
And the value of the parameter can be extracted from `req.query.zipcode`. A catch-all route:
```
api/weather/[...zipcode].ts
```
will match not only `api/weather/12345`, but also `api/weather/location/12345`.

CSS can be scoped to specific Next components. This is done by naming the files like `<component>.module.css`. The selectors used in such a file are automatically prefixed to avoid naming conflicts. But because of that, one cannot use the classes as they are, but rather import the file and treat is as a JavaScript object:
```ts
import styles from "../styles/Home.module.css"

const Home: NextPage = () => {
	return (
		<div className={styles.container}>
		</div>
	)
}
```
One can also define styles object in TypeScript:
```tsx
import { CSSProperties } from 'react'

const body: CSSProperties = { };

<Text style={body}>Hello</Text>
```
With `pages`-based routing we have a hook:
```ts
import { useRouter } from "/next/router
```
that allows for programmatic navigation.
#### Routing based on the app directory
The root project directory contains the `app` directory. Inside there are subdirectories corresponding to routes e.g. `users`. This will correspond to the route `usees`. 
Inside of them there are files with names following Convention-Over-Configuration:
`page.tsx|jsx`.
for routes returning a markup, or
`layout.tsx|jsx`
for layouts, or
`route.tsx|jsx`
for API routes.
Extension `js` is also allowed (?)
Other files in the route folders are not accessible from the web browser. This is different behavior than in the case of `pages`-based routing.

**Subroutes** are created as subdirectories. **Dynamic routes** are also created as directory names with parameters in square brackets, like `[id]`. Parameter value is accessible in `props`, like `props.params.id`. **Query parameters** are accessible through `props`, like `props.searchParams.sortOrder`.

All components in the `app` directory are server-side components by default. `pages` directory does not support server-side components by default, one has to do some extra effort.

But server-side components allow caching:
```jsx
const res = awaut fetch(endpoint, {
	next: {revalidate: 10}
});
```
Disabling the cache:
```jsx
const res = await fetch(endpoint, {
	cache: 'no-store'
});
```
The rendering is static when Next.js sees that the data to populate the component is static.

We make a component into a client component just by adding
```tsx
'use client';
```
at the top of the source file which is going to be the root of the client part of the component hierarchy.
Now, client components cannot be `async`.

In client components, we cannot use `<Link>`. With `app`-based routing we have a hook:
```tsx
import { useRouter } from "/next/navigation
// ...
const router = useRouter();
// ...
<button onClick={() => router.push('/users')}>Create</button>
```
that allows for programmatic navigation.
For error handling, one can create a component error.tsx at any level of route directories hierarchy or global-error.tsx directly in the app directory to handle also errors that occur in the layout component. They must be client components. Next.js injects into them.
```ts
interface Props {
	error: Error,
	reset: () => void
};
// ...
<button onClick={() => reset()}>Retry</button>
```
###### Layouts
In `layout.tsx` in any route subdirectory, valid for this route and its subroutes:
```tsx
interface Props {
	children: ReactNode;
}
// ...
<div>{children}</div>
```
###### API routes
(in `route.tsx`)
```tsx
export function GET(request: NextRequest) {
	return NextResponse.json([
		{ id: 1, name: "Max"},
		{ id: 2, name: "John" },
	]);
}

export async function POST(request: NextRequest) {
	const body = await request.json();
	return NextResponse.json(body);
}
```
Setting response status:
```
return NextResponse.json(
	{error: "User not found"},
	{status: 404}
)
```
There are also `props` including, e.g., `params` that can be injected as a second parameter.
#### Authentication with NextAuth.js
In the file `app/api/auth/authOptions.ts`
```ts
import { NextAuthOptions } from 'next-auth' 
import GoogleProvider from 'next-auth/providers/google'
import CredentialsProvider from 'next-auth/providers/credentials'
import { PrismaAdapter } from '@next-auth/prisma-adapter'
import { prisma } from '@/prisma/client'
import bcrypt from 'bcrypt'

export const authOptions: NextAuthOptions = {
	// If we need to store some data in a database
	adapters: PrismaAdapter(clinet),
	providers: [
		// One option
		GoogleProvider({
			clientId: process.env.GOOGLE_CLIENT_ID!,
			secretSecret: process.env.GOGLE_CLIENT_SECRET!
		}),
		// Another option
		CredentialsProvider({
			name: 'Credentials',
			credentials: {
				emaasyncil: { label: "Email", type: 'email', 
					placeholder: 'Email'},		
				password: { label: "Password", type: 'password', 
					placeholder: 'Password'},
			},
			async authorize(credentials, req) {
				if (!credentials?.email || !credentials?.password) {
					return null;
				}
				const user =  await prisma.user.findUnique({
					where: { email: credentials.email }
				})
				if (!user) return null;
			
				// Assuming that hashedPassword is defined in the User
				// model from prisma, it should be optional, because in the
				// case of social login we do not store password
				// in the database				
				const passwordsMatch = bcrypt.compare(
					credentials.password, 
					user.hashedPassword!);
				return passwordsMatch ? user : null;
			},
		})
	],
	// If database adabter is used and we want social login
	session: {
		strategy: 'jwt'
	}
};
```
In the file `app/api/auth/[...nextauth]/route.ts`
```tsx
import NextAuth from 'next-auth';
import { authOptions } from '../authOptions'

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST }
```
We need `adapter` only if we want to store some user- or session-related information in a database. **For the `PrismaAdapter` we need also to define models as described in the `NextAuth` documentation.** Adding an adapter changes the default `strategy` to `database`, therefore we need to change it to `jwt` to be able to use OAuth.
In `.env`:
```sh
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=<long random string, e.g., output of openssl rand -base64 32>
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
```
In markup:
```tsx
<Link href="/api/auth/signin">Sign In</Link>
```
###### Accessing session info on the server
```tsx
import { getServerSession } from 'next-auth';
import { authOptions } from './api/auth/[...nextauth]/route';

export default async function Home {
	const session = await getServerSession(authOptions);
}

	return (
		<main>
			<h1>Hello { session && <span>{session.user!.name}</span}</h1>
		</main>
	);
}
```
###### Accessing session info on the client
Create a new client component that wraps `SessionProvider`:
```tsx
'use client';
import { SessionProvider } from 'next-auth/react';
import { ReactNode } from 'react';

const AuthProvider = ({children}: {children: ReactNode}) => {
	return (
		<SessionProvider>{children}</SessionProvider>
	)
}

```
###### Signing out
```tsx
<Link href="/api/auth/signout">Sign Out</Link>
```
and wrap everything that needs the session information in `<AuthProvider>...</AuthProvider>`.
Then in the component that needs session informatiion:
```tsx
'use client';

import { useSession } from 'next-auth/react';
// ...
const {status, data: session} = useSession();
// ...
{ status === 'authenticated' && <div>{session.user!.name}</div> }
```
###### Protecting routes with NextAuth middleware
In `middleware.ts`:
```ts
// export default object that is imported from this module
export { default } from 'next-auth/middleware'

export config = ...
```
#### Defining a middleware
In a file `middleware.ts` **outside** of the `app` directory:
```ts
export function middleware(request: NextRequest) {
	// Second argument is base URL
	return NextResponse.redirect(new URL('/new=page', request.url));
}

export const config = {
	// * zero or more parameters
	// + one or more parameters
	// ? zero or one
	matcher: ['/users/:id*']
}
```
#### Common Next components
`Head` from `next/head` can contain `<title>` and `<meta>`
`Link` from `next/link` can be used to navigate to internal pages:
```tsx
<Link href="/components/weather"> Weather </Link>
```
Thanks to it, we can replace the the content of the page with an appropriate component, without redownloading all the resources linked by the whole page.

`Image` from `next/image`. It optimizes images serving them in a compact `webp` format. It allows to include images while setting useful properties:
```tsx
import coffee from "@/public/images/coffee.jpg";

// "main" by default is "static", if Image has set "fill", 
// then its parent must have one of the following classes
<main className="relative|absolute|fixed h-screen">
<Image
	// src="/vercel.svg"
	src={coffee}
	alt="Coffee"
	// width={72}
	// height={16}
	fill
	style={{ objectFit: 'cover|contain' }}
	//Tailwind: className="object-cover|object-contain"
	// sizes="100vw" <- 100% of viewport
	// For mobile. tablets, desktops:
	sizes="(max-width: 480px) 100vw, (max-width: 768px) 50vw, 33wv"
	quality={100} // from 1 to 100
	priority // not lazy loading
	/>
</main>
```
Defining domains from which we can serve images. This is for security. In `next.config.js`:
```ts
const nextConfig = {
	images: {
		remotePatterns: [{
			protocol: 'https',
			hostname: 'example.com',
			port: '',
			pathname: '/account123/**',
		},]
	}

}
```
`Suspense` to show loading UI etc.
```tsx
<Suspense fallback={<p>Loading...</p>}>
	<!-- What is going to be shown after loading is finished -->
</Suspense>
```
`Script` from "next/script". Inline scripts can cause errors when referencing global JS objects. A way out is to make them into strings:
```tsx
<Script
	id="unique-id"
	strategy="afterInteractive|beforeInteractive|lazyOnload|worker">
	{`window.dataLayer = ...`}
</Script>
```
#### Pre-rendering modes
###### Static Site Generation (SSG)
Formally looks the same as SSR, but with `...Static...` instead of `...ServerSide...`.
###### Server-Side Rendering (SSR)
One has to define an additional async function `getServerSideProps`:
```tsx
import type {
	GetServerSideProps,
	GetServerSidePropsContext,
	InferGetServerSidePropsType,
	NextPage,
	PreviewData
} from "next";
import { ParsedUrlQuery } from "querystring";
import { fetchNames } from "../utils/fetch-names";

type responseItemType = { id: string; name: string; };

const NamesSSR: NextPage = (
	props: InferGetServerSidePropsType<typeof getServerSideProps>
) => {

	const output = props.names.map((item: responseItemType, idx: number) => {
		return ( 
			<li key={`name-${idx}`}>
				{item.id} : {item.name}
			</li> 
		); 
	});
	
	return ( 
		<ul> 
			{output}
		</ul>
	);
};

export const getServerSideProps: GetServerSideProps = async ( 
	context: GetServerSidePropsContext<ParsedUrlQuery, PreviewData> 
) => {

	let names: responseItemType[] | [] = [];
	try { 
		names = await fetchNames(); 
	} catch(err) {} 
	return {
		props: {
			names
		}
	};
};

export default NamesSSR;
```
###### Incremental Static Regeneration
One has to define the time (in seconds) after which the initially pre-rendered HTML will be invalidated:
```jsx
	return {
		props: {
			names,
			revalidate: 30
		}
	};
```
#### NPM scripts
Development mode:
```shell
npm run dev
```
Building for production
```shell
npm run build
```
Running the app in production:
```shell
npm start
```

#### Tailwind CSS
###### Example utility classes
Padding
```
p-[number]
px-[number]
py-[number]
p[t|r|b|l]-[number]
```
Margins
```
m-[number]
m[x|y|t|r|b|l]-[number]
```
Text:
```
text-[xs|sm|base|lg|xl|2xl|3xl|...]
text-sky-500
text-[color] # Google Tailwind Color Palette
font-[thin|light|normal|medoum|bold]
```
Background:
```
bg-[color]
```
Pseudoclasses:
```
hover:bg-sky-900
```
Flex and spacing
```
flex space-x-3
```
###### Overriding default style for a given element type
```css
@layer base {
	h1 {
		@apply font-extrabold text-2xl mb-3;
	}
}
```
###### Input validation with Zod
Validation schema
```ts
import { z } from 'zod';

export default const schema = z.object({
	name: z.string().min(3),
	email: z.string().email(),
	age: z.number(),
});

schema.parse(body); // throws an exception
const validation = schema.safeParse(body);
if (!validation.success) {
	return NextResponse.json(validation.error.errors)
}
```
#### Misc
###### Using custom fonts
```tsx
const poppins = localFont({
	src: "../public/fonts/poppins-regular-webfont.woff2".
});

<body className={poppins.className}>
// ...
</body>
```
###### Lazy loading
Component:
```tsx
import dynamic from "next/dynamic"
const HeavyComponent = dynamic(
	() => import("./components/HeavyComponent),
	{
		ssr: false,
		loading: () => <p>Loading...</p>
	}
);
// ...
<HeavyComponent />
```
External library, where it is needed, for example a click handler:
```tsx
const _ = (await import('lodash')).default;
_.orderBy(users, ['name']);
```
###### VSCode shortcuts
Cmd+p - searching a given file
Cmd+space - code completion
Cmd+d - multiple cursor
IntelliSense for a React component `rafce`